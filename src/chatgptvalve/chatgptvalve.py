import time


class Valve:
    def __init__(self):
        self._open_switch = False
        self._closed_switch = True
        self._pressure = 0.0
        self._interlock = False
        self._state = 'closed'
        self._transition_time = 1.0

    @property
    def open_switch(self):
        return self._open_switch

    @property
    def closed_switch(self):
        return self._closed_switch

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, value):
        self._pressure = value
        if self._pressure < 1.0:
            self._interlock = True
        else:
            self._interlock = False

    @property
    def interlock(self):
        return self._interlock

    @property
    def state(self):
        return self._state

    def _transition(self, new_state):
        print(f"Transitioning from {self._state} to {new_state}")
        self._state = new_state

    def open(self):
        if self._state == 'closed' and not self._interlock:
            self._transition('opening')
            time.sleep(self._transition_time)
            self._transition('open')
        else:
            print("Cannot open the valve due to interlock or current state")

    def close(self):
        if self._state == 'open' and not self._interlock:
            self._transition('closing')
            time.sleep(self._transition_time)
            self._transition('closed')
        else:
            print("Cannot close the valve due to interlock or current state")

