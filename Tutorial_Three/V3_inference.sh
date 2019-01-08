#!/bin/bash
echo "---------------------"
echo "---- Inferencing ----"
echo "---------------------"

cd inceptionv3/
sudo pip install -r requirements.txt >> install.log

cd inference/

python flask_web.py 


