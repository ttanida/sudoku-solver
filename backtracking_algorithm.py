from check_input_constraint import get_values_of_cells


def backtracking_algo(ui_obj):
	# create list of 81 variable/Cell objects

def possible(row_index, column_index, number, values_of_cells):
	"""Checks if it's possible to place the number in the specified
	row_index and column_index in the numpy matrix values_of_cells"""

	# check for number in the same row
	for i in range(1, 10):
		if values_of_cells[row_index-1][i-1] == number:
			return False

	# check for number in the same column
		for i in range(1, 10):
			if values_of_cells[i-1][column_index-1] == number:
				return False

	# check for number in the same block

	# block_index_row and block_index_column are the indices of the upper left most cell
	# of the block in which row_index and column_index are located
	block_index_row = ((row_index-1) // 3) * 3
	block_index_column = ((column_index - 1) // 3) * 3

	for i in range(0, 3):
		for j in range(0, 3):
			if values_of_cells[block_index_row+i][block_index_column+j] == number:
				return False
