import pyautogui
import time
import random
import click

left_swipes = 0
right_swipes = 0

while True:
	counter = 0
	anzahl_bilder_wechseln = random.randint(0, 7)
	ja_oder_nein = random.randint(0, 2)
	pyautogui.click(1106, 558) #erster klick geht immer hier hin
	print(f"erster klick geht raus")
	print(f"es werden {anzahl_bilder_wechseln} bilder gewechselt")
	while counter < anzahl_bilder_wechseln:
		wahrsch_fuer_naechses_bild = random.randint(0, 3) 
		if wahrsch_fuer_naechses_bild <= 2:
			pyautogui.click(1106, 558) #weiteres bild ansehen
			counter+=1
			time.sleep(random.randint(2,4))
			print (f"klick fuer weiteres bild in der ersten schleife {counter}")
		else :
			pyautogui.click(1114, 195)
			time.sleep(random.randint(3,5))
			print(f"klick fuer vorheriges bild in der zweiten schleife")
	print ("goodbye loop")
	if ja_oder_nein <= 1:
		pyautogui.click(758, 689) #left swipe
		left_swipes+=1
		print (f"so viele {left_swipes}left swipes")
		print (f"so viele {right_swipes}right swipes")
	elif ja_oder_nein == 2:
		pyautogui.click(963, 674) #right swipe
		right_swipes += 1
		print (f"so viele left swipes -> {left_swipes}")
		print (f"so viele right swipes ->  {right_swipes}")
	time.sleep(random.randint(3, 5))
	print (f"das programm wurde mit dem counter {counter} beendet")
