import os
from pathlib import Path

project_name = "german_visa"
list_of_files = [ 
     
     f"{project_name}/__init__.py",
     f"{project_name}/components/__init__.py",
     f"{project_name}/components/data_ingestion.py",
     f"{project_name}/components/data_validation.py",
     f"{project_name}/components/data_transformation.py",
     f"{project_name}/components/model_trainer.py",
     f"{project_name}/components/model_evaluation.py"
     f"{project_name}/components/model_pusher.py"
     f"{project_name}/configuration/__init__.py",
     f"{project_name}/constant/__init__.py",
     f"{project_name}/entity/__init__.py",
     f"{project_name}/entity/config_entity/__init__.py",
      f"{project_name}/entity/artifact_entity/__init__.py",
     f"{project_name}/exception/__init__.py",
     f"{project_name}/logger/__init__.py",
     f"{project_name}/pipeline/__init__.py",
     f"{project_name}/pipeline/training.py",
     f"{project_name}/pipeline/prediction.py,"
     f"{project_name}/utils/__init__.py",
     f"{project_name}/utils/main_utils.py",
     "app.py",
     "requirements.txt",
     "setup.py",
     "Dockerfile",
     ".dockerignore",
     "demo.py",
     "config/model.yaml",
     "config/schema.yaml"]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir,file_name = os.path.split(filepath)
    if file_dir !="":
        os.makedirs(file_dir,exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
    else:
        print(f"File {filepath} already exists")