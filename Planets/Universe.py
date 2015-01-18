import pygame

"""
Keeps track of the absolute coordinates of all celestials.
"""
class Universe:
	def __init__(self, dic=None):
		#Allow some celestials to be passed in at the beginning.
		if dic is not None: self.dictionary = dic
		else: self.dictionary = {}

	"""
	Iterating over the Universe iterates over the underlying dictionary.
	"""
	def __iter__(self):
		return iter(self.dictionary.items())