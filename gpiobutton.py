from subprocess import call
import os, random
import RPi.GPIO as GPIO

#HELPER METHODS

def setupEvents():
	GPIO.add_event_detect(button1, GPIO.FALLING, bouncetime=200)
	GPIO.add_event_detect(button2, GPIO.FALLING, bouncetime=200)
	GPIO.add_event_detect(buttonExit, GPIO.FALLING, bouncetime=200)

def removeEvents():
	GPIO.remove_event_detect(button1)
	GPIO.remove_event_detect(button2)
	GPIO.remove_event_detect(buttonExit)

def playFile(dir, file):
	call("play " + dir + file, shell=True)

def pickRandomFile(directory):
	return random.choice(os.listdir(directory))

def playRandomFile(directory):
	playFile(directory, pickRandomFile(directory))

# Set Up GPIO

GPIO.setmode(GPIO.BCM)

button1 = 4
button2 = 17
buttonExit = 26

GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonExit, GPIO.IN, pull_up_down=GPIO.PUD_UP)

##Setup File Locations

dir1 = '/home/pi/Desktop/sound1/'
dir2 = '/home/pi/Desktop/sound2/'

##MAIN LOOP

setupEvents()
print "Starting main loop"

while 1:
	if GPIO.event_detected(button1):
		removeEvents()
		playRandomFile(dir1)
		setupEvents()
	elif GPIO.event_detected(button2):
		removeEvents()
		playRandomFile(dir2)
		setupEvents()
	elif GPIO.event_detected(buttonExit):
		break

GPIO.cleanup()

call('play /home/pi/Desktop/utilsound/goodbye.wav', shell=True)
