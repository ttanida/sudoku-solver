class Cell:
	"""Each of the 81 cells has a respective name, domain and list of other cells
	that the given cell has a constraint with"""
	def __init__(self, name, domain, list_constrained_cells):
		self.name = name
		self.domain = domain
		self.list_constrained_cells = list_constrained_cells

	def __repr__(self):
		# return f"{self.name}, domain: {self.domain}, list_other_cells: {self.list_constrained_cells}"
		return f"{self.name}, domain: {self.domain}"

