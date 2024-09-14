@echo off
echo [%date% %time%]: "START"

echo [%date% %time%]: "creating env with python 3.10 version" 
conda create --name my_env python==3.10 -y

echo [%date% %time%]: "activating the environment" 
call conda activate my_env

echo [%date% %time%]: "installing the requirements" 
pip install -r requirements.txt

echo [%date% %time%]: "END" 





