import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pin = 21

try:
    while True:
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)
        ans = GPIO.input(pin)
        print('ans = ',ans)
except KeyboardInterrupt:
    print('exit pressed Ctrl+C')
except:
    print('other exception')
finally:
    GPIO.cleanup() #return PINs to the origin state
    print('end of program')

