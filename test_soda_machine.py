import unittest
from soda_machine import SodaMachine


class TestFillRegister(unittest.TestCase):

    def setUp(self) -> None:
        self.soda_machine = SodaMachine()

    def test_fill_register(self):
        """Asserts length of register is 88 coins"""
        self.assertEqual(len(self.soda_machine.register), 88)

class TestFillInventory(unittest.TestCase):

    def setUp(self) -> None:
        self.soda_machine = SodaMachine()

    def test_fill_inventory(self):
        """Asserts inventory is 30 items"""
        self.assertEqual(len(self.soda_machine.inventory), 30)

class TestGetCoinFromRegister(unittest.TestCase):

    def setUp(self) -> None:
        self.soda_machine = SodaMachine()

    def test_get_quarter(self):
        """Asserts a quarter can be pulled from register"""
        self.assertEqual((self.soda_machine.get_coin_from_register('Quarter')).name, 'Quarter')

    def test_get_dime(self):
        """Asserts a quarter can be pulled from register"""
        self.assertEqual((self.soda_machine.get_coin_from_register('Dime')).name, 'Dime')

    def test_get_nickel(self):
        """Asserts a quarter can be pulled from register"""
        self.assertEqual((self.soda_machine.get_coin_from_register('Nickel')).name, 'Nickel')

    def test_get_penny(self):
        """Asserts a quarter can be pulled from register"""
        self.assertEqual((self.soda_machine.get_coin_from_register('Penny')).name, 'Penny')

    def test_get_none(self):
        """Asserts a quarter can be pulled from register"""
        self.assertEqual(self.soda_machine.get_coin_from_register('None'), None)

class TestRegisterHasCoin(unittest.TestCase):

    def setUp(self) -> None:
        self.soda_machine = SodaMachine()

    def test_has_quarter(self):
        """Asserts register has a quarter"""
        self.assertTrue(self.soda_machine.register_has_coin("Quarter"))

    def test_has_dime(self):
        """Asserts register has a dime"""
        self.assertTrue(self.soda_machine.register_has_coin("Dime"))

    def test_has_nickel(self):
        """Asserts register has a nickel"""
        self.assertTrue(self.soda_machine.register_has_coin("Nickel"))

    def test_has_penny(self):
        """Asserts register has a penny"""
        self.assertTrue(self.soda_machine.register_has_coin("Penny"))

    def test_has_invalid(self):
        """Asserts invalid coin option entered"""
        self.assertFalse(self.soda_machine.register_has_coin("poop"))

class TestDetermineChangeValue(unittest.TestCase):

    def setUp(self) -> None:
        self.soda_machine = SodaMachine()

if __name__ == '__main__':
    unittest.main()
