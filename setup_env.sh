#!/bin/bash

#########################################
# Installing python and necessary packages.
# This script will install python
# into the ~/local/bin directory
#########################################

# installing python 3.7
mkdir -p ~/local/bin/
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
tar xvzf Python-3.7.0.tgz
cd Python-3.7.0
sudo yum install gcc
./configure
make
make altinstall prefix=~/local  # specify local installation directory
ln -s ~/local/bin/python3.7.0 ~/local/bin/python
cd ..

# Now you can install other packages using pip
~/local/bin/ curl -O https://bootstrap.pypa.io/get-pip.py
~/local/bin/ sudo python3 get-pip.py
~/local/bin/ sudo python3.4 -m pip install numpy==1.15.0 # install numpy
~/local/bin/ sudo python3.4 -m pip install scipy==1.1.0
~/local/bin/ sudo python3.4 -m pip install pandas==0.19.1
~/local/bin/ sudo python3.4 -m pip install boto3==1.7.74
~/local/bin/ sudo python3.4 -m pip install scikit-learn==0.19.2

