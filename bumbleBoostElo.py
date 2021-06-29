import pyautogui
import time
import random
import click

d = 0  # number of left swipes
e = 0  # number of right swipes

while True:
	b = 0 #counter
	a = random.randint(0, 7) #anzahl bilder ansehen
	c = random.randint(0, 2) #no (0)(1) or yes (2)
	pyautogui.click(1106, 558) #erster klick geht immer hier hin
	while b<a:
		k = random.randint(0, 3) 
		if k <= 2:
			pyautogui.click(1106, 558) #weiteres bild ansehen
			b+=1
			time.sleep(random.randint(2,4))
			print ("klick fuer weiteres bild in der ersten schleife" + str(b))
		else :
			pyautogui.click(1150, 195)
			time.sleep(random.randint(3,5))
			print("klick fuer vorheriges bild")
	print "goodbye loop"
	if c == 0 or c == 1:
		pyautogui.click(658, 689) #left swipe
		d+=1
		print (str(d) + "left swipes")
		print (str(e) + "right swipes")
	elif c == 2:
		pyautogui.click(1063, 674) #right swipe
		e += 1
		print (str(d) + "left swipes")
		print (str(e) + "right swipes")
	time.sleep(random.randint(3, 5))
	print ("das programm wurde mit b beendet =" + str(b))
