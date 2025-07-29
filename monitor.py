from time import sleep
import sys

def is_vital_in_range(value, lower, upper):
    return lower <= value <= upper

def print_alert(message):
    print(message)
    blink_alert()

def blink_alert():
    for _ in range(6):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)

def vitals_ok(temperature, pulseRate, spo2):
    vitals = [
        ('Temperature', temperature, 95, 102, 'Temperature critical!'),
        ('Pulse Rate', pulseRate, 60, 100, 'Pulse Rate is out of range!'),
        ('Oxygen Saturation', spo2, 90, 100, 'Oxygen Saturation out of range!')
    ]

    all_ok = True
    for _, value, low, high, message in vitals:
        if not is_vital_in_range(value, low, high):
            print_alert(message)
            all_ok = False
    return all_ok
