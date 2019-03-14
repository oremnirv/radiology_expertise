import numpy as np
import pandas as pd

####
# Input: df - pandas dataframe [num_radiologist X (num_procedures + 2)]
#        clusters - dict[dict]. keys: 0-num_groups from EM
#                   keys' keys: dict_keys(['labels', 'group_speciality_procedures', 'scores', 'procedure_description']
# Output: pandas dataframe [num_radiologist X (unique_procedures_from_clusters + 2)]
####

def extract_features(df, clusters, num_groups):

    cluster_procedures = [(np.array(
        clusters[k]["group_speciality_procedures"]).reshape(-1, 1)) for k in clusters.keys()]
    cols = (np.unique(np.vstack(cluster_procedures)))
    for i in range(num_groups):
        cols_w_score = clusters[i]["group_speciality_procedures"]
        df.loc[df[0] == i, cols_w_score] = clusters[i]["scores"]
        non_zero_cols = np.append(np.append(cols_w_score, 0), "npi")
        df.loc[df[0] == i, ~df.columns.isin(non_zero_cols)] = 0
    feature_cols = np.append(np.append(cols, 0), "npi")
    df = df.loc[:, df.columns.isin(feature_cols)]
    df = df.rename(index=str, columns={0: "label"})

    return df


def main():

    pass


if __name__ == '__main__':
    main()
