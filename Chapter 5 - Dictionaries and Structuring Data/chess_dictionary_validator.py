# A program that checks whether a given chess board (given as a dictionary) is valid


def is_valid_chess_board(board):
    validSpaceLocations = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
    wPlayerPieces, bPlayerPieces = {}, {}
    wPlayerPiecesCount, bPlayerPiecesCount = 0, 0

    for key, value in board.items():
        # Check if the piece in a valid space
        if not (1 <= int(key[0]) <= 8 and key[1].lower() in validSpaceLocations):
            return False

        # Assign the pieces to the correct player dictionary, and increment the piece count
        if value[0].lower() == 'w':
            wPlayerPieces.setdefault(value, 0)
            wPlayerPieces[value] += 1
            wPlayerPiecesCount += 1
        elif value[0].lower() == 'b':
            bPlayerPieces.setdefault(value, 0)
            bPlayerPieces[value] += 1
            bPlayerPiecesCount += 1

    # Check if either piece count for either player exceeds the maximum
    if wPlayerPiecesCount > 16 or bPlayerPiecesCount > 16:
        return False

    # Checks for number of kings and pawns allowed
    try:
        if wPlayerPieces['wking'] != 1 or bPlayerPieces['bking'] != 1:
            return False
        if wPlayerPieces['wpawn'] > 8 or bPlayerPieces['bpawn'] > 8:
            return False
    except KeyError:
        return True

    return True


if __name__ == '__main__':
    sampleBoard1 = {}
    sampleBoard2 = {'1h': 'bking', '6c': 'wqueen', '5h': 'bpawn',
                    '3e': 'wking', '4e': 'wpawn', '7e': 'bpawn'}

    print(is_valid_chess_board(sampleBoard1))
    print(is_valid_chess_board(sampleBoard2))
