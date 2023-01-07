class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #use a single list to rep 3x3 board
        self.current_winner = None #keep track of winner 
    
    def print_board(self):
        #getting the rows
        for row in [self.board[i*3:(i*1)*3] for i in range(3)]:
            print(' | ' + ' | '.join(row) + ' | ')
    
    @staticmethod
    def print_board_nums():

        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(' | ' + ' | '.join(row) + ' | ')
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ' ] #list comprehension 
        #moves = []
        #for (i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
         #   if spot == ' ':
         #       moves.append(i)
        #return moves 

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
        #return(len(self.available_moves()))
    
    def make_move(self, square, letter):
        #if valid move, then make the move (assign square to letter)
        #then return true. if invalid, return false 
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        #winner if 3 in a row anywhere / check all of these
        #check the row
        row_ind = square // 3
        row = self.board [row_ind*3 : (row_ind +1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        #check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True 

def play(game, x_player, o_player, print_game=True):
    #returns the winner of game / none if tie
    if print_game:
        game.print_board_nums()
    
    letter = 'x' #starting letter 

    while game.empty_squares():
        #get the move from the appropriate player
        if letter == '0':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        #define function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('') #empty line
            
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter
            
            letter = 'o' if letter == 'x' else 'x' #switches player
        
        if print_game:
            print('It\'s a tie')
