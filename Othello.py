# Author: Tommy Nguyen
# GitHub username: TommyTegra
# Date: 6/7/2023
# Description: This file contains a playable reversi, or othello,
#       board game on a 8x8 board, through calling methods within
#       the classes.


class Player:
    """
    Represents a player in the othello game. Will be called from
    the Othello class for player creation so that players are tied
    to the game being played.
    """
    def __init__(self, name, color):
        """
        Initializes a player object with the two given
        strings.
        """
        self._name = name
        # Color should be black or white
        self._color = color

    def get_name(self):
        """
        Returns the string value for the name data member.
        """
        return self._name

    def set_name(self, new_name):
        """
        Assigns a new string value for the name data member.
        """
        self._name = new_name

    def get_color(self):
        """
        Returns the string value for the color data member.
        """
        return self._color

    def set_color(self, new_color):
        """
        Assigns a new string value to the color data member.
        """
        self._color = new_color


class Othello:
    """
    Represents the board game othello/reversi which contains
    methods and information regarding both the player and the
    board, and its play functionalities. Will use the Player
    class to create a player thus, storing the player info
    along with the game.
    """
    def __init__(self):
        """
        Initializes the othello game to be played by initializing
        a list of player and the game board.
        """
        self._player_list = {}
        self._board = [
            ['*','*','*','*','*','*','*','*','*','*'],
            ['*','.','.','.','.','.','.','.','.','*'],
            ['*','.','.','.','.','.','.','.','.','*'],
            ['*','.','.','.','.','.','.','.','.','*'],
            ['*','.','.','.','O','X','.','.','.','*'],
            ['*','.','.','.','X','O','.','.','.','*'],
            ['*','.','.','.','.','.','.','.','.','*'],
            ['*','.','.','.','.','.','.','.','.','*'],
            ['*','.','.','.','.','.','.','.','.','*'],
            ['*','*','*','*','*','*','*','*','*','*']
        ]

    def print_board(self):
        """
        Returns the current state of the board including the boundaries,
        without commas and in a board format, not as a list.
        """
        for row in self._board:
            # Space for nicer alignment during printing
            print(' '.join(row))

    def get_player_list(self):
        """
        This method is solely for testing purposes.
        Returns the player list dictionary.
        """
        return self._player_list

    def create_player(self, player_name, player_color):
        """
        Contains two string parameters and uses the Player class to
        create a Player object which contains a player's name and
        color for the othello game. The object is then added to the
        player list dictionary in the Othello class with the player's
        name as the key.
        """
        player_obj = Player(player_name, player_color)
        self._player_list[player_obj.get_name()] = player_obj

    def return_winner(self):
        """
        Returns a string which states which player has won the game
        based on the number of color pieces on the game board. Will
        take in consideration of a tie as well.
        """
        # Initializes method local variables
        black_counter = 0
        white_counter = 0
        black_player = None
        white_player = None

        # Checks throughout the board for pieces based on color
        for row in self._board:
            for item in row:
                if item == "X":
                    black_counter += 1
                elif item == "O":
                    white_counter += 1

        # Get player's names
        for player in self._player_list:
            if self._player_list[player].get_color() == 'black':
                black_player = self._player_list[player].get_name()

        for player in self._player_list:
            if self._player_list[player].get_color() == 'white':
                white_player = self._player_list[player].get_name()

        # Evaluates the number of pieces
        if black_counter > white_counter:
            return "Winner is black player: " + black_player
        elif white_counter > black_counter:
            return "Winner is white player: " + white_player
        else:
            return "It's a tie"

    def position_validity(self, opp_color, row_index, col_index, row_direction, col_direction):
        """
        An additional function to assist return_available_positions
        method by checking if there is a valid position from a
        given direction of a given position, with the given opponent's
        color. Returns the valid position, if any.
        """
        # Determines if the initial condition of an opposite color piece is adjacent
        if self._board[row_index + row_direction][col_index + col_direction] == opp_color:
            if row_direction > 0:
                row_direction += 1
            elif row_direction < 0:
                row_direction -= 1
            if col_direction > 0:
                col_direction += 1
            elif col_direction < 0:
                col_direction -= 1
            cont = True
            while cont:
                # Continues in the direction
                if self._board[row_index + row_direction][col_index + col_direction] == opp_color:
                    if row_direction > 0:
                        row_direction += 1
                    elif row_direction < 0:
                        row_direction -= 1
                    if col_direction > 0:
                        col_direction += 1
                    elif col_direction < 0:
                        col_direction -= 1
                # The end condition of an open spot being satisfied for a valid position
                elif self._board[row_index + row_direction][col_index + col_direction] == '.':
                    position = (row_index + row_direction, col_index + col_direction)
                    return position
                else:
                    cont = False
            return None
        return None

    def return_available_positions(self, color):
        """
        Has a string parameter for the color piece, and returns a
        list of possible moves/positions based on the current board.
        """
        # Initial variables set up
        valid_list = []
        player_piece = None
        opponent_piece = None
        if color == 'black':
            player_piece = 'X'
            opponent_piece = 'O'
        elif color == 'white':
            player_piece = 'O'
            opponent_piece = 'X'

        # Looks for a piece of the given color
        for row in range(0, len(self._board)):
            for column in range(0, len(self._board[row])):
                if self._board[row][column] == player_piece:

                    # Adjacent positions above
                    row_change = -1
                    col_change = -1
                    if self.position_validity(opponent_piece, row, column, row_change, col_change) is not None:
                        valid_list.append(self.position_validity(opponent_piece, row, column, row_change, col_change))

                    row_change = -1
                    col_change = 0
                    if self.position_validity(opponent_piece, row, column, row_change, col_change) is not None:
                        valid_list.append(self.position_validity(opponent_piece, row, column, row_change, col_change))

                    row_change = -1
                    col_change = 1
                    if self.position_validity(opponent_piece, row, column, row_change, col_change) is not None:
                        valid_list.append(self.position_validity(opponent_piece, row, column, row_change, col_change))

                    # Adjacent positions in-line
                    row_change = 0
                    col_change = -1
                    if self.position_validity(opponent_piece, row, column, row_change, col_change) is not None:
                        valid_list.append(self.position_validity(opponent_piece, row, column, row_change, col_change))

                    row_change = 0
                    col_change = 1
                    if self.position_validity(opponent_piece, row, column, row_change, col_change) is not None:
                        valid_list.append(self.position_validity(opponent_piece, row, column, row_change, col_change))

                    # Adjacent positions below
                    row_change = 1
                    col_change = -1
                    if self.position_validity(opponent_piece, row, column, row_change, col_change) is not None:
                        valid_list.append(self.position_validity(opponent_piece, row, column, row_change, col_change))

                    row_change = 1
                    col_change = 0
                    if self.position_validity(opponent_piece, row, column, row_change, col_change) is not None:
                        valid_list.append(self.position_validity(opponent_piece, row, column, row_change, col_change))

                    row_change = 1
                    col_change = 1
                    if self.position_validity(opponent_piece, row, column, row_change, col_change) is not None:
                        valid_list.append(self.position_validity(opponent_piece, row, column, row_change, col_change))

        # Sorts and removes duplicates in the list
        no_dupe_set = set(valid_list)
        no_dupe_list = list(no_dupe_set)
        no_dupe_list.sort()
        return no_dupe_list

    def make_move(self, color, piece_position):
        """
        Has two parameters which identifies the color and the position
        to place said piece on the board. It will update the board along
        with returning the board after the move is done. This method will
        be called within the play_game method.
        """
        # Initial variables set up
        change_piece_list = []
        color_piece = None
        opposite_piece = None
        if color == 'black':
            color_piece = 'X'
            opposite_piece = 'O'
        elif color == 'white':
            color_piece = 'O'
            opposite_piece = 'X'
        # Tuple unpacking
        row, col = piece_position

        # Determines if the path contains valid pieces to be flipped, adds to list if so
        # Paths above the position
        row_diff = -1
        col_diff = -1
        if self._board[row + row_diff][col + col_diff] == opposite_piece:
            temp_list = [(row + row_diff, col + col_diff)]
            row_diff -= 1
            col_diff -= 1
            cont = True
            while cont:
                if self._board[row + row_diff][col + col_diff] == opposite_piece:
                    temp_list.append((row + row_diff, col + col_diff))
                    row_diff -= 1
                    col_diff -= 1
                elif self._board[row + row_diff][col + col_diff] == color_piece:
                    change_piece_list.extend(temp_list)
                    cont = False
                else:
                    cont = False

        row_diff = -1
        col_diff = 0
        if self._board[row + row_diff][col + col_diff] == opposite_piece:
            temp_list = [(row + row_diff, col + col_diff)]
            row_diff -= 1
            cont = True
            while cont:
                if self._board[row + row_diff][col + col_diff] == opposite_piece:
                    temp_list.append((row + row_diff, col + col_diff))
                    row_diff -= 1
                elif self._board[row + row_diff][col + col_diff] == color_piece:
                    change_piece_list.extend(temp_list)
                    cont = False
                else:
                    cont = False

        row_diff = -1
        col_diff = 1
        if self._board[row + row_diff][col + col_diff] == opposite_piece:
            temp_list = [(row + row_diff, col + col_diff)]
            row_diff -= 1
            col_diff += 1
            cont = True
            while cont:
                if self._board[row + row_diff][col + col_diff] == opposite_piece:
                    temp_list.append((row + row_diff, col + col_diff))
                    row_diff -= 1
                    col_diff += 1
                elif self._board[row + row_diff][col + col_diff] == color_piece:
                    change_piece_list.extend(temp_list)
                    cont = False
                else:
                    cont = False

        # Paths in-line
        row_diff = 0
        col_diff = -1
        if self._board[row + row_diff][col + col_diff] == opposite_piece:
            temp_list = [(row + row_diff, col + col_diff)]
            col_diff -= 1
            cont = True
            while cont:
                if self._board[row + row_diff][col + col_diff] == opposite_piece:
                    temp_list.append((row + row_diff, col + col_diff))
                    col_diff -= 1
                elif self._board[row + row_diff][col + col_diff] == color_piece:
                    change_piece_list.extend(temp_list)
                    cont = False
                else:
                    cont = False

        row_diff = 0
        col_diff = 1
        if self._board[row + row_diff][col + col_diff] == opposite_piece:
            temp_list = [(row + row_diff, col + col_diff)]
            col_diff += 1
            cont = True
            while cont:
                if self._board[row + row_diff][col + col_diff] == opposite_piece:
                    temp_list.append((row + row_diff, col + col_diff))
                    col_diff += 1
                elif self._board[row + row_diff][col + col_diff] == color_piece:
                    change_piece_list.extend(temp_list)
                    cont = False
                else:
                    cont = False

        # Paths below
        row_diff = 1
        col_diff = -1
        if self._board[row + row_diff][col + col_diff] == opposite_piece:
            temp_list = [(row + row_diff, col + col_diff)]
            row_diff += 1
            col_diff -= 1
            cont = True
            while cont:
                if self._board[row + row_diff][col + col_diff] == opposite_piece:
                    temp_list.append((row + row_diff, col + col_diff))
                    row_diff += 1
                    col_diff -= 1
                elif self._board[row + row_diff][col + col_diff] == color_piece:
                    change_piece_list.extend(temp_list)
                    cont = False
                else:
                    cont = False

        row_diff = 1
        col_diff = 0
        if self._board[row + row_diff][col + col_diff] == opposite_piece:
            temp_list = [(row + row_diff, col + col_diff)]
            row_diff += 1
            cont = True
            while cont:
                if self._board[row + row_diff][col + col_diff] == opposite_piece:
                    temp_list.append((row + row_diff, col + col_diff))
                    row_diff += 1
                elif self._board[row + row_diff][col + col_diff] == color_piece:
                    change_piece_list.extend(temp_list)
                    cont = False
                else:
                    cont = False

        row_diff = 1
        col_diff = 1
        if self._board[row + row_diff][col + col_diff] == opposite_piece:
            temp_list = [(row + row_diff, col + col_diff)]
            row_diff += 1
            col_diff += 1
            cont = True
            while cont:
                if self._board[row + row_diff][col + col_diff] == opposite_piece:
                    temp_list.append((row + row_diff, col + col_diff))
                    row_diff += 1
                    col_diff += 1
                elif self._board[row + row_diff][col + col_diff] == color_piece:
                    change_piece_list.extend(temp_list)
                    cont = False
                else:
                    cont = False

        # Adds initial position
        change_piece_list.append((row, col))

        # Flips all pieces in the list that were validated
        for position in change_piece_list:
            row_index, col_index = position
            self._board[row_index][col_index] = color_piece

        return self._board

    def play_game(self, color, piece_position):
        """
        Will call make_move method to try to move pieces for the player
        to the given position with the specified color. Will check if
        the move is valid, if so, complete the move, if not, print a
        string stating so and provide a list of valid moves, also,
        considering the case of no valid moves. Will also have a case
        for end game and call return_winner method if so.
        """
        # Determines if the move is valid
        if piece_position not in self.return_available_positions(color):
            print(f"Here are the valid moves: {self.return_available_positions(color)}")
            return "Invalid move"
        else:
            self.make_move(color, piece_position)

        # Determines if there are any valid moves left for both players
        opposite_color = None
        if color == 'black':
            opposite_color = 'white'
        elif color == 'white':
            opposite_color = 'black'
        # End game when both players have no valid moves left
        if (
                len(self.return_available_positions(color)) == 0 and
                len(self.return_available_positions(opposite_color)) == 0
        ):
            # Initializes method local variables
            black_pieces = 0
            white_pieces = 0

            # Checks throughout the board for pieces based on color
            for row in self._board:
                for item in row:
                    if item == "X":
                        black_pieces += 1
                    elif item == "O":
                        white_pieces += 1
            print(f"Game is ended white piece: {white_pieces} black piece: {black_pieces}")
            return self.return_winner()





# Test code below:
# game = Othello()
# game.print_board()
# game.create_player("Helen", "white")
# game.create_player("Leo", "black")
# print(game.get_player_list())
# print(game.return_winner())
# print(game.return_available_positions('black'))
# print(game.make_move('black', (4,3)))
# game.print_board()
# print(game.return_available_positions('white'))
# game.make_move('white', (3,3))
# game.print_board()
# print(game.return_available_positions('black'))
# game.make_move('black', (3,4))
# game.print_board()
# print(game.return_available_positions('white'))
# game.make_move('white', (3,5))
# game.print_board()
# print(game.return_available_positions('black'))

# game = Othello()
# game.create_player("Helen", "white")
# game.create_player("Leo", "black")
# game.make_move("black", (5,6))
# game.print_board()
# game.play_game("white", (7,6))
# game.print_board()

# game = Othello()
# game.print_board()
# game.create_player("Helen", "white")
# game.create_player("Leo", "black")
# game.play_game("black", (3,2))
# game.print_board()
# game.play_game("white", (6,6))
# game.print_board()
