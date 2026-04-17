"""Minimal GPIO-based motor controller."""

from gpiozero import OutputDevice


class MotorController:
    """Control one motor through one GPIO output."""

    def __init__(self, gpio_number):
        self.motor = OutputDevice(gpio_number)

    def motor_on(self):
        self.motor.on()

    def motor_off(self):
        self.motor.off()
