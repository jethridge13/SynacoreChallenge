from parser import Parser
import sys

def parseIns(ins, parser):
	'''
	ins - The integer from the read-in bytes
	f - BufferedReader to read in more bytes if necessary
	i - offset - read from this offset in the byte memory

	Performs an action depending on the instruction
	
	Return -2: Runtime error in function
	Return -1: Function not yet implemented error
	Return 0: Halt execution and terminate program
	Return 1: Do nothing
	Return 2: Instruction done correctly
	'''
	# halt: 0
	# stop execution and terminate the program
	if ins == 0:
		return 0
	# set: 1 a b
	# set register <a> to the value of <b>
	elif ins == 1:
		parser.offset += 1
		a = getRegisterIndex(parser)
		parser.offset += 1
		b = getValueFromRegister(parser)
		parser.registers[a] = b
		return 2
	# push: 2 a
	# push <a> onto the stack
	elif ins == 2:
		parser.offset += 1
		a = getValueFromRegister(parser)
		parser.stack.append(a)
		return 2
	# pop: 3 a
	# remove the top element from the stack and write it into <a>; empty stack = error
	elif ins == 3:
		if len(parser.stack) <= 0:
			return -2
		parser.offset += 1
		a = getRegisterIndex(parser)
		parser.registers[a] = parser.stack.pop()
		return 2
	# eq: 4 a b c
	# set <a> to 1 if <b> is equal to <c>; set it to 0 otherwise
	elif ins == 4:
		parser.offset += 1
		a = getRegisterIndex(parser)
		parser.offset += 1
		b = getValueFromRegister(parser)
		parser.offset += 1
		c = getValueFromRegister(parser)
		if b == c:
			parser.registers[a] = 1
		else:
			parser.registers[a] = 0
		return 2
	# gt: 5 a b c
	# set <a> to 1 if <b> is greater than <c>; set it to 0 otherwise
	elif ins == 5:
		parser.offset += 1
		a = getRegisterIndex(parser)
		parser.offset += 1
		b = getValueFromRegister(parser)
		parser.offset += 1
		c = getValueFromRegister(parser)
		if b > c:
			parser.registers[a] = 1
		else:
			parser.registers[a] = 0
		return 2
	# jmp: 6 a
	# jump to <a>
	elif ins == 6:
		parser.offset += 1
		a = getValueFromRegister(parser)
		parser.offset = a - 1
		return 2
	# jt: 7 a b
	# if <a> is nonzero, jump to <b>
	elif ins == 7:
		parser.offset += 1
		a = getValueFromRegister(parser)
		parser.offset += 1
		b = getValueFromRegister(parser)
		if a != 0:
			parser.offset = b - 1
		return 2
	# jf: 8 a b
	# if <a> is zero, jump to <b>
	elif ins == 8:
		parser.offset += 1
		a = getValueFromRegister(parser)
		parser.offset += 1
		b = getValueFromRegister(parser)
		if a == 0:
			parser.offset = b - 1
		return 2
	# add: 9 a b c
	# assign into <a> the sum of <b> and <c> (modulo 32768)
	elif ins == 9:
		parser.offset += 1
		a = getRegisterIndex(parser)
		parser.offset += 1
		b = getValueFromRegister(parser)
		parser.offset += 1
		c = getValueFromRegister(parser)
		parser.registers[a] = (b + c) % 32768
		return 2
	# mult: 10 a b c
	# store into <a> the product of <b> and <c> (modulo 32768)
	elif ins == 10:
		parser.offset += 1
		a = getRegisterIndex(parser)
		parser.offset += 1
		b = getValueFromRegister(parser)
		parser.offset += 1
		c = getValueFromRegister(parser)
		parser.registers[a] = (b * c) % 32768
		return 2
	# mod: 11 a b c
	# store into <a> the remainder of <b> divided by <c>
	elif ins == 11:
		parser.offset += 1
		a = getRegisterIndex(parser)
		parser.offset += 1
		b = getValueFromRegister(parser)
		parser.offset += 1
		c = getValueFromRegister(parser)
		parser.registers[a] = b % c
		return 2
	# and: 12 a b c
	# stores into <a> the bitwise and of <b> and <c>
	elif ins == 12:
		parser.offset += 1
		a = getRegisterIndex(parser)
		parser.offset += 1
		b = getValueFromRegister(parser)
		parser.offset += 1
		c = getValueFromRegister(parser)
		parser.registers[a] = b & c
		return 2
	# or: 13 a b c
	# stores into <a> the bitwise or of <b> and <c>
	elif ins == 13:
		parser.offset += 1
		a = getRegisterIndex(parser)
		parser.offset += 1
		b = getValueFromRegister(parser)
		parser.offset += 1
		c = getValueFromRegister(parser)
		parser.registers[a] = b | c
		return 2
	# not: 14 a b
	# stores 15-bit bitwise inverse of <b> in <a>
	elif ins == 14:
		parser.offset += 1
		a = getRegisterIndex(parser)
		parser.offset += 1
		b = getValueFromRegister(parser)
		# Only first 15 bits
		b = ~ b
		b = b & 0x7fff
		parser.registers[a] = b
		return 2
	# rmem: 15 a b
	# read memory at address <b> and write it to <a>
	elif ins == 15:
		parser.offset += 1
		a = getRegisterIndex(parser)
		parser.offset += 1
		b = getValueFromRegister(parser)
		parser.registers[a] = parser.bytes[b]
		return 2
	# wmem: 16 a b
	# write the value from <b> into memory at address <a>
	elif ins == 16:
		parser.offset += 1
		a = getValueFromRegister(parser)
		parser.offset += 1
		b = getValueFromRegister(parser)
		parser.bytes[a] = b
		return 2
	# call: 17 a
	# write the address of the next instruction to the stack and jump to <a>
	elif ins == 17:
		parser.offset += 1
		a = getValueFromRegister(parser)
		parser.stack.append(parser.offset + 1)
		parser.offset = a - 1
		return 2
	# ret: 18
	# remove the top element from the stack and jump to it; empty stack = halt
	elif ins == 18:
		parser.offset = parser.stack.pop() - 1
		return 2
	# out: 19 a
	# write the character represented by ascii code <a> to the terminal
	elif ins == 19:
		parser.offset += 1
		a = getValueFromRegister(parser)
		c = chr(a)
		print(c, end='')
		return 2
	# in: 20 a
	# read a character from the terminal and write its ascii code to <a>;
	# it can be assumed that once input starts, it will continue until a 
	# newline is encountered; this means that you can safely read whole 
	# lines from the keyboard and trust that they will be fully read
	# TODO
	elif ins == 20:
		parser.offset += 1
		a = getRegisterIndex(parser)
		for i in range(0, 5):
			print(parser.bytes[parser.offset + i])
		return -1
	# noop: 21
	# no operation
	elif ins == 21:
		return 1
	else:
		return -1

def getValueFromRegister(parser):
	n = parser.bytes[parser.offset]
	if n > 32767:
		n -= 32768
		assert n >=0 and n <= 7
		n = parser.registers[n]
	return n

def getRegisterIndex(parser):
	n = parser.bytes[parser.offset]
	if n > 32767:
		n -= 32768
	assert n >=0 and n <= 7
	return n

def readloop(path, parser):
	i = 0
	with open(path, 'rb') as f:
		byte = int.from_bytes(f.read(2), byteorder='little')
		last = 0
		while last != f.tell():
			parser.bytes.append(byte)
			last = f.tell()
			byte = int.from_bytes(f.read(2), byteorder='little')

def executeLoop(parser):
	while parser.offset < len(parser.bytes):
		r = parseIns(parser.bytes[parser.offset], parser)
		if r < 0:
			print('ERROR')
			print('Exiting on instruction %s' % parser.bytes[parser.offset])
			sys.exit(1)
		if r == 0:
			sys.exit()
		parser.offset += 1
	print('End of instructions')

if __name__ == '__main__':
	p = Parser()
	readloop('challenge.bin', p)
	executeLoop(p)
