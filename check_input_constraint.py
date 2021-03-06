import numpy as np


def check_input_constraints(ui_obj):
	"""Checks if initial user input satisfies the sudoku constraints (e.g. no duplicate number in same row)

	Any time a cell value is modified, check_input_constraints calls method retrieve_values_of_cells to retrieve
	all 81 cells values and store them in a 9x9 numpy array values_of_cells.

	Check_input_constraints then passes values_of_cells and values_of_cells transposed into methods
	check_constraints_rows_columns and check_constraints_blocks to check if the row/column/block constraints
	are not violated.

	If a constraint is violated, the respective row/column/block and the two cells that violated the constraint are
	highlighted in red by methods change_row_color/change_column_color/change_block_color and all inputs are disabled
	except for the two cells that violated the constraint.

	If the conflict is resolved, method enable_input enables all input again.
	"""

	# retrieve nested numpy array of all 81 cell values
	values_of_cells = retrieve_values_of_cells(ui_obj)

	# check for duplicates in rows
	check_rows = check_constraints_rows_columns(values_of_cells)

	# change row color and disable all input (except for duplicates) if there is a row duplicate
	change_row_color(check_rows, ui_obj)
	disable_input_rows(check_rows, ui_obj)

	# check for duplicates in columns (values_of_cells passed as transpose)
	check_columns = check_constraints_rows_columns(values_of_cells.T)

	# change column color and disable all input (except for duplicates) if there is a column duplicate
	change_column_color(check_columns, ui_obj)
	disable_input_columns(check_columns, ui_obj)

	# check for duplicates in blocks
	check_blocks = check_constraints_blocks(values_of_cells)

	# change block color and disable all input (except for duplicates) if there is a block duplicate
	change_block_color(check_blocks, ui_obj)
	disable_input_blocks(check_blocks, ui_obj)

	# enable all input if there are neither row nor column nor block duplicates and change color back to white
	if check_rows is None and check_columns is None and check_blocks is None:
		enable_input(ui_obj)


def retrieve_values_of_cells(ui_obj):
	"""Retrieves all 81 cell values of sudoku grid as a nested numpy array

	If a cell is empty, its value is 0."""
	values_of_cells = np.zeros([9, 9])
	for row in range(1, 10):
		for column in range(1, 10):
			value_of_cell = eval(f'ui_obj.cell{row}{column}.text()', {"ui_obj": ui_obj})
			if value_of_cell != "":
				values_of_cells[row - 1, column - 1] = int(value_of_cell)

	return values_of_cells


def check_constraints_rows_columns(values_of_cells):
	"""Checks if user input (matrix values_of_cells) satisfies the row/column sudoku constraints
	(i.e. no duplicate number in same row/column)

	If matrix values_of_cells is passed as input without modification, the method checks for the row constraints.
	If transposed matrix values_of_cells is passed as input, the method checks for the column constraints.

	Method goes row-by-row (or column-by-column if transposed matrix passed as argument) and stores cell values != 0
	in dictionary "found_values" with the values as keys and the respective column (or row) as values.

	If there is a duplicate value in a row, it returns a tuple of (row, column1, column2), where column1 is the
	column of the 1st duplicate value and column2 is the column of the 2nd duplicate value.

	Similarly, if transposed matrix is passed as argument and there is a duplicate value in a column, it returns
	a tuple of (column, row1, row2), where row1 is the row of the 1st duplicate value and row2 is the row of the
	2nd duplicate value.

	If there are no duplicate values, method return None.
	"""
	for row in range(1, 10):
		found_values = {}
		for column in range(1, 10):
			value_of_cell = values_of_cells[row - 1, column - 1]
			if value_of_cell != 0:
				if value_of_cell not in found_values.keys():
					found_values[value_of_cell] = column
				else:
					return row, found_values[value_of_cell], column

	return None


def check_constraints_blocks(values_of_cells):
	"""Checks if user input (matrix values_of_cells) satisfies the block sudoku constraints
	(i.e. no duplicate number in same block)

	There a 9 blocks in total, which are checked one-by-one using the first two for loops.

	Cell values != 0 are stored as keys in the dictionary "found_values" with their respective row_index and
	column_index stored as values.

	If the same cell value is found twice in a block, the method return a tuple consisting of the indices of the
	rows and columns of the respective block (stored in row_blocks and column_blocks) and the specific row/column
	indices of the cells whose value appears twice.

	If there are no constraint violation, the method returns None.
	"""
	row_blocks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	column_blocks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

	for row_block in row_blocks:
		for column_block in column_blocks:
			found_values = {}
			for row_index in row_block:
				for column_index in column_block:
					value_of_cell = values_of_cells[row_index - 1, column_index - 1]
					if value_of_cell != 0:
						if value_of_cell not in found_values.keys():
							found_values[value_of_cell] = row_index, column_index
						else:
							return row_block, column_block, found_values[value_of_cell], (row_index, column_index)

	return None


def change_row_color(check_rows, ui_obj):
	"""Changes the color of the row whose cells violated the constraint to light red and the color of the two cells
	that specifically violated the constraint to dark red."""
	if check_rows is not None:
		for column in range(1, 10):
			eval(f'ui_obj.cell{check_rows[0]}{column}.setStyleSheet("background-color: rgb(255, 128, 128);")', {"ui_obj": ui_obj})

		eval(f'ui_obj.cell{check_rows[0]}{check_rows[1]}.setStyleSheet("background-color: rgb(230, 0, 0);")', {"ui_obj": ui_obj})
		eval(f'ui_obj.cell{check_rows[0]}{check_rows[2]}.setStyleSheet("background-color: rgb(230, 0, 0);")', {"ui_obj": ui_obj})


def change_column_color(check_columns, ui_obj):
	"""Changes the color of the column whose cells violated the constraint to light red and the color of the two
	cells that specifically violated the constraint to dark red."""
	if check_columns is not None:
		for row in range(1, 10):
			eval(f'ui_obj.cell{row}{check_columns[0]}.setStyleSheet("background-color: rgb(255, 128, 128);")', {"ui_obj": ui_obj})

		eval(f'ui_obj.cell{check_columns[1]}{check_columns[0]}.setStyleSheet("background-color: rgb(230, 0, 0);")', {"ui_obj": ui_obj})
		eval(f'ui_obj.cell{check_columns[2]}{check_columns[0]}.setStyleSheet("background-color: rgb(230, 0, 0);")', {"ui_obj": ui_obj})


def change_block_color(check_blocks, ui_obj):
	"""Changes the color of the block whose cells violated the constraint to light red and the color of the two
	cells that specifically violated the constraint to dark red."""
	if check_blocks is not None:

		# row_block and column_block are the respective rows and columns (i.e. block) where constraint was violated
		row_block = check_blocks[0]
		column_block = check_blocks[1]

		# row_index_1, column_index_1, row_index_2, column_index_2 are the row/column indices of two cells that
		# violated the constraint
		row_index_1 = check_blocks[2][0]
		column_index_1 = check_blocks[2][1]
		row_index_2 = check_blocks[3][0]
		column_index_2 = check_blocks[3][1]

		for row_index in row_block:
			for column_index in column_block:
				eval(f'ui_obj.cell{row_index}{column_index}.setStyleSheet("background-color: rgb(255, 128, 128);")', {"ui_obj": ui_obj})

		eval(f'ui_obj.cell{row_index_1}{column_index_1}.setStyleSheet("background-color: rgb(230, 0, 0);")', {"ui_obj": ui_obj})
		eval(f'ui_obj.cell{row_index_2}{column_index_2}.setStyleSheet("background-color: rgb(230, 0, 0);")', {"ui_obj": ui_obj})


def disable_input_rows(check_rows, ui_obj):
	"""Disables all input except for the cells that violated constraints

	Also sets tool tip to 'Please resolve conflict' for all cells to advise user of conflict."""
	if check_rows is not None:
		for row in range(1, 10):
			for column in range(1, 10):
				eval(f'ui_obj.cell{row}{column}.setToolTip("Please resolve the conflict!")', {"ui_obj": ui_obj})
				eval(f'ui_obj.cell{row}{column}.setToolTipDuration(10000)', {"ui_obj": ui_obj})
				if row == check_rows[0] and (column == check_rows[1] or column == check_rows[2]):
					continue
				eval(f'ui_obj.cell{row}{column}.setDisabled(True)', {"ui_obj": ui_obj})

		ui_obj.solve_button.setDisabled(True)


def disable_input_columns(check_columns, ui_obj):
	"""Disables all input except for the cells that violated constraints

	Also sets tool tip to 'Please resolve conflict' for all cells to advise user of conflict."""
	if check_columns is not None:
		for column in range(1, 10):
			for row in range(1, 10):
				eval(f'ui_obj.cell{row}{column}.setToolTip("Please resolve the conflict!")', {"ui_obj": ui_obj})
				eval(f'ui_obj.cell{row}{column}.setToolTipDuration(10000)', {"ui_obj": ui_obj})
				if column == check_columns[0] and (row == check_columns[1] or row == check_columns[2]):
					continue
				eval(f'ui_obj.cell{row}{column}.setDisabled(True)', {"ui_obj": ui_obj})

		ui_obj.solve_button.setDisabled(True)


def disable_input_blocks(check_blocks, ui_obj):
	"""Disables all input except for the cells that violated constraints

	Also sets tool tip to 'Please resolve conflict' for all cells to advise user of conflict."""
	if check_blocks is not None:
		# row_index_1, column_index_1, row_index_2, column_index_2 are the row/column indices of two cells that
		# violated the constraint
		row_index_1 = check_blocks[2][0]
		column_index_1 = check_blocks[2][1]
		row_index_2 = check_blocks[3][0]
		column_index_2 = check_blocks[3][1]

		for row in range(1, 10):
			for column in range(1, 10):
				eval(f'ui_obj.cell{row}{column}.setToolTip("Please resolve the conflict!")', {"ui_obj": ui_obj})
				eval(f'ui_obj.cell{row}{column}.setToolTipDuration(10000)', {"ui_obj": ui_obj})
				if (row == row_index_1 and column == column_index_1) or (
						row == row_index_2 and column == column_index_2):
					continue
				eval(f'ui_obj.cell{row}{column}.setDisabled(True)', {"ui_obj": ui_obj})

		ui_obj.solve_button.setDisabled(True)


def enable_input(ui_obj):
	"Enables all input"
	for row in range(1, 10):
		for column in range(1, 10):
			eval(f'ui_obj.cell{row}{column}.setEnabled(True)', {"ui_obj": ui_obj})
			eval(f'ui_obj.cell{row}{column}.setStyleSheet("background-color: rgb(255, 255, 255);")', {"ui_obj": ui_obj})

	ui_obj.solve_button.setEnabled(True)


