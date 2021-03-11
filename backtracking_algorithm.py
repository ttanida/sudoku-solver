from check_input_constraint import get_values_of_cells
from cell import Cell


def backtracking_algo(ui_obj):
	# create list of 81 variable/Cell objects
	list_variables = create_list_variable(ui_obj)

	# apply AC-3 as preprocessing step to reduce domains of 81 variables
	pre_processing_ac3(list_variables)


def create_list_variable(ui_obj):
	"""Creates a list containing all 81 cells objects

	If the value of a cell is empty (meaning value == 0), then the domain of the cell is full,
	meaning the cell can be assigned any value between 1 - 9

	If the value of the cell is already assigned by the user, then the domain of the cell is
	exactly the already assigned value.
	"""

	# get nested numpy array of all 81 cell values
	values_of_cells = get_values_of_cells(ui_obj)

	list_variables = []
	full_domain = list(range(1, 10))

	for row_index in range(1, 10):
		for column_index in range(1, 10):
			value_cell = values_of_cells[row_index-1, column_index-1]
			list_constrained_cells = get_cell_constraint(row_index, column_index)
			if value_cell == 0:
				list_variables.append(Cell(f"cell{row_index}{column_index}", full_domain.copy(), list_constrained_cells))
			else:
				list_variables.append(Cell(f"cell{row_index}{column_index}", [int(value_cell)], list_constrained_cells))

	return list_variables


def get_cell_constraint(row_index, column_index):
	"""Return a list of all the cells, whose value has to be different from the given cell's value

	I.e. cells in the same row, same column or same block.
	"""
	row_column_blocks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

	row_block = None
	column_block = None
	for block in row_column_blocks:
		if row_index in block:
			row_block = block
		if column_index in block:
			column_block = block

	set_constrained_cells = set()
	for row in range(1, 10):
		for column in range(1, 10):
			if (row_index == row or column_index == column) and \
					not (row_index == row and column_index == column):
				set_constrained_cells.add(f"cell{row}{column}")
			elif (row in row_block and column in column_block) and \
					not (row_index == row and column_index == column):
				set_constrained_cells.add(f"cell{row}{column}")

	return list(set_constrained_cells)


def pre_processing_ac3(list_variables):
	all_arcs = get_all_arcs(list_variables)

	while len(all_arcs) != 0:
		arc = all_arcs.pop()
		if remove_inconsistent_values(arc):
			add_neighbors(list_variables, all_arcs, arc)

	for var in list_variables:
		print(var)

def get_all_arcs(list_variables):
	"""Return a set of all arcs between cells that are constrained.

	E.g. there exist arcs (cell11, cell12) and (cell12, cell11), since they lie in the same row
	and are thus constrained.

	But there is no arc (cell11, cell78), since they don't have any common constraints.
	"""
	all_arcs = set()
	for variable_1 in list_variables:
		for variable_2 in list_variables:
			if variable_1 is not variable_2 and variable_2.name in variable_1.list_constrained_cells:
				all_arcs.add((variable_1, variable_2))

	return all_arcs


def remove_inconsistent_values(arc):
	"""Returns true iff succeeds"""
	removed = False

	domain_variable_1= arc[0].domain
	domain_variable_2= arc[1].domain
	if arc[1].name in arc[0].list_constrained_cells:
		for value in domain_variable_1:
			# if the only value in the domain of variable 2 is the given value, then the constraint of Var2 != Var2
			# cannot be fulfilled:
			if len(domain_variable_2) == 1 and value in domain_variable_2:
				arc[0].domain.remove(value)
				removed = True

	return removed


def add_neighbors(list_variables, all_arcs, arc):
	row_column_blocks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

	x_i = arc[0]
	row_block = None
	column_block = None
	row_index = int(x_i.name[4])
	column_index = int(x_i.name[5])
	for block in row_column_blocks:
		if row_index in block:
			row_block = block
		if column_index in block:
			column_block = block

	row_index_j = int(arc[1].name[4])
	column_index_j = int(arc[1].name[5])

	for row in range(1, 10):
		for column in range(1, 10):
			if (row == row_index or column == column_index) \
					and not (row == row_index and column == column_index) \
					and not (row == row_index_j and column == column_index_j):
				neighbor = list_variables[9 * (row-1) + (column-1)]
				all_arcs.add(tuple([neighbor, x_i]))
			elif (row in row_block and column in column_block) \
					and not (row == row_index and column == column_index) \
					and not (row == row_index_j and column == column_index_j):
				neighbor = list_variables[9 * (row-1) + (column-1)]
				all_arcs.add(tuple([neighbor, x_i]))


