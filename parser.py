class Parser:

	def __init__(self):
		# eight registers
		self.registers = [0] * 8
		# an unbounded stack which holds individual 16-bit values
		self.stack = []
		# memory with 15-bit address space storing 16-bit values
		self.memory = []
		# Stores instruction bytes
		self.bytes = []
		# Offset to fetch instructions from bytes
		self.offset = 0
	
