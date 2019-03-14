import pandas as pd

###
# Input: pandas dataframe
# Output: pandas dataframe
###


# find all unique combinations of hcpcs codes  and descriptions
def unique_combo(df):
    hcpcs_descrip = df.groupby(['hcpcs_code', 'hcpcs_description']).size(
    ).reset_index().rename(columns={0: 'count'})

    return hcpcs_descrip.loc[:, ['hcpcs_code', 'hcpcs_description']]


def main():

    pass

if __name__ == '__main__':
    main()



