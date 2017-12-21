import RPi.GPIO as GPIO
import time

# BOARD нумерация контактов
# моторы
motor_l=13
motor_r=15

# направение
way_l=16
way_r=18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor_l, GPIO.OUT, initial=0)
GPIO.setup(motor_r, GPIO.OUT, initial=0)
GPIO.setup(way_l, GPIO.OUT, initial=0)
GPIO.setup(way_r, GPIO.OUT, initial=0)

try:
    GPIO.output(motor_l, GPIO.LOW)
    GPIO.output(motor_r, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(motor_l, GPIO.HIGH)
    GPIO.output(motor_r, GPIO.LOW)
    time.sleep(2)
    GPIO.output(motor_l, GPIO.HIGH)
    GPIO.output(motor_r, GPIO.HIGH)
    time.sleep(2)
    
except KeyboardInterrupt:
    print("Exit pressed Ctrl+C")

except:
    print("Other exception")
    
finally:
    GPIO.cleanup()
    print("end of script")
