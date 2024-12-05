import os
# from box.exceptions import BoxValueError
import yaml
from src.CNN_Classifier import logger
import json
import joblib
# from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


def read_yaml(path: Path)->ConfigBox:
    try:
        with open(path ) as yaml_file:
            content= yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path } loaded  successfully")
            return ConfigBox(content)
    except ValueError:
        logger.info("Empty Yaml File")
        raise ValueError("Yaml file is Empty")
    except Exception as e:
        raise e



def create_directory(path: list,verbose = True):
    for path in path:
        os.makedirs(path,exist_ok= True)
        if verbose :
            logger.info(f"{path} directory  is created")


def save_json(path: Path,data: dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file stored at :{path}")        

def load_json(path: Path)->ConfigBox:
    with open(path)as f:
        content  = json.load(f)
    logger.info(f"Json file is loaded: {path}")
    return ConfigBox(content)



def save_bins(data: Any,path:Path):
    joblib.dump(value=data,filename=path)
    logger.info(f"Binary file Saved at {path}")


def load_bins(path: Path)->Any:
    data = joblib.load(path)
    logger.info(f'Binary file loaded :{path}')
    return data



def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())

