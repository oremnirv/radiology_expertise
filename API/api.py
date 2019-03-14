import pandas as pd
import pickle

features = pd.read_csv("radiologist_features.csv")
with open('cluster_dict.pickle', 'rb') as handle:
    clusters = pickle.load(handle)

###
# input: pandas df
# Output: pandas df first column "npi" and other columns are features
# with scores
###

def get_features_with_npi(features=features):
    return features.iloc[:, :-1]

###
# input: int, pandas df
# Output: list of npis associated with cluster number
###


def get_npis_of_cluster(cluster_num, features=features):
    return features.loc[features["label"] == cluster_num, "npi"]


###
# input: str, dict[dict], pandas dataframe
# Output: str, list(str), list(str)
###

def get_radiologist_specialties(npi, clusters=clusters, features=features):
    label = features.loc[features["npi"].isin(list([npi])), :]["label"]
    cluster_info_description = clusters[int(label)]["procedure_description"]
    cluster_info_codes = clusters[int(label)]["group_speciality_procedures"]

    return [npi, cluster_info_codes, cluster_info_description]

####
# Output: dict[dict] - including label of cluster,
# associated rows in features df, hcpcs codes representing speciality
# and hcpcs descriptions
####


def get_full_clusters_data(clusters=clusters):
    return clusters