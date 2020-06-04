# A program that checks whether a given chess board (given as a dictionary) is valid


def is_valid_chess_board(board):
    valid_space_locations = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
    w_player_pieces, b_player_pieces = {}, {}
    w_player_pieces_count, b_player_pieces_count = 0, 0

    for key, value in board.items():
        # Check if the piece in a valid space
        if not (1 <= int(key[0]) <= 8 and key[1].lower() in valid_space_locations):
            return False

        # Assign the pieces to the correct player dictionary, and increment the piece count
        if value[0].lower() == 'w':
            w_player_pieces.setdefault(value, 0)
            w_player_pieces[value] += 1
            w_player_pieces_count += 1
        elif value[0].lower() == 'b':
            b_player_pieces.setdefault(value, 0)
            b_player_pieces[value] += 1
            b_player_pieces_count += 1

    # Check if either piece count for either player exceeds the maximum
    if w_player_pieces_count > 16 or b_player_pieces_count > 16:
        return False

    # Checks for number of kings and pawns allowed
    try:
        if w_player_pieces['wking'] != 1 or b_player_pieces['bking'] != 1:
            return False
        if w_player_pieces['wpawn'] > 8 or b_player_pieces['bpawn'] > 8:
            return False
    except KeyError:
        return True

    return True


if __name__ == '__main__':
    sample_Board_1 = {}
    sample_Board_2 = {'1h': 'bking', '6c': 'wqueen', '5h': 'bpawn', '3e': 'wking', '4e': 'wpawn', '7e': 'bpawn'}

    print(is_valid_chess_board(sample_Board_1))
    print(is_valid_chess_board(sample_Board_2))
