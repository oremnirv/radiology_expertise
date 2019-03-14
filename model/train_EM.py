from sklearn.mixture import GaussianMixture
import numpy as np
import pandas as pd

###
# Input: df - pandas dataframe
# Output: GaussianMixture object - model with lowest AIC, labels - numpy array,
#                                  num_cluster_groups - int
###


# train the EM algorithm for different clusters between  1-max_compenents
# and choose the model with lowest AIC
def EM(df, max_compenents=40):
    n_components = np.arange(1, max_compenents)
    models = [GaussianMixture(n, covariance_type='full', random_state=0).fit(df.values)
              for n in n_components]
    # choose model with lowest AIC score
    best_model_num = np.argmin(list([m.aic(df.values) for m in models]))
    labels = models[best_model_num].predict(df.values)

    return (models[best_model_num], labels, best_model_num + 1)


###
# Input: df - pandas dataframe, labels - numpy array [num_radiologists]
# Output: pandas dataframe
###

# add labels predicted by EM model to match npi's
def add_label_to_df(df, labels):
    labels = lp = pd.Series(labels)
    df_w_labels = pd.concat([df.reset_index(drop=True), labels], axis=1)

    return df_w_labels


def main():
    pass


if __name__ == '__main__':
    main()
