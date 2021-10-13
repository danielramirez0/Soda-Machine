import unittest
from soda_machine import SodaMachine
import coins
import cans


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
        self.assertEqual(
            (self.soda_machine.get_coin_from_register('Quarter')).name, 'Quarter')

    def test_get_dime(self):
        """Asserts a quarter can be pulled from register"""
        self.assertEqual(
            (self.soda_machine.get_coin_from_register('Dime')).name, 'Dime')

    def test_get_nickel(self):
        """Asserts a quarter can be pulled from register"""
        self.assertEqual(
            (self.soda_machine.get_coin_from_register('Nickel')).name, 'Nickel')

    def test_get_penny(self):
        """Asserts a quarter can be pulled from register"""
        self.assertEqual(
            (self.soda_machine.get_coin_from_register('Penny')).name, 'Penny')

    def test_get_none(self):
        """Asserts a quarter can be pulled from register"""
        self.assertEqual(
            self.soda_machine.get_coin_from_register('None'), None)


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

    def test_higher_payment(self):
        '''Asserts positive return'''
        self.assertGreater(
            self.soda_machine.determine_change_value(1.5, .5), .5)

    def test_lower_payment(self):
        '''Asserts negative return'''
        self.assertLess(self.soda_machine.determine_change_value(.5, 1.5), 1.5)

    def test_equal_payment(self):
        '''Asserts 0 return'''
        self.assertEqual(self.soda_machine.determine_change_value(1.5, 1.5), 0)


class TestCalculateCoinValue(unittest.TestCase):

    def setUp(self) -> None:
        self.soda_machine = SodaMachine()
        self.all_coins = [
            coins.Quarter(),
            coins.Nickel(),
            coins.Dime(),
            coins.Penny()
        ]

    def test_calculate_all_coins(self):
        self.assertEqual(
            self.soda_machine.calculate_coin_value(self.all_coins), .41)

    def test_calculate_empyt_coins(self):
        self.assertEqual(self.soda_machine.calculate_coin_value([]), 0)


class TestGetInventorySoda(unittest.TestCase):

    def setUp(self) -> None:
        self.soda_machine = SodaMachine()

    def test_cola(self):
        self.assertEqual(
            self.soda_machine.get_inventory_soda("Cola").name,
            "Cola"
        )

    def test_orange_soda(self):
        self.assertEqual(
            self.soda_machine.get_inventory_soda("Orange Soda").name,
            "Orange Soda"
        )

    def test_root_beer(self):
        self.assertEqual(
            self.soda_machine.get_inventory_soda("Root Beer").name,
            "Root Beer"
        )

    def test_mountain_dew(self):
        self.assertEqual(
            self.soda_machine.get_inventory_soda("Mountain Dew"),
            None
        )


class TestReturnInventory(unittest.TestCase):

    def setUp(self) -> None:
        self.soda_machine = SodaMachine()
        self.soda = cans.Cola()

    def test_add_can(self):
        self.soda_machine.return_inventory(self.soda)
        self.assertEqual(
            len(self.soda_machine.inventory),
            31
        )


class TestDepositCoinsIntoRegister(unittest.TestCase):

    def setUp(self) -> None:
        self.soda_machine = SodaMachine()
        self.all_coins = [
            coins.Quarter(),
            coins.Nickel(),
            coins.Dime(),
            coins.Penny()
        ]
    
    def test_deposit_coins(self):
        self.soda_machine.deposit_coins_into_register(self.all_coins)
        self.assertEqual(len(self.soda_machine.register), 92)



if __name__ == '__main__':
    unittest.main()
