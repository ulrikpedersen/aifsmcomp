from chatgptvalve.chatgptvalve import Valve
# Unit tests
import unittest


class TestValve(unittest.TestCase):
    def test_initial_state(self):
        valve = Valve()
        self.assertEqual(valve.state, 'closed')

    def test_opening(self):
        valve = Valve()
        valve.pressure = 2.0
        valve.open()
        self.assertEqual(valve.state, 'open')

    def test_closing(self):
        valve = Valve()
        valve.pressure = 2.0
        valve.open()
        valve.close()
        self.assertEqual(valve.state, 'closed')

    def test_interlock(self):
        valve = Valve()
        valve.pressure = 0.5
        valve.open()
        self.assertEqual(valve.state, 'closed')
        self.assertTrue(valve.interlock)

    def test_invalid_transition_due_to_interlock(self):
        valve = Valve()
        valve.pressure = 0.5
        valve.open()
        valve.pressure = 2.0
        valve.close()
        self.assertEqual(valve.state, 'closed')  # Corrected assertion

    def test_invalid_transition_due_to_state(self):
        valve = Valve()
        valve.pressure = 2.0
        valve.open()
        valve.open()
        self.assertEqual(valve.state, 'open')


if __name__ == "__main__":
    unittest.main()
