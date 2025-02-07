import unittest

from engine.CapuletEngine import CapuletEngine # every 30,000 miles
from engine.SternmanEngine import SternmanEngine # when the warning indicator is on
from engine.WilloughbyEngine import WilloughbyEngine # every 60,000 miles

class TestCapuletEngine(unittest.TestCase): 
    def ShouldBeServiced(self):
        CurrentMileage = 30001
        LastServiceMileage = 0
        engine = CapuletEngine(CurrentMileage, LastServiceMileage)
        self.assertTrue(engine.NeedsService())

    def ShouldNotBeServiced(self):
        CurrentMileage = 25000
        LastServiceMileage = 0
        engine = CapuletEngine(CurrentMileage, LastServiceMileage)
        self.assertFalse(engine.NeedsService())

class TestWilloughbyEngine(unittest.TestCase): 
    def ShouldBeServiced(self):
        CurrentMileage = 60001
        LastServiceMileage = 0
        engine = WilloughbyEngine(CurrentMileage, LastServiceMileage)
        self.assertTrue(engine.NeedsService())

    def ShouldNotBeServiced(self):
        CurrentMileage = 55000
        LastServiceMileage = 0
        engine = WilloughbyEngine(CurrentMileage, LastServiceMileage)
        self.assertFalse(engine.NeedsService())

class TestSternmanEngine(unittest.TestCase): 
    def ShouldBeServiced(self):
        WarningLightIsOn = True
        engine = SternmanEngine(WarningLightIsOn)
        self.assertTrue(engine.NeedsService())

    def ShouldNotBeServiced(self):
        WarningLightIsOn = False
        engine = SternmanEngine(WarningLightIsOn)
        self.assertFalse(engine.NeedsService())