import tkinter
from tkinter import *
from game import Game
import random

# initialization
game = Game(random.choice([True, False]))
game_start = False


# action when user choose a cell
def click_cell(idx, cell):
    if game.user.turn and game_start:
        if cell in game.grid_xy:
            grid_cells[idx].config(text="O")
            game.user.select(cell)
            game.grid_xy.remove(cell)
            clicked_var.set(idx)


# update cell color
def highlight(cells):
    for idx in cells:
        grid_cells[mapping.get(idx)].config(bg="#CDC2AE")


# reset game
def reset_game():
    global game
    game = Game(random.choice([True, False]))
    for cell in grid_cells:
        cell.config(text="", bg="#C2DED1")
    start_game()


# game process
def start_game():
    global game
    global game_start
    game_start = True

    if game.user.turn:
        lb_message.config(text="You go first", fg="#666")
    else:
        lb_message.config(text="Computer goes first", fg="#666")

    while game_start:
        if len(game.grid_xy) > 0:
            if game.user.turn:
                # wait for user to click
                btn_start.wait_variable(clicked_var)
                winning_cells = game.check(game.user)
                if len(winning_cells) > 0:
                    highlight(winning_cells)
                    break
                game.pc.turn = True
            # check if all cells are clicked again
            if len(game.grid_xy) > 0:
                pc_picked = game.pc_action()
                grid_cells[mapping.get(pc_picked)].config(text="X")
                winning_cells = game.check(game.pc)
                if len(winning_cells) > 0:
                    highlight(winning_cells)
                    break
                game.user.turn = True
        else:
            game_start = False
            game.winner = None

    # display result
    if game.winner == game.user:
        lb_message.config(text="You won!", fg="#354259")
    elif game.winner == game.pc:
        lb_message.config(text="You lost!", fg="#354259")
    else:
        lb_message.config(text="Draw", fg="#354259")


# ui setup
window = Tk()
window.title('Tic Tac Toe')
window.configure(padx='70', pady='50', bg="#ECE5C7")
clicked_var = tkinter.IntVar()

grid_cells = [Label] * 9
mapping = dict()
for i, xy in enumerate(game.grid_xy):
    grid_cells[i] = Label(text="",
                          font=('Arial', 20, "normal"),
                          width=8, height=4,
                          fg="#354259",
                          bg="#C2DED1")
    grid_cells[i].bind('<Button-1>', func=lambda event, idx=i, cell=xy: click_cell(idx, cell))
    grid_cells[i].grid(row=xy[0], column=xy[1], padx=3, pady=3)
    mapping[xy] = i

lb_message = Label(text="", font=('Arial', 14, "normal"), bg="#ECE5C7", fg="#666", pady=15)
lb_message.grid(row=4, column=0, columnspan=3)
btn_start = Button(text="Start a new game", font=('Trebuchet', 16, "normal"),
                   padx=2, pady=5, border=0, highlightthickness=0, fg="#354259",
                   command=reset_game)
btn_start.grid(row=5, column=0, columnspan=3)

window.mainloop()
