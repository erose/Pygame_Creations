import pygame

"""
A wrapper around the pygame.Surface object which we draw upon.
Supports drawing onto the screen, clearing the screen.
Knows its width + height in pixels.
"""

class Screen():
	def __init__(self, width, height):
		# In pixels.
		self.width, self.height = width, height

		# Create and store a Surface object representing the screen.
		self.surface = pygame.display.set_mode((width, height))

		# Create a background Surface which we blit onto the screen to clear it.
		self.background = pygame.Surface((width, height))

	"""
	Draws the given image at the specified coordinates.
	"""
	def draw_at(self, image, position):
		# We draw onto the surface, not the background.
		self.surface.blit(image, position)

	def clear(self):
		# Blit the background onto the screen.
		self.surface.blit(self.background, (0, 0))

