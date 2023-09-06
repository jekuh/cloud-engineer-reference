import json
import boto3


class AccountAccess:
    
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table('account_access')

    def insert_data(self, account_id, date, role, authentication):
        self.table.put_item(
            Item={
                'account_id': account_id,
                'date': date,
                'role': role,
                'authentication': authentication
            }
        )

    def read_data(self, account_id):
        response = self.table.get_item(Key={'account_id': account_id})
        item = response.get('Item')
        return item

def lambda_handler(event, context):
    account_id = event['account_id']
    date = event['date']
    role = event['role']
    authentication = ['authentication']

    account_access = AccountAccess()
    
    account_access.insert_data(account_id, date, role, authentication)

    return {
        'statusCode': 200,
        'body': 'Data inserted successfully'
    }


TABLE_NAME = 'account_access'
BUCKET_NAME = 'athena4cloudtrail-result'
FILE_KEY = '5161104c-08e2-4785-af99-b93e05028be7.csv'