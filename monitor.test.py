import unittest
import monitor as m


class MonitorTest(unittest.TestCase):

    # --- Unit tests for pure functions ---
    def test_is_vital_in_range(self):
        self.assertTrue(m.is_vital_in_range(98, 95, 102))
        self.assertFalse(m.is_vital_in_range(104, 95, 102))

    def test_check_vital_ok(self):
        ok, msg = m.check_vital("Pulse Rate", 75, 60, 100, "is out of range!")
        self.assertTrue(ok)
        self.assertIsNone(msg)

    def test_check_vital_not_ok(self):
        ok, msg = m.check_vital("Pulse Rate", 120, 60, 100, "is out of range!")
        self.assertFalse(ok)
        self.assertEqual(msg, "Pulse Rate is out of range!")

    def test_check_all_vitals_ok(self):
        ok, msgs = m.check_all_vitals(98.1, 75, 95)
        self.assertTrue(ok)
        self.assertEqual(len(msgs), 0)

    def test_check_all_vitals_failures(self):
        ok, msgs = m.check_all_vitals(104, 120, 85)
        self.assertFalse(ok)
        self.assertEqual(len(msgs), 3)

    # --- Integration tests ---
    def test_vitals_ok_true(self):
        self.assertTrue(m.vitals_ok(98.1, 75, 95))

    def test_vitals_ok_false(self):
        self.assertFalse(m.vitals_ok(99, 120, 70))


if __name__ == "__main__":
    unittest.main()
