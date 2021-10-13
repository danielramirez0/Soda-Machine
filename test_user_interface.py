import unittest
import user_interface
import cans
import coins


class TestValidateMainMenu(unittest.TestCase):
    """Tests if validate_main_menu method returns a the correct tuple"""

    def test_validate_main_menu_one(self):
        self.assertTupleEqual(user_interface.validate_main_menu(1), (True, 1))

    def test_validate_main_menue_two(self):
        self.assertTupleEqual(user_interface.validate_main_menu(2), (True, 2))

    def test_validate_main_menu_three(self):
        self.assertTupleEqual(user_interface.validate_main_menu(3), (True, 3))

    def test_validate_main_menu_four(self):
        self.assertTupleEqual(user_interface.validate_main_menu(4), (True, 4))

    def test_validate_main_menu_five(self):
        self.assertTupleEqual(
            user_interface.validate_main_menu(5), (False, None))


class TestTryParseInt(unittest.TestCase):
    """Tests if try_parse_int method returns the correct integer or returns 0"""

    def test_try_parse_int_ten(self):
        self.assertEqual(user_interface.try_parse_int('10'), 10)

    def test_try_parse_int_string(self):
        self.assertEqual(user_interface.try_parse_int('hello'), 0)


class TestGetUniqueCanNames(unittest.TestCase):
    """Tests if get_unique_can_names returns a filtered list removing all duplicates"""

    def test_get_unique_names_duplicates(self):
        test_cans = [
            cans.Cola(),
            cans.Cola(),
            cans.OrangeSoda(),
            cans.OrangeSoda(),
            cans.RootBeer(),
            cans.RootBeer()
        ]

        self.assertEqual(
            len(user_interface.get_unique_can_names(test_cans)), 3)

    def test_get_unique_names_empty(self):
        self.assertEqual(len(user_interface.get_unique_can_names([])), 0)


class TestDisplayPaymentValue(unittest.TestCase):
    """Tests if display_payment_value returns the sum of a list of coins which is passed in"""

    def test_display_payment_value_all(self):
        test_coins = [
            coins.Quarter(),
            coins.Nickel(),
            coins.Dime(),
            coins.Penny()
        ]

        self.assertEqual(user_interface.display_payment_value(test_coins), .41)

    def test_display_payment_value_empty(self):
        self.assertEqual(user_interface.display_payment_value([]), 0)


class TestValidateCoinSelection(unittest.TestCase):
    """Tests if validate_coin_selection returns the appropriate tuple"""

    def test_validate_coinselection_one(self):
        self.assertEqual(
            user_interface.validate_coin_selection(1), (True, "Quarter"))

    def test_validate_coinselection_two(self):
        self.assertEqual(
            user_interface.validate_coin_selection(2), (True, "Dime"))

    def test_validate_coinselection_three(self):
        self.assertEqual(
            user_interface.validate_coin_selection(3), (True, "Nickel"))

    def test_validate_coinselection_four(self):
        self.assertEqual(
            user_interface.validate_coin_selection(4), (True, "Penny"))

    def test_validate_coinselection_five(self):
        self.assertEqual(
            user_interface.validate_coin_selection(5), (True, "Done"))

    def test_validate_coinselection_six(self):
        self.assertEqual(
            user_interface.validate_coin_selection(6), (False, None))


if __name__ == '__main__':
    unittest.main()
