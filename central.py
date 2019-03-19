import time
import pickle
from spreemo_pickle import read_pkl_file
from dynamoDB_init import dynamo_DB
from filter_npis_in_pickle_file import filter_npi_and_insert_to_pd_df
from clean_table import *
from transform_df_to_npi_times_hcpcs_code import *
from train_EM import *
from cluster_radiologist_to_dict_by_label import *
from unique_hcpcs_code_description_combo import *
from clusters_to_features import *


def main():
    npi_list = read_pkl_file("npis.pkl")
    # handle = dynamo_DB(
    #     "", "", "")
    # table = handle.get_table("Medicare2016Filtered")
    start_time = time.time()
    print("start at:", start_time)
    df = filter_npi_and_insert_to_pd_df(table, npi_list)
    print("filtering--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    df = line_srvc_cnt_cleanup(df)
    df = hcpcs_description_cleanup(df)
    hcpcs_combo = unique_combo(df)
    print("cleanup--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    df = transform_df(df)
    df = duplicate_procedure_cleanup(df, hcpcs_combo)
    df = remove_col_w_o_specialists(df)
    print("transform--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    model, labels, num_groups = EM(df.drop("npi", axis=1))
    print("EM--- %s seconds ---" % (time.time() - start_time))
    df_w_labels = add_label_to_df(df, labels)
    start_time = time.time()
    clusters = radiologist_dict(
        df_w_labels, model.means_, labels, hcpcs_combo, num_groups)
    print("cluster_descrip--- %s seconds ---" % (time.time() - start_time))
    features = extract_features(df_w_labels, clusters, num_groups)
    features.to_csv("radiologist_features.csv")
    with open('cluster_dict.pickle', 'wb') as handle:
        pickle.dump(clusters, handle, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
    main()
