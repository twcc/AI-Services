#!/bin/bash
# origin william@NCHC
# modify kmo@NCHC 2019.0222 
# modify leo.chen@twsc.io 2021/01/12

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

cd AI-Services/Tutorial_Three
wget https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz

echo "copy data to ~/.keras/datasets/cifar-10-batches-py.tar.gz"
#pipenv run python src/test/s3.py download -s $COPYTOFILE -d ~/.keras/datasets/ -k cifar-10-python.tar.gz
mv ~/AI-Services/Tutorial_Three/cifar-10-python.tar.gz ~/.keras/datasets/cifar-10-batches-py.tar.gz

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


