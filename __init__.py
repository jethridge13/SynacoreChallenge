from parser import Parser as parser
import sys

def parseIns(ins, f):
	'''
	ins - The integer from the read-in bytes
	f - BufferedReader to read in more bytes if necessary

	Performs an action depending on the instruction
	'''
	# halt: 0
	# stop execution and terminate the program
	if ins == 0:
		return 0
	# set: 1 a b
	# set register <a> to the value of <b>
	# TODO
	elif ins == 1:
		return -1
	# push: 2 a
	# push <a> onto the stack
	# TODO
	elif ins == 2:
		return -1
	# pop: 3 a
	# remove the top element from the stack and write it into <a>; empty stack = error
	# TODO
	elif ins == 3:
		return -1
	# eq: 4 a b c
	# set <a> to 1 if <b> is equal to <c>; set it to 0 otherwise
	# TODO
	elif ins == 4:
		return -1
	# gt: 5 a b c
	# set <a> to 1 if <b> is greater than <c>; set it to 0 otherwise
	# TODO
	elif ins == 5:
		return -1
	# jmp: 6 a
	# jump to <a>
	# TODO
	elif ins == 6:
		return -1
	# jt: 7 a b
	# if <a> is nonzero, jump to <b>
	# TODO
	elif ins == 7:
		return -1
	# jf: 8 a b
	# if <a> is zero, jump to <b>
	# TODO
	elif ins == 8:
		return -1
	# add: 9 a b c
	# assign into <a> the sum of <b> and <c> (modulo 32768)
	# TODO
	elif ins == 9:
		return -1
	# mult: 10 a b c
	# store into <a> the product of <b> and <c> (modulo 32768)
	# TODO
	elif ins == 10:
		return -1
	# mod: 11 a b c
	# store into <a> the remainder of <b> divided by <c>
	# TODO
	elif ins == 11:
		return -1
	# and: 12 a b c
	# stores into <a> the bitwise and of <b> and <c>
	# TODO
	elif ins == 12:
		return -1
	# or: 13 a b c
	# stores into <a> the bitwise or of <b> and <c>
	# TODO
	elif ins == 13:
		return -1
	# not: 14 a b
	# stores 15-bit bitwise inverse of <b> in <a>
	# TODO
	elif ins == 14:
		return -1
	# rmem: 15 a b
	# read memory at address <b> and write it to <a>
	# TODO
	elif ins == 15:
		return -1
	# wmem: 16 a b
	# write the value from <b> into memory at address <a>
	# TODO
	elif ins == 16:
		return -1
	# call: 17 a
	# write the address of the next instruction to the stack and jump to <a>
	# TODO
	elif ins == 17:
		return -1
	# ret: 18
	# remove the top element from the stack and jump to it; empty stack = halt
	# TODO
	elif ins == 18:
		return -1
	# out: 19 a
	# write the character represented by ascii code <a> to the terminal
	# TODO
	elif ins == 19:
		c = chr(int.from_bytes(f.read(2), byteorder='little'))
		print(c, end='')
		return 2
	# in: 20 a
	# read a character from the terminal and write its ascii code to <a>; it can be assumed that once input starts, it will continue until a newline is encountered; this means that you can safely read whole lines from the keyboard and trust that they will be fully read
	# TODO
	elif ins == 20:
		return -1
	# noop: 21
	# no operation
	elif ins == 21:
		return 1
	else:
		return -1

def readloop(path):
	with open(path, 'rb') as f:
		byte = int.from_bytes(f.read(2), byteorder='little')
		while byte:
			# TODO Do stuff
			r = parseIns(byte, f)
			if r < 0:
				print('ERROR')
				print('Exiting on instruction %s' % byte)
				sys.exit(1)
			if r == 0:
				sys.exit()
			byte = int.from_bytes(f.read(2), byteorder='little')

if __name__ == '__main__':
	readloop('challenge.bin')
