import pandas as pd

###
# Input: pandas dataframe
# Output: pandas dataframe
###


# Take original df and give every procedure a column with value of
# "line_srvc_cnt"
def transform_df(df):
    df = df.loc[:, ["npi", "hcpcs_code", "line_srvc_cnt"]
                ].reset_index(drop=True)
    df = pd.melt(df, id_vars=['npi', 'hcpcs_code'],
                 value_vars=['line_srvc_cnt'])
    transformed_df = df.groupby(
        ['npi', 'hcpcs_code']).sum().transpose().stack(0).reset_index()
    transformed_df = transformed_df.fillna(0)
    transformed_df.index.names = ['idx']
    transformed_df = transformed_df.drop("level_0", axis=1)

    return transformed_df


def main():

    pass


if __name__ == '__main__':
    main()
