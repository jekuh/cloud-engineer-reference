import unittest
from unittest.mock import MagicMock
from check_order_update_type import check_order_update_type

class TestCheckOrderUpdateType(unittest.TestCase):

    def test_tag_update(self):
        order_input = {
            "oe-cherwell-request-id": "136094",
            "oe-account-order-type": "update",
            "oe-account-budget": "20"
        }
        result = check_order_update_type(order_input)
        expected_result = {
            "update_type": "tag_update",
            "account_protection_change": False,
            "account_name_change": False,
            "account_ou_change": False
        }
        self.assertEqual(result, expected_result)

    def test_tf_update_account_name_change(self):
        order_input = {
            "oe-cherwell-request-id": "136094",
            "oe-account-order-type": "update",
            "oe-account-budget": "20",
            "oe-account-name": "NewName"
        }
        result = check_order_update_type(order_input)
        expected_result = {
            "update_type": "tf_update",
            "account_protection_change": False,
            "account_name_change": True,
            "account_ou_change": False
        }
        self.assertEqual(result, expected_result)

    def test_tf_update_account_protection_change(self):
        order_input = {
            "oe-cherwell-request-id": "136094",
            "oe-account-order-type": "update",
            "oe-account-budget": "20",
            "oe-account-protection": "new_value"
        }
        result = check_order_update_type(order_input)
        expected_result = {
            "update_type": "tf_update",
            "account_protection_change": True,
            "account_name_change": False,
            "account_ou_change": False
        }
        self.assertEqual(result, expected_result)

    def test_tf_update_account_ou_change(self):
        order_input = {
            "oe-cherwell-request-id": "136094",
            "oe-account-order-type": "update",
            "oe-account-budget": "20",
            "oe-account-ou": "new_value"
        }
        result = check_order_update_type(order_input)
        expected_result = {
            "update_type": "tf_update",
            "account_protection_change": False,
            "account_name_change": False,
            "account_ou_change": True
        }
        self.assertEqual(result, expected_result)

    def test_tf_update(self):
        order_input = {
            "oe-cherwell-request-id": "136094",
            "oe-account-order-type": "create",
            "oe-account-budget": "20"
        }
        result = check_order_update_type(order_input)
        expected_result = {
            "update_type": "tf_update",
            "account_protection_change": False,
            "account_name_change": False,
            "account_ou_change": False
        }
        self.assertEqual(result, expected_result)

    def test_tag_update(self):
        order_input = {
            "oe-cherwell-request-id": "136094",
            "oe-account-order-type": "create",
            "oe-account-legal-entity": "CH696"
        }
        result = check_order_update_type(order_input)
        expected_result = {
            "update_type": "tag_update",
            "account_protection_change": False,
            "account_name_change": False,
            "account_ou_change": False
        }
        self.assertEqual(result, expected_result)

    def test_edge_update(self):
        order_input = {
            "oe-cherwell-request-id": "136094",
            "oe-account-order-type": "create",
            "oe-account-protection": True
        }
        result = check_order_update_type(order_input)
        expected_result = {
            "update_type": "edge_update",
            "account_protection_change": True,
            "account_name_change": False,
            "account_ou_change": False
        }
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
