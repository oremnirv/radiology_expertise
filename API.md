# Physician expertise API interface

Query the module to get features and analyse

## Getting Started

First, follow the setup.md file instructions.


After the enviornment is set and the main.py file was executed,

We are able to interface with any program and query the following:

```
Get a pandas df including all npis and all features
Get npis associated with a specific cluster number
Get the specialities associated with a specific npi
Get full information on all clusters
```

We give an example hereunder how to query each of the requests

### All features with npi's

```
run python -c 'from api import get_features_with_npi; get_features_with_npi()'

Output:

npi   feature_1_score feature_2_score  feature_3_score   ...
...

```

### Cluster's npis

Specify cluster_num
```
e.g.
cluster_num = 5
run python -c 'from api import get_npis_of_cluster; get_npis_of_cluster(cluster_num)'

Output:
1013159680
1023046265
1023076049
1033130836
...

```

## Physician specialities

Specify npi string

```
e.g.
npi = "1013159680"
run python -c 'from api import get_radiologist_specialties; get_radiologist_specialties(npi)'

Output:
CT scan head or brain
X-ray of chest, 1 view, front

```

Note that the running time is aprox. 1 hr: 30 min for filtering and 20
min for the EM algorithm training.

## Full cluster data
```
e.g.
cluster_num = 5
run python -c 'from api import get_full_clusters_data; get_full_clusters_data()'

Output:
{0: {'labels': (array([  10, ...])), 'group_speciality_procedures':  Index(['70450', '71010', '71020'], 'scores': [52.4048488008342, 67.75938477580813, 51.03623566214807], 'procedure_description':  CT scan head or brain, X-ray of chest, 1 view, front, X-ray of chest, 2 views, front and side}, 1: {...},...}
...

```

## Author

***Omer Nivron** - *DRAFT work*



