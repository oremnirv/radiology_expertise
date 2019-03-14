from boto3.dynamodb.conditions import (
    Attr, Key
)
import pandas as pd


###
# Input: dynamodb.Table object, list[str]
# Output: pandas dataframe
###

# filter radiologists in npi_list from dynamoDB.Table
def filter_npi_and_insert_to_pd_df(table, npi_list):
    df = pd.DataFrame()
    for i in npi_list:
        _response = table.query(
            KeyConditionExpression=(
                Key("npi").eq(i) &
                Key("hcpcs_code").begins_with("7")
            ),  # required condition
            # filter expressions are optional in DynamoDB queries!
            # This is just an example. You probably won't
            # need filter expressions.
        )

        # get items (drop response metadata)
        items = _response.get("Items")
        df = df.append(pd.DataFrame(items))

    return df


def main():

    pass


if __name__ == '__main__':
    main()
