import os
import time

from readchar import readkey, key
from board import Board
from snake import Snake


def the_game(size):
    board = Board(size)
    snake = Snake(board=board)
    board.print()
    
    k = readkey()
    while k != 'o':
        if k == 'w' or k == key.UP: # up
            snake.change_direction(1)
        if k == 'a' or k == key.LEFT: # left
            snake.change_direction(0)
        if k == 's' or k == key.DOWN: # down
            snake.change_direction(3)
        if k == 'd' or k == key.RIGHT: # right
            snake.change_direction(2)
        
        snake.move()
        os.system('clear')
        board.print()
        print(snake.my_coords[0])
        k = readkey()
        
if __name__ == "__main__":
    the_game(9)
