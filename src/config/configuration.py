from src.utils import read_yaml
from dataclasses import dataclass
from pathlib import Path
from os.path import join
import os

root_path =  Path("D:\Data Science\ML\Projects\Medical_chatbot")
config_ds = read_yaml(join(root_path,"config.yaml"))


class dataingestionconfig:
    def __init__(self):
        self.root_folder   = join(root_path,Path(config_ds["dataingestion_config"]["root_dir"]))
        self.source_url    = config_ds["dataingestion_config"]["source_url"]
        self.download_path = join(root_path,Path(config_ds["dataingestion_config"]["download_path"]))
        self.unzip_path    = join(root_path,Path(config_ds["dataingestion_config"]["unzip_path"]))


@dataclass
class DataTransformationconfig:
    preprocessor_obj_file_path=os.path.join(root_path,'artifacts\preprocessor.pkl')
