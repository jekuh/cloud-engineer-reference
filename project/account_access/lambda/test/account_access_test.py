import unittest
from unittest.mock import MagicMock
from account_access.src.account_access import AccountAccess


class TestAccountAccess(unittest.TestCase):
    
    def setUp(self):
        self.account_access = AccountAccess()
        self.dynamodb_mock = MagicMock()
        self.table_mock = MagicMock()
        self.account_access.dynamodb = self.dynamodb_mock
        self.account_access.table = self.table_mock

    def test_insert_data(self):
        account_id = '123'
        date = '2022-01-01'
        role = 'admin'
        authentication = ['authentication']

        self.account_access.insert_data(account_id, date, role, authentication)

        self.table_mock.put_item.assert_called_once_with(
            Item={
                'account_id': account_id,
                'date': date,
                'role': role,
                'authentication': authentication
            }
        )

    def test_read_data(self):
        account_id = '123'

        response_mock = {
            'Item': {

            }
        }
        self.table_mock.get_item.return_value = response_mock

        result = self.account_access.read_data(account_id)

        self.assertEqual(result, response_mock['Item'])

if __name__ == '__main__':
    unittest.main()
