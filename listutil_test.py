import unittest
from listutil import unique
 
class ListUtilTest(unittest.TestCase):
 
    def test_single_item_list(self):
        self.assertListEqual( ['hi'], unique(['hi']) )
    def test_single_item_many_time_list(self):
        self.assertListEqual(['1'] , unique(['1','1','1','1','1','1','1']))
    def test_two_item_many_time_many_order(self):
        self.assertListEqual(['1','2'], unique(['1','1','2','2','2','1']))
    def test_three_items_many_order(self):
        self.assertListEqual(['1','2','3'], unique(['2','3','1']))
    def test_three_items_many_order_many_times(self):
        self.assertListEqual(['1','2','3'], unique(['3','2','1','1','2','3','2','2','2']))
    def test_ten_items_many_order_many_times(self):
        self.assertListEqual(['1','2','3','4','5','6','7','8','9','10'], unique(['3','2','1','1','2','3','5','6','7','7','6','5','4','4','10','9','8']))
    def list_with_double_quote(self):
        self.assertListEqual(["1","2","3"], unique(['1','2','3']))
if __name__ == '__main__':
    unittest.main()