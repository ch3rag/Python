
grammar = {'<start>' : [['This', '<object>', 'is here.']], '<object>' :[['Car'], ['Computer'],['Assignment']]}

import sys
from random import choice, seed

def expand (symbol):
	if symbol.startswith('<'):
		definitions = grammar[symbol]
		expansions  = choice(definitions)
		map(expand, expansions)
	else :
		print symbol


expand('<start>')

'''
This
Assignment
is here.

'''
