import pyautogui
import time
import random
import click

while True:
	a = random.randint(0, 6)
	b = 0
	while b<a:
		pyautogui.click(1000, 550)
		b+=1
		time.sleep(random.randint(2,4))
	pyautogui.click(955,700)
	time.sleep(random.randint(1, 3))
	pyautogui.click(857,623)
	time.sleep(random.randint(3, 5))
