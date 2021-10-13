import unittest
import wallet  

class TestWallet(unittest.TestCase):
    """Tests to see if the Wallet class instantiates correctly"""

    def setUp(self):
        self.wallet = wallet.Wallet()

    def test_wallet_instantiation(self):
        self.assertEqual(len(self.wallet.money), 88)

if __name__ == '__main__':
    unittest.main()