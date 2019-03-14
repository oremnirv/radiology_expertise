from sklearn.metrics import pairwise_distances_argmin_min

###
# Input: numpy array [float], pandas dataframe
# Output: int
###


# find index of closest member to cluster center
def find_idx_closest_member_to_center(cluster_means, cluster_members):
    closest, _ = pairwise_distances_argmin_min(
        cluster_means.reshape(1, -1), cluster_members)

    return closest


def main():
    pass


if __name__ == '__main__':
    main()
