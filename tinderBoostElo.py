import pyautogui
import time
import random
import click

d = 0  # number of left swipes
e = 0  # number of right swipes

while True:
	a = random.randint(0, 6)
	b = 0
	c = random.randint(0,1)

	while b<a:
		pyautogui.click(950, 400)
		b+=1
		time.sleep(random.randint(2,4))
	if c == 1:	
		pyautogui.click(780,570)
		d+=1
		print (str(d) + "left swipes")
		print (str(e) + "right swipes")
	else:
		pyautogui.click(930,570)
		e += 1
		print (str(d) + "left swipes")
		print (str(e) + "right swipes")
	time.sleep(random.randint(3, 5))
