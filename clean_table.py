import numpy as np
import pandas as pd


###
# Input: pandas dataframe
# Output: pandas dataframe
###

# remove "|" from the "line_srvc_cnt" column and sum the values in each cell
def line_srvc_cnt_cleanup(df):
    df['line_srvc_cnt'] = df['line_srvc_cnt'].map(lambda x: (x.split("|")))
    df['line_srvc_cnt'] = df['line_srvc_cnt'].map(
        lambda x: sum((map(float, x))))

    return df

###
# Input: pandas dataframe
# Output: pandas dataframe
###


# remove "|" from the "hcpcs_description" column
def hcpcs_description_cleanup(df):
    sep = "|"
    df["hcpcs_description"] = df["hcpcs_description"].map(
        lambda x: x.split(sep, 1)[0])

    return df


###
# Input: df - pandas dataframe, hcpcs_combo - pandas dataframe [num_procedures X 2]
# Output: pandas dataframe - each duplicate procedure is merged into one column
###

# we sum duplicate procedures (assumption)
def duplicate_procedure_cleanup(df, hcpcs_combo):
    duplicates = hcpcs_combo.iloc[np.where(
        hcpcs_combo["hcpcs_description"].duplicated(False))[0], :]
    unique_dupli_procedure = duplicates["hcpcs_description"].unique()
    for i in range(len(unique_dupli_procedure)):
        idxes = hcpcs_combo[hcpcs_combo["hcpcs_description"]
                            == unique_dupli_procedure[i]]["hcpcs_code"].values
        df[idxes[0]] = (df[idxes].sum(axis=1))
        df = df.drop(idxes[1:], axis=1)

    return df

###
# Input: df - pandas dataframe
# Output: pandas dataframe
###

# remove cols when max is < 100
def remove_col_w_o_specialists(df):
    removable_cols = [
        np.where(np.argmax(np.array(df.iloc[:, 1:]), axis=0) < 100)[0] + 1]
    df = df.drop(df.columns[removable_cols], axis=1)
    return df


def main():

    pass


if __name__ == '__main__':
    main()
