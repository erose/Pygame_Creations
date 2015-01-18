import pygame
from Screen import Screen

"""
The current view of the universe.
Keeps track of the celestials that we have to draw.
"""

class View:
	def __init__(self, universe, width, height, center=(0, 0), zoom=10):
		# The universe this is a view of.
		self.universe = universe

		# The position in the universe at which this view is centered.
		self.center = center

		# The initial pixels/point ratio.
		self.zoom = zoom

		# The width and height of the view (in points).
		self.width, self.height = width, height

		# The actual Surface which is drawn upon.
		# Width, height are in units of points,
		# so we adjust them by a factor of zoom to get pixels.
		self.screen = Screen(width * zoom, height * zoom)

		# Initialize the {(x, y) : Celestial} dictionary.
		self.update()

	"""
	Sets the center of this view to new coordinates.
	"""
	def recenter(self, new_x, new_y):
		# Set center to the new center.
		self.center = new_x, new_y

		# Update because visibility may have changed.
		self.update()

	"""
	Increments or decrements the zoom level.
	"""
	def change_zoom(self, dzoom):
		if dzoom > 0:
			self.set_zoom(self.zoom + dzoom)

		if dzoom < 0 and self.zoom > 1:
			self.set_zoom(self.zoom + dzoom)

	"""
	Changes the zoom level to the specified value.
	"""
	def set_zoom(self, new_zoom):
		self.zoom = new_zoom

		# Update because visibility may have changed.
		self.update()

	"""
	Adjusts the center of the view by dx, dy.
	"""
	def translate(self, dx, dy):
		x, y = self.center
		self.recenter(x + dx, y + dy)

	"""
	Called whenever the view changes in a way that may affect what objects are visible.
	"""
	def update(self):
		# What once was viewable may be no longer.
		self.viewable = {}

		# Iterate through every object in the universe.
		for position, celestial in self.universe:
			# The absolute position of the celestial.
			x, y = position

			# The absolute position of the center of the view.
			center_x, center_y = self.center

			# The radius, converted to pixels.
			r = celestial.radius * self.zoom

			# The width and height, converted to pixels.
			w, h = self.width * self.zoom, self.height * self.zoom

			# Calculate the relative positions in pixels.
			relative_x = x - center_x
			relative_y = y - center_y

			if  (
				(-r + -w/2 <= relative_x * self.zoom <= w/2 + r)
				and
				(-r + -h/2 <= relative_y * self.zoom <= h/2 + r)
				):

					# The object is in our view, so save it (by the relative position).
					self.viewable[(relative_x, relative_y)] = celestial

					# Create an image for this object, at the current zoom level.
					celestial.image = celestial.generate_image(self.zoom)

	"""
	Wipes the screen and draws all of the viewable objects onto it.
	"""
	def draw(self):
		self.screen.clear()

		for position, celestial in self.viewable.items():
			# The radius (multiplied by zoom to get it in pixels).
			r = celestial.radius * self.zoom

			# We're using (0, 0) is the middle, but blit uses (0, 0) = top left.
			x, y = position

			# In units of pixels.
			draw_position = (
							(self.width/2 + x) * self.zoom,
							(self.height/2 + y) * self.zoom
							)

			# Blit places images by their top left corners.
			# so we adjust x and y by the number of pixels in the radius.
			draw_position = tuple(i - r for i in draw_position)

			#  print(draw_position)

			self.screen.draw_at(celestial.image, draw_position)

		# Update so we can see the changes.
		pygame.display.flip()
