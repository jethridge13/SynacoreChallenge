class Parser:

	def __init__(self):
		self.registers = [0] * 8
		self.stack = []
		self.bytes = []
		self.offset = 0
	
