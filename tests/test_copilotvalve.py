from copilotvalve.copilotvalve import Valve, State
import unittest

class TestValve(unittest.TestCase):
    def setUp(self):
        self.valve = Valve()

    def test_open_close(self):
        self.valve.update_pressure(1.5)
        self.valve.open_valve()
        self.assertEqual(self.valve.state, State.OPEN)
        self.valve.close_valve()
        self.assertEqual(self.valve.state, State.CLOSED)

    def test_interlock(self):
        self.valve.update_pressure(0.5)
        self.assertEqual(self.valve.state, State.INTERLOCKED)
        self.valve.open_valve()
        self.assertEqual(self.valve.state, State.INTERLOCKED)
        self.valve.update_pressure(1.5)
        self.valve.open_valve()
        self.assertEqual(self.valve.state, State.OPEN)

if __name__ == '__main__':
    unittest.main()