#!/bin/bash
# origin william@NCHC
# modify kmo@NCHC 2019.0222 

for arg in "$@"
do
  if [ "$arg" == "--path" ] || [ "$arg" == "-p" ]
  then
     COPYTOFILE="$2"
  fi
done
echo "Start Process"
echo "Checking for folder"

if [ ! -d "~/.keras/datasets" ];
then
    echo "Creating ~/.keras/datasets"
    mkdir -p ~/.keras/datasets
else
    echo "~/.keras/datasets already exists"
fi

if [ -z "$COPYTOFILE" ]
then
      echo "s3bucket is not define, result will save in weight folder"
else
      echo "result will save in $COPYTOFILE"
      s3bucket="$COPYTOFILE"
fi

echo "--------------------"
echo "----- Download -----"
echo "--------------------"
# Install pipenv
pip install -e git+https://github.com/pypa/pipenv.git@bugfix/resolver-markers#egg=pipenv
# Clone TWCC-CLI
git clone https://github.com/TW-NCHC/TWCC-CLI.git
# cd to TWCC-CLI & Install 
cd TWCC-CLI && pipenv install

echo "copy data to ~/.keras/datasets/cifar-10-batches-py.tar.gz"
pipenv run python src/test/s3.py download -s obj0612 -d ~/.keras/datasets/ -k cifar-10-python.tar.gz
mv ~/.keras/datasets/cifar-10-python.tar.gz ~/.keras/datasets/cifar-10-batches-py.tar.gz

echo "extract cifar-10-batches-py.tar.gz"
tar -C ~/.keras/datasets/  -xvzf ~/.keras/datasets/cifar-10-batches-py.tar.gz > progress.log

if [ -d ~/.keras/datasets/cifar-10-batches-py ]; then
  echo "Finished extract data "
fi

echo "--------------------"
echo "----- Training -----"
echo "--------------------"

EPOCH=5
BATCH=45

cd ~/AI-Services/Tutorial_Three/inceptionv3/

#cd inceptionv3/
sudo pip install -r requirements.txt >> install.log

cd train/

python V3.py start-training --batch $BATCH --epoch $EPOCH

echo "--------------------"
echo "------ Upload ------"
echo "--------------------"

cd ~/AI-Services/Tutorial_Three/TWCC-CLI
pipenv run python src/test/s3.py upload -s ~/AI-Services/Tutorial_Three/inceptionv3/train/weights/ -d "$COPYTOFILE" -r

