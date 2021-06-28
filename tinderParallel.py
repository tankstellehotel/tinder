import pyautogui
import time
import random
import click

while True:
	a = random.randint(0, 6)
	b = 0
	while b<a:
		pyautogui.click(613, 430)
		b+=1
		time.sleep(random.randint(2,4))
	pyautogui.click(485, 640)
	time.sleep(random.randint(3, 5))
