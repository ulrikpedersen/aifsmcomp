import time
from enum import Enum

class State(Enum):
    OPEN = 1
    CLOSED = 2
    OPENING = 3
    CLOSING = 4
    INTERLOCKED = 5

class Valve:
    def __init__(self):
        self.pressure = 0.0
        self.interlock = False
        self.end_switch_open = False
        self.end_switch_close = True
        self.state = State.CLOSED

    def open_valve(self):
        if not self.interlock:
            self.state = State.OPENING
            time.sleep(1)
            self.end_switch_open = True
            self.end_switch_close = False
            self.state = State.OPEN

    def close_valve(self):
        if not self.interlock:
            self.state = State.CLOSING
            time.sleep(1)
            self.end_switch_open = False
            self.end_switch_close = True
            self.state = State.CLOSED

    def update_pressure(self, pressure):
        self.pressure = pressure
        self.check_interlock()

    def check_interlock(self):
        if self.pressure < 1.0:
            self.interlock = True
            self.state = State.INTERLOCKED
        else:
            self.interlock = False

    def check_state(self):
        if self.interlock:
            self.state = State.INTERLOCKED
        elif self.end_switch_open:
            self.state = State.OPEN
        elif self.end_switch_close:
            self.state = State.CLOSED
