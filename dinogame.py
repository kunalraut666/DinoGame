import pyautogui as pg
from PIL import Image, ImageGrab
import time

def screenshot():
	image= ImageGrab.grab().convert('L')
	return image

lst = [x for x in range(83,176)]
	
def collide(data):

#White
#........Bird.............
	for i in range(300,350):
		for j in range(300,600):
			if data[i,j]==83:
				pg.keyDown('down')
				time.sleep(0.2)
				pg.keyUp('down')
				return True

#........Cactus...........	
	for i in range(350,400):
		for j in range(600,710):
			if data[i,j]==83:
				pg.press('space')
				return True

				
#black
# ........Bird.............
	for i in range(300,350):
		for j in range(300,600):
			if data[i,j] in lst:
				pg.keyDown('down')
				time.sleep(0.2)
				pg.keyUp('down')
				return True
#.......Cactus...........
	for i in range(350,400):
			for j in range(600,710):
				if data[i,j] in lst:
					pg.press('space')
					return True



	return False
			
time.sleep(2)
pg.press('up')
while True:
	image=screenshot()
	data=image.load()
	collide(data) 
