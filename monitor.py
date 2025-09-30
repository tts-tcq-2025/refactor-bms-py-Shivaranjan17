from time import sleep
import sys


# --- Pure functions (logic only) ---

def is_vital_in_range(value: float, lower: float, upper: float) -> bool:
    """Check if a vital sign is within the given range."""
    return lower <= value <= upper


def check_vital(name: str, value: float, low: float, high: float, alert_message: str):
    """Return (ok, message) for a vital sign."""
    if is_vital_in_range(value, low, high):
        return True, None
    return False, f"{name} {alert_message}"


def check_all_vitals(temperature: float, pulse_rate: float, spo2: float):
    """Return (overall_ok, list_of_messages) for all vitals."""
    vitals = [
        ("Temperature", temperature, 95, 102, "critical!"),
        ("Pulse Rate", pulse_rate, 60, 100, "is out of range!"),
        ("Oxygen Saturation", spo2, 90, 100, "out of range!"),
    ]

    results = [check_vital(name, val, low, high, msg) for name, val, low, high, msg in vitals]
    overall_ok = all(ok for ok, _ in results)
    messages = [msg for ok, msg in results if not ok]
    return overall_ok, messages


# --- I/O functions (alerts, blinking, printing) ---

def print_alert(message: str):
    """Print alert and blink."""
    print(message)
    blink_alert()


def blink_alert():
    """Simulate blinking alert with console output."""
    for _ in range(3):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(0.5)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(0.5)


def vitals_ok(temperature: float, pulse_rate: float, spo2: float) -> bool:
    """Main function for consumers. Runs logic + alerts."""
    overall_ok, messages = check_all_vitals(temperature, pulse_rate, spo2)
    for msg in messages:
        print_alert(msg)
    return overall_ok
