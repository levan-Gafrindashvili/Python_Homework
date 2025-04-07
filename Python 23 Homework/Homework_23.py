
import unittest
from Process_orders import process_orders

class TestProcessOrders(unittest.TestCase):
    def testproduct_NotIn_inventory(self):
        orders = [
            {"product": "banana", "quantity": 5}
        ]
        inventory = {
            "apple": 10,
            }
        
        with self.assertRaises(ValueError) as context:
            process_orders(orders, inventory)
        
        self.assertEqual(str(context.exception), "Product 'banana' not found in inventory") # <-- 
        #აქ მინდოდა დამეწერა Your Product is not in inventory ეს და რომ ვწერდი აღარ მუშაობდა რატომ?
    
    def testNotEnoughStock(self):
        orders = [
            {"product": "apple", "quantity": 15}
        ]
        inventory = {
            "apple": 1
        }
        with self.assertRaises(ValueError) as context:
            process_orders(orders, inventory)
        
        self.assertEqual(str(context.exception), "Not enough stock for 'apple'")

    def testSuccessfulOrder(self):
        orders = [
            {"product": "apple", "quantity": 5},
            {"product": "banana", "quantity": 3}
        ]
        inventory = {
            "apple": 10,
            "banana": 15
        }
        result = process_orders(orders, inventory)
        self.assertEqual(result, orders)
        self.assertEqual(inventory, {"apple": 5, "banana": 12})
        

if __name__ == "__main__":
    unittest.main()