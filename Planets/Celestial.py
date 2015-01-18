import pygame

#Local imports
from Colors import *

"""
An instance of Celestial is an un-reified object.
It knows everything except its position, acceleration, velocity.
"""
class Celestial(pygame.sprite.Sprite):
	def __init__(self, **attrs):
		#Call the pygame.Sprite constructor.
		pygame.sprite.Sprite.__init__(self)

		#The default attributes are Mars's.
		for attribute, default_value in [
			("name", "Mars"),
			("mass", 100),

			#Celestial objects are circles.
			#Radius is in points.
			("radius", 10),

			("visible", True),

			#These three are used to generate the image.
			("base_color", RED),
			("decoration", None),
			("transparency", 255)

		]:	setattr(self, attribute, attrs.get(attribute, default_value))

	"""
	Returns a pygame Surface, given a pixel/points ratio.
	Called when the celestial is seen.
	"""
	def generate_image(self, zoom):
		r = self.radius * zoom

		#Create a (diameter x diameter) square.
		image = pygame.Surface((r * 2, r * 2))

		#From top left, center is one radius down, one radius right.
		center = (r, r)
		pygame.draw.circle(image, self.base_color, center, r)

		#Decoration is a function applied to the image.
		if self.decoration is not None:
			self.decoration(self, image)

		#This image has a black background (the square) that we don't want to see.
		image.set_colorkey((0, 0, 0))

		#The alpha channel controls transparency (lower is more transparent).
		image.set_alpha(self.transparency)

		return image

	def __repr__(self):
		return "<{}>, mass: {}, radius {}".format(
			self.name, self.mass, self.radius)

if __name__ == "__main__":
	c = Celestial()
	print(c)

	k = Celestial(name="Kashyyk", mass=200, color=GREEN)
	print(k)