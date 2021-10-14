import unittest
import customer
import coins
import cans

class TestGetWalletCoin(unittest.TestCase):
    """Tests the Customer class's get_wallet_coin method"""

    def setUp(self):
        self.customer = customer.Customer()

    def test_get_wallet_coin_quarter(self):
        """Pass in Quarter, check to see if the wallet returns a Quarter"""
        self.assertEqual(
            self.customer.get_wallet_coin(coins.Quarter().name).value, .25)

    def test_get_wallet_coin_dime(self):
        """Pass in Dime, check to see if the wallet returns a Dime"""
        self.assertEqual(
            self.customer.get_wallet_coin(coins.Dime().name).value, .10)

    def test_get_wallet_coin_nickel(self):
        """Pass in Nickel, check to see if the wallet returns a Nickel"""
        self.assertEqual(
            self.customer.get_wallet_coin(coins.Nickel().name).value, .05)

    def test_get_wallet_coin_penny(self):
        """Pass in Penny, check to see if the wallet returns a Penny"""
        self.assertEqual(
            self.customer.get_wallet_coin(coins.Penny().name).value, .01)

    def test_get_wallet_coin_list(self):
        """Pass in a list, check to see if the wallet does not add items from a list"""
        self.assertEqual(
            self.customer.get_wallet_coin('Invalid'), None)

class TestAddCoinsToWallet(unittest.TestCase):
    """Tests the Customer class's add_coins_to_wallet"""

    def setUp(self):
        self.customer = customer.Customer()

    def test_add_three_coins_to_wallet(self):
        """Adds three coins to the wallet, checks to see if the length of of the coins list extends by three"""
        length1 = len(self.customer.wallet.money)
        self.customer.add_coins_to_wallet([coins.Penny(), coins.Penny(), coins.Penny()])
        self.assertEqual(length1 + 3, len(self.customer.wallet.money))

    def test_add_no_coins_to_wallet(self):
        """Adds no coins to the wallet, checks to see if the length of of the coins list does not extend"""
        length1 = len(self.customer.wallet.money)
        self.customer.add_coins_to_wallet([])
        self.assertEqual(length1, len(self.customer.wallet.money))

class TestAddCanToBackpack(unittest.TestCase):
    """Tests the Customer class's add_can_to_backpack method"""

    def setUp(self):
        self.customer = customer.Customer()

    def test_add_one_can_tobackpack(self):
        """Adds one can to the backpack, checks to see if the length of the packpack list extends by one"""
        self.customer.add_can_to_backpack(cans.Cola())
        self.assertEqual(len(self.customer.backpack.purchased_cans), 1)
    
    def test_add_two_can_tobackpack(self):
        """Adds two can to the backpack, checks to see if the length of the packpack list extends by two"""
        self.customer.add_can_to_backpack(cans.Cola())
        self.customer.add_can_to_backpack(cans.Cola())
        self.assertEqual(len(self.customer.backpack.purchased_cans), 2)

    def test_add_three_can_tobackpack(self):
        """Adds three can to the backpack, checks to see if the length of the packpack list extends by three"""
        self.customer.add_can_to_backpack(cans.Cola())
        self.customer.add_can_to_backpack(cans.Cola())
        self.customer.add_can_to_backpack(cans.Cola())
        self.assertEqual(len(self.customer.backpack.purchased_cans), 3)

if __name__ == '__main__':
    unittest.main()