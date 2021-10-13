import unittest
import customer

class TestGetWalletCoin(unittest.TestCase):
    """Tests the Customer class's get_wallet_coin method"""

    def setUp(self):
        self.customer = customer.Customer()

    def test_get_wallet_coin_quarter(self):
        """Pass in Quarter, check to see if the wallet returns a Quarter"""
        returned_coin = self.customer.get_wallet_coin('Quarter')
        self.assertEquals(returned_coin.value, .25)

    def test_get_wallet_coin_dime(self):
        """Pass in Dime, check to see if the wallet returns a Dime"""
        returned_coin = self.customer.get_wallet_coin('Dime')
        self.assertEquals(returned_coin.value, .10)

    def test_get_wallet_coin_nickel(self):
        """Pass in Nickel, check to see if the wallet returns a Nickel"""
        returned_coin = self.customer.get_wallet_coin('Nickel')
        self.assertEquals(returned_coin.value, .05)

    def test_get_wallet_coin_penny(self):
        """Pass in Penny, check to see if the wallet returns a Penny"""
        returned_coin = self.customer.get_wallet_coin('Penny')
        self.assertEquals(returned_coin.value, .01)

class TestAddCoinsToWallet(unittest.TestCase):
    """Tests the Customer class's add_coins_to_wallet"""

    def setUp(self):
        self.customer = customer.Customer()

    def test_add_three_coins_to_wallet(self):
        """Adds three coins to the wallet, checks to see if the length of of the coins list extends by three"""
        self.customer.wallet.money = []
        self.customer.add_coins_to_wallet(['Penny', 'Nickel', 'Dime'])
        self.assertEquals(len(self.customer.wallet.money), 3)

    def test_add_no_coins_to_wallet(self):
        """Adds no coins to the wallet, checks to see if the length of of the coins list does not extend"""
        self.customer.wallet.money = []
        self.customer.add_coins_to_wallet([])
        self.assertEquals(len(self.customer.wallet.money), 0)

class TestAddCanToBackpack(unittest.TestCase):
    """Tests the Customer class's add_can_to_backpack method"""

    def setUp(self):
        self.customer = customer.Customer()

    def test_add_one_can_tobackpack(self):
        pass

if __name__ == '__main__':
    unittest.main()