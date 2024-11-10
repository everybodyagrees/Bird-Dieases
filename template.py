import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep"
    f"src{project_name}/__init_.py",
    f"src{project_name}/components/__init_.py",
    f"src{project_name}/utils/__init_.py",
    f"src{project_name}/configs/__init_.py",
    f"src{project_name}/components/configuration.py",
    f"src{project_name}/pipeline/__init_.py",
    f"src{project_name}/entity/__init_.py",
    f"src{project_name}/constants/__init_.py",\
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"


]


for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename = os.path.split(filepath) 


    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info("Creating directory;{filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exist")