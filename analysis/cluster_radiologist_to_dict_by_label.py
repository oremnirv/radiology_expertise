import numpy as np
from scipy import stats
from find_representitive_class_member import *


###
# Input: pandas dataframe, numpy array[float], numpy array[int], pandas dataframe, int
# Output: dict[dict]
###


# construct a dictionary for all cluster members with their speciality procedures
# scores for these specialities based on quantile score
# and wording description of procedures
def radiologist_dict(df_w_labels, model_means, labels, hcpcs_combos, best_model_num):
    clusters = {}

    for i in range(best_model_num):
        clusters[i] = {}
        clusters[i]["labels"] = (np.where(labels == i))

    for i in range(best_model_num):
        cluster_members = (
            df_w_labels.loc[df_w_labels[0] == i, :].iloc[:, 1:-1]).reset_index(drop=True)
        closest_idx = find_idx_closest_member_to_center(
            model_means[i], cluster_members)
        vals_bigger_than_100 = cluster_members.loc[closest_idx[0],
                                                   :][cluster_members.loc[closest_idx[0], :] > 100]
        representitive_procedures = vals_bigger_than_100.index
        clusters[i]["group_speciality_procedures"] = representitive_procedures
        scores = []
        if(len(representitive_procedures) > 0):
            for j in range(len(representitive_procedures)):
                scores.append(stats.percentileofscore(
                    df_w_labels[representitive_procedures[j]], vals_bigger_than_100[j]))
        else:
            scores = None
        clusters[i]["scores"] = scores
        clusters[i]["procedure_description"] = (hcpcs_combos[hcpcs_combos["hcpcs_code"].isin(
            representitive_procedures)]["hcpcs_description"])

    return clusters


def main():
    pass


if __name__ == '__main__':
    main()
