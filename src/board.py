from random import choice

class Board:
    def __init__(self, size: int) -> None:
        self.size = size
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.food_coords = [None, None]
        self.new_food()
    
    def empty_elements(self) -> list:
        empties = []
        for k in range(self.size):
            for j in range(self.size):
                if self.board[k][j] == ' ':
                    empties.append([k, j])
                    
        return empties
    
    def new_food(self) -> None:
        # remove old food by replacing it with empty space
        if self.food_coords[0] is None or self.food_coords[1] is None:
            pass
        else:
            self.board[self.food_coords[0]][self.food_coords[1]] = ' '
        
        # create new food
        empties = self.empty_elements()
        self.food_coords = choice(empties)
        self.board[self.food_coords[0]][self.food_coords[1]] = 'x'
        
    def print(self) -> None:
        vertical = '+' + '—' * self.size + '+'
        
        print(vertical)
        for row in self.board:
            print('|', end='')
            for element in row:
                print(element, end='')
            print('|')
        print(vertical)