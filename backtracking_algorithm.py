from check_input_constraint import retrieve_values_of_cells

class Backtracking:
	def __init__(self, ui_obj):
		self.ui_obj = ui_obj
		print(retrieve_values_of_cells(ui_obj))

