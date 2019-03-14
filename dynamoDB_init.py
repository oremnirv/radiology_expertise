from boto3 import resource
from boto3.dynamodb.conditions import (
    Attr, Key
)


# instantiate dynamodb resource
class dynamo_DB:

    def __init__(self, region_name, aws_secret_access_key, aws_access_key_id):
        self.region_name = region_name
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_access_key_id = aws_access_key_id

        self.dynamodb_handle = resource(
            "dynamodb", region_name=self.region_name,
            aws_secret_access_key=self.aws_secret_access_key,
            aws_access_key_id=self.aws_access_key_id)

    def get_table(self, table_name):
        self.table = self.dynamodb_handle.Table(table_name)

        return self.table

def main():
    handle = dynamo_DB(
        "us-east-2", "RH5BUCbHGiY/AmD33xKX8eymm902PHHNiUqaTy3y", "AKIAIENW5YLQFYRWHC2Q")
    table = handle.get_table("Medicare2016Filtered")


if __name__ == '__main__':
    main()
