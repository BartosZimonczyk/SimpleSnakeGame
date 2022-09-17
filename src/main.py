from board import Board
from snake import Snake


if __name__ == "__main__":
    board = Board(5)
    snake = Snake(board=board)
    board.print()
    snake.move()
    board.print()