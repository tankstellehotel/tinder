import pyautogui
import time
import random
import click

while True:
	a = random.randint(0, 6)
	b = 0
	while b<a:
		pyautogui.click(950, 400)
		b+=1
		time.sleep(random.randint(2,4))
	pyautogui.click(930,570)
	time.sleep(random.randint(3, 5))
