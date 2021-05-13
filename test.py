import unittest
import calculator
 
class TestCarPark(unittest.TestCase):
    def testInputIsZero(self):
        self.assertEqual(calculator.calulate(0, 0), 0)
 
    def testInputIsNegativeTime(self):
        self.assertEqual(calculator.calulate(-10, -10), 0)
        self.assertEqual(calculator.calulate(-20, -5), 0)
        self.assertEqual(calculator.calulate(-1, -9), 0)

    def testHourNotMoreThanTwentyMinute(self):
        self.assertEqual(calculator.calulate(0, 1), 0)
        self.assertEqual(calculator.calulate(0, 15), 0)
        self.assertEqual(calculator.calulate(0, 20), 0)

    def testHourIsMoreThanOneButBelowThree(self):
        self.assertEqual(calculator.calulate(1, 0), 10)
        self.assertEqual(calculator.calulate(3, 0), 50)
        self.assertEqual(calculator.calulate(2, 30), 50)

    def testHourIsMoreThanThree(self):
        self.assertEqual(calculator.calulate(5, 15), 170)
        self.assertEqual(calculator.calulate(4, 0), 90)
 
if __name__ == '__main__':
   unittest.main()