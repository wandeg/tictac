'__author__' = 'jamesmaringa'


def initialize_board():
	return [[None for x in range(3)] for y in range(3)]

def board_is_full(board):
	return all([all(row) for row in board])

def cell_is_empty(board,row,col):
	return board[row][col] is not None

def row_is_full(row):
	return all(board[row])

def column_is_full(column):
	return all([row[column] for row in board])


def main():
	pass


if __name__ == '__main__':
	main()