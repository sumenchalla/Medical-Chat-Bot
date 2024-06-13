from src.logger import logging
from src.utils import read_yaml
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path


config_ds = read_yaml(Path("D:\Data Science\ML\Projects\Medical_chatbot\config.yaml"))

@dataclass

class dataingestionconfig:
    root_folder   = config_ds["dataingestion_config"]["root_dir"]
    source_url    = config_ds["dataingestion_config"]["source_url"]
    download_path = config_ds["dataingestion_config"]["download_path"]
    unzip_path    = config_ds["dataingestion_config"]["unzip_path"]  
