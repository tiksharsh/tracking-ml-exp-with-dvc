## read params
## process
### return dataframe
# https://www.analyticsvidhya.com/blog/2021/06/mlops-tracking-ml-experiments-with-data-version-control/
# https://github.com/amitvkulkarni/Versioning-ML-Models-datasets-With-DVC/blob/main/src/get_data.py

import os
import yaml
import pandas as pd
import argparse

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=',', encoding="utf-8")
    df = pd.get_dummies(df, columns=['famhist'], drop_first= True)
    df.drop('sbp', axis=1, inplace=True)
    return df

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default='params.yaml')
    parsed_args = args.parse_args()
    data = get_data(config_path = parsed_args.config)