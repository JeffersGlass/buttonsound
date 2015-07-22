from subprocess import call
import os, random
import RPi.GPIO as GPIO

#HELPER METHODS

##Add event listener for the two buttons to play soundss, and a third button to exit the program cleanly
##This method is called after each sound is played to re-enable event listening.
def setupEvents():
	GPIO.add_event_detect(button1, GPIO.FALLING, bouncetime=200)
	GPIO.add_event_detect(button2, GPIO.FALLING, bouncetime=200)
	GPIO.add_event_detect(buttonExit, GPIO.FALLING, bouncetime=200)

##Removes listening for any events
##This method is called immedaitely after any button is pressed, to block any further button presses until a sound is finished playing
def removeEvents():
	GPIO.remove_event_detect(button1)
	GPIO.remove_event_detect(button2)
	GPIO.remove_event_detect(buttonExit)

##Call's the 'play' command from the Sox library on the given file in the appropriate directory. The 'play' command is usually successful at playing the sound, regardles of format or length
def playFile(dir, file):
	call("play " + dir + file, shell=True)

##Selects a random file from the given directory, independent of OS file structure
def pickRandomFile(directory):
	return random.choice(os.listdir(directory))

##Wrapper function; uses the above playFile and pickRandomFile functions to play a random file.
def playRandomFile(directory):
	playFile(directory, pickRandomFile(directory))

# Set Up GPIO

GPIO.setmode(GPIO.BCM)

#Various GPIO input pins on the rPI
button1 = 4
button2 = 17
buttonExit = 26

#Enable the pull-up pins on our GPIO pin. The pins will be activated by pulling them to ground.
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
	if GPIO.event_detected(button1): #Play a file from the first collection
		removeEvents()
		playRandomFile(dir1)
		setupEvents()
	elif GPIO.event_detected(button2): #Play a file from the second collection
		removeEvents()
		playRandomFile(dir2)
		setupEvents()
	elif GPIO.event_detected(buttonExit): #Exit
		break

GPIO.cleanup()

#Play a goodbye sound before exiting.
call('play /home/pi/Desktop/utilsound/goodbye.wav', shell=True)
