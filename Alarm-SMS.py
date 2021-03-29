# Import modules needed
import time
import RPi.GPIO as GPIO
import SMS

# setup GPIO using Broadcom SOC channel numbering
GPIO.setmode(GPIO.BCM)

# define the GPIO port you will use for the motion detector
PIR_SENSOR = 23

# number of seconds to delay between alarms
DELAY = 5

# set message
MSG = '<desired message>'

# setup phone and carrier information
NUMBER = '<your phone number, no spaces or dashes>'
CARRIER = '<your carrier>'

# set to pull-up (normally closed position for a PIR sensor dry contact)
GPIO.setup(PIR_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
	# setup an indefinite loop that looks for the PIR sensor to be triggered
	while True:
		# motion is detected
		GPIO.wait_for_edge(PIR_SENSOR, GPIO.RISING)
		# print and send message
		print(MSG)
		SMS.send(NUMBER, CARRIER, MSG)

		# do you want a time delay in between alarms?
		time.sleep(DELAY)

except KeyboardInterrupt:
	# cleanup GPIOs on keyboard exit
	GPIO.cleanup()

# cleanup GPIOs when program exits
GPIO.cleanup()
