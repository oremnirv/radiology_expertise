# Radiology expertise exploration

Extarct radiologist speciality features for future predictive modelling

## Getting Started

*** If run on instance please use t2.large

First, install git and clone the current repository

```
sudo yum install git
git clone current-repository
```

Start by running the shell script

```
./setup_env.sh
```

If any problems occured, please follow the instructions below. Otherwise, jump to Running the program section.


### Prerequisites

For this program we will use python 3.6.5
with packages:

```
numpy 1.15.0
scipy 1.1.0
pandas 0.19.1
boto3 1.7.74
scikit-learn 0.19.2
```

### Installing

Install python 3.6.5 and pip:

```
https://realpython.com/installing-python/
```

After python is installed run in command line
```
pip install numpy==1.15.0 # install numpy
pip install scipy==1.1.0
pip install pandas==0.19.1
pip install boto3==1.7.74
pip install scikit-learn==0.19.2

```

## Running the program

Once the enviornment is set, from the command line do:

```
python3 central.py
```

Note that the running time is aprox. 1 hr 30 min for filtering and 20
min for the EM algorithm training.

## Output
The file main.py will produce a csv file with radiologist features named
"radiologist_features.csv" and a pickled dictionary "cluster_dict.pickle"
containing the different clusters and their speciality


## Authors

***Omer Nivron** - *DRAFT work*



