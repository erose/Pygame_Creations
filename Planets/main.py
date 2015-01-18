import pygame
from time import sleep
from pygame.locals import *

# Local imports
from View import View
from Universe import Universe
from Celestial import Celestial
from Colors import *

paused = False
universe = None
view = None

# Timing specs for controlling frames per second
clock = pygame.time.Clock()
fps = 20

#------------
#--------------------
#------------

"""
Takes a single step of the simulation.
Called even when paused == True.
"""
def simulation_step():
	pass

"""
Called every frame.
"""
def handle_keypresses(pressed):
	global paused

	if pressed[K_RIGHT]: 		view.translate(1, 0)
	if pressed[K_LEFT]: 		view.translate(-1, 0)
	if pressed[K_UP]: 			view.translate(0, -1)
	if pressed[K_DOWN]: 		view.translate(0, 1)

	if pressed[K_a]:			view.change_zoom(1)
	if pressed[K_b]:			view.change_zoom(-1)

	if pressed[K_SPACE]:		paused = not (paused)
	
	if pressed[K_ESCAPE]:		quit()

"""
Hub for everything that runs once per frame.
"""
def main_loop():
	while True:
		view.draw()

		# We handle all keypresses every frame.
		handle_keypresses(pygame.key.get_pressed())

		# Listen for quit events.
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit()

		# Limits frames per second to the specified value.
		clock.tick(fps)

def quit():
	pygame.quit()
	exit()

if __name__ == "__main__":
	pygame.init()

	kashyyk = Celestial(name="Kashyyk", radius=2, base_color=GREEN)
	mars = Celestial(name="Mars", radius=10, base_color=RED)

	universe = Universe({
		(0, 0) : kashyyk,
		(15, 15) : mars
		})

	view = View(universe, 60, 60, center=(0, 0), zoom=10)

	main_loop()