# buttonsound
Holds the code and description for a random-sound player.

This project was begun based on a conversation with on 5/1/15. A breif description:

"This project should consist of a small(ish) box with two buttons. If you press one button, the box should play a randomly selected sound from a collection of sound files. If you press the other button, the box should play a randomly selected sound from a different collection of sound files. These sound files will be continually updated/added to."

==========REQUIRED LIBRARIES=================

sox: the Sound Exchange library (uses "play" functionality)
os: for selecting a file from the file system
random: for choosing a random file
RPi.GPIO: for accepting input



========HARDWARE DESCRIPTION=================

This program responds to three buttons:
  Button 1 (BCM Pin 4): Play a sound from the first collection of sounds
  Button 2 (BCM Pin 17): Play a sound from the second colllections of sounds
  Button Exit (BCM Pin 26): Exit the waiting loop, cleanup GPIO, and end program.
