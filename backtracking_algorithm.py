from check_input_constraint import get_values_of_cells
from PyQt5 import QtWidgets
import time


def prepare(ui_obj):
	"""Prepares the data for the backtracking algorithm

	1. Converts ui_obj to nested numpy matrix values_of_cells to be passed into backtracking_algo
	2. Highlights user inputted cells in orange"""
	values_of_cells = get_values_of_cells(ui_obj)

	color_user_inputted_cells(values_of_cells, ui_obj)
	try:
		backtracking_algo(values_of_cells, ui_obj)
	except:
		print("finished!")


def color_user_inputted_cells(values_of_cells, ui_obj):
	for row in range(1, 10):
		for column in range(1, 10):
			if values_of_cells[row-1][column-1] != 0:
				eval(f'ui_obj.cell{row}{column}.setStyleSheet("background-color: rgb(255, 204, 153);")', {"ui_obj": ui_obj})


def backtracking_algo(values_of_cells, ui_obj):
	for row in range(1, 10):
		for column in range(1, 10):
			# if a cell is empty, its value is zero
			if values_of_cells[row-1][column-1] == 0:
				# we test which number from 1 - 9 is possible to place in the empty cell
				for number in range(1, 10):
					if possible(row, column, number, values_of_cells):
						# if it's possible to place the number there, we place it
						values_of_cells[row-1][column-1] = number

						# we also place it in the sudoku field GUI
						eval(f'ui_obj.cell{row}{column}.setText("{number}")', {"ui_obj": ui_obj})
						QtWidgets.qApp.processEvents()

						# since we now have 1 empty cell less than before, we can call backtracking_algo
						# recursively to fill out the rest of the empty cells
						backtracking_algo(values_of_cells, ui_obj)

						# if we backtrack (meaning the assigned number leads to a "dead end"), we have to
						# make the cell empty again by assigning zero
						values_of_cells[row - 1][column - 1] = 0

						# we also have to empty it in the sudoku field GUI
						eval(f'ui_obj.cell{row}{column}.setText("")', {"ui_obj": ui_obj})
						QtWidgets.qApp.processEvents()

				# if no number from 1 - 9 is possible to place in the empty cell, we have to backtrack
				return None

	# we raise an exception once we've found a solution (out of possibly many)
	# we know we have a solution, since we went through the nested for loops, which means that no cell is empty
	raise Exception("Solution to sudoku found! Breaking out of recursive loop!")

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

	return True
