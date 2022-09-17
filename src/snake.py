from board import Board


class Snake:
    def __init__(self, board: Board) -> None:
        self.board = board
        self.my_coords = [[self.board.size // 2 + 1, self.board.size // 2 + 1]]
        self.length = len(self.my_coords)
        self.directions = [(0,-1), (-1,0), (0,1), (1,0)]
        self.current_direction = 0
        self.add_snake_to_board()
        
    def move(self) -> None:
        y, x = self.directions[self.current_direction]
        for k in range(self.length-1, -1, -1):
            if k > 0:
                self.my_coords[k] = self.my_coords[k-1].copy()
            else:
                if self.my_coords[0][0] + y < 0 or self.my_coords[0][0] + y > self.board.size-1:
                    raise ValueError("Y error")
                if self.my_coords[0][1] + x < 0 or self.my_coords[0][1] + x > self.board.size-1:
                    raise ValueError("X error")
                
                self.my_coords[0][0] = self.my_coords[0][0] + y
                self.my_coords[0][1] = self.my_coords[0][1] + x
                
                # checking the collision
                if self.my_coords[0] in self.my_coords[1:(self.length-1)]:
                    raise ValueError('Dont eat yourself!')
                
                # eating the food
                if self.my_coords[0] == self.board.food_coords:
                    self.eat()
        
        # move snake on the board
        self.add_snake_to_board()
    
    def change_direction(self, direction: int) -> None:
        if direction >= 0 and direction < 4:
            self.current_direction = direction
    
    def eat(self):
        self.length += 1
        self.my_coords.append(self.my_coords[-1])
        self.board.new_food()
    
    def add_snake_to_board(self) -> None:
        # remove old snake
        for k in range(self.board.size):
            for j in range(self.board.size):
                if self.board.board[k][j] == 'o':
                    self.board.board[k][j] = ' '
        
        # add new snake
        for coord in self.my_coords:
            y, x = coord
            self.board.board[y][x] = 'o'
        