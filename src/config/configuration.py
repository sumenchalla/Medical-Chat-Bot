from src.utils import read_yaml
from dataclasses import dataclass
from pathlib import Path
from os.path import join


config_ds = read_yaml(Path("D:\Data Science\ML\Projects\Medical_chatbot\config.yaml"))


class dataingestionconfig:
    def __init__(self):
        self.root_folder   = join(Path("D:\Data Science\ML\Projects\Medical_chatbot"),Path(config_ds["dataingestion_config"]["root_dir"]))
        self.source_url    = config_ds["dataingestion_config"]["source_url"]
        self.download_path = join(Path("D:\Data Science\ML\Projects\Medical_chatbot"),Path(config_ds["dataingestion_config"]["download_path"]))
        self.unzip_path    = join(Path("D:\Data Science\ML\Projects\Medical_chatbot"),Path(config_ds["dataingestion_config"]["unzip_path"]))
