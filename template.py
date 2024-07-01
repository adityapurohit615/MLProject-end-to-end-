import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "mlproject"

list_of_file = [
    #".github/workflows/.gitkeep",#ye hum ek folder bana rhe hai and we make this folder because during deployement we use github actions and the code for github actions is written here
    f"src/{project_name}/__init__.py",#ye hamara project folder hai mlproject name se and if in future agar hume isse package banana hoga toh we will use __init__.py
    f"src/{project_name}/components/__init__.py",# this init file we use so that when we compile it, it can become a package
    f"src/{project_name}/components/data_ingestion.py",#this is our data ingestion file in which we will read the data and will transform it into training and test data
    f"src/{project_name}/components/data_transformation.py",#in this file we will transform the  data and perform operation on the data like feature engineering and feature transformation
    f"src/{project_name}/components/model_trainer.py",# in this file we will train our model
    f"src/{project_name}/components/model_monitoring.py",# in this file we will write the code to monitor out model
    # now we will create the files for the pipeline,Up untill now we have created the files for the component
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py", #in this we will create a training pipeline
    f"src/{project_name}/pipeline/prediction_pipeline.py",# and similarly we will create our prediction pipeline using the components in this file
    # we need some more files in our project beside the pipelines and its components and those files are listed below
    f"src/{project_name}/exception.py", # this file will handle the exception handling of our project
    f"src/{project_name}/logger.py", # this file will handle the logging details of our project
    f"src/{project_name}/utils.py", # this file will handle the utilities of our project
    "__init__.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"



]

for filepath in list_of_file:
    filepath = Path(filepath) # using this we will be iterating on all the paths for the files that are available in our list_of_files list
    filedir,filename = os.path.split(filepath) #os.path.split(filepath) will give us file directory, and file name which we will use in either creating a new file or to check if the file of this name already exist

    if filedir != "": #if the file directory for a particular file does not exist we will make a directory for that file
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
    # the above code means if the path of the file does not exist or if the file size is 0
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file:{filepath}")
        # then basically we will open the file path and we will create an empty file for that file path
    else: # and if the IF condition doesnot work that means the file path already exist and we will print this message
        logging.info(f"{filename} already exist")

