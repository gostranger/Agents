from pygame import gfxdraw
import pygame
import sys,os

pygame.init()
x_axis=500
y_axis=500
count =0
screen = pygame.display.set_mode([x_axis,y_axis])
running = True
class ant:
	def __init__(self,x_axis,y_axis):
		self.x = x_axis
		self.y = y_axis
		self.setUp()
	
	def getLoc(self):
		return [self.x,self.y]

	def setUp(self):
		self.up = True
		self.down = False
		self.right = False
		self.left = False

	def setDown(self):
		self.up = False
		self.down = True
		self.right = False
		self.left = False

	def setRight(self):
		self.up = False
		self.down = False
		self.right = True
		self.left = False
	
	def setLeft(self):
		self.up = False
		self.down = False
		self.right = False
		self.left = True

	def Left(self):
		if self.up:
			self.x = (self.x-1)%x_axis
			self.setLeft()
		elif self.down:
			self.x = (self.x+1)%x_axis
			self.setRight()
		elif self.right:
			self.y = (self.y+1)%y_axis
			self.setUp()
		elif self.left:
			self.y = (self.y-1)%y_axis
			self.setDown()

	def Right(self):
		if self.up:
			self.x = (self.x+1)%x_axis
			self.setRight()
		elif self.down:
			self.x = (self.x-1)%x_axis
			self.setLeft()
		elif self.right:
			self.y = (self.y-1)%y_axis
			self.setDown()
		elif self.left:
			self.y = (self.y+1)%y_axis
			self.setUp()
		
	def Forward(self):
		if self.up:
			self.y = (self.y+1)%y_axis
		elif self.down:
			self.y = (self.y-1)%y_axis
		elif self.right:
			self.x = (self.x+1)%x_axis
		elif self.left:
			self.x = (self.x-1)%x_axis

def checkpixel(x,y):
	return screen.get_at((x,y))

def equal(a,b):
	if a[0] == b[0]:
		if a[1] == b[1]:
			if a[2] == b[2]:
				return True
	return False

white = [255,255,255,255]
black = [0,0,0,255]
ant1 = ant(x_axis-100,y_axis-100)
ant2 = ant(100,100)

def move(antt):
	antt.Forward()
	if equal(checkpixel(antt.getLoc()[0],antt.getLoc()[1]),white):	
		gfxdraw.pixel(screen,antt.getLoc()[0],antt.getLoc()[1],[0,0,0])
		antt.Right()
	elif equal(checkpixel(antt.getLoc()[0],antt.getLoc()[1]),black):
		gfxdraw.pixel(screen,antt.getLoc()[0],antt.getLoc()[1],[255,255,255])
		antt.Left()



while(running):
	for event in pygame.event.get():
        	if event.type == pygame.QUIT:
			running = False
	
	move(ant1)
	move(ant2)
	
	count = count+1
	pygame.display.flip()


print("Agent took ["+str(count)+"] Iteration")
pygame.quit()

