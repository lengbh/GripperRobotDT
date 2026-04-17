"""Minimal GPIO-based motor controller."""

from gpiozero import OutputDevice


class Motor:
    """Control one motor through one GPIO output."""

    def __init__(self, gpio_number):
        self.pin = OutputDevice(gpio_number)
        self.pin.on()

    def run(self):
        self.pin.off()

    def stop(self):
        self.pin.on()

motor = Motor(17)
