from dynamoDB_init import dynamo_DB

###
# Input: dynamoDB.Table object
# Output: dict
###


def get_dynamoDB_table_metadata(table):
    """
    Get some metadata about chosen table.
    """
    return {
        'num_items': table.item_count,
        'primary_key_name': table.key_schema[0],
        'status': table.table_status,
        'bytes_size': table.table_size_bytes,
        'global_secondary_indices': table.global_secondary_indexes
    }


def main():
    handle = dynamo_DB(
        "us-east-2", "RH5BUCbHGiY/AmD33xKX8eymm902PHHNiUqaTy3y", "AKIAIENW5YLQFYRWHC2Q")
    table = handle.get_table("Medicare2016Filtered")
    print(get_dynamoDB_table_metadata(table))


if __name__ == '__main__':
    main()
