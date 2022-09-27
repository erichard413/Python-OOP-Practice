"""Python serial number generator."""

from tracemalloc import start


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """creates new serial number at starting number
            takes starting number int
        """
        self.start = start
        self.num = start
    def generate(self):
        """generates new incremental number"""
        serial_num = self.num
        self.num = self.num + 1
        return serial_num
    def reset(self):
        """resets serial number back to starting number value"""
        self.num = self.start
    
    
