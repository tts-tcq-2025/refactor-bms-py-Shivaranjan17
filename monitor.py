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
    all_ok = True

    if not is_vital_in_range(temperature, 95, 102):
        print_alert('Temperature critical!')
        all_ok = False

    if not is_vital_in_range(pulseRate, 60, 100):
        print_alert('Pulse Rate is out of range!')
        all_ok = False

    if not is_vital_in_range(spo2, 90, 100):
        print_alert('Oxygen Saturation out of range!')
        all_ok = False

    return all_ok
