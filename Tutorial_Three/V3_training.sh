#!/bin/bash
for arg in "$@"
do
  if [ "$arg" == "--path" ] || [ "$arg" == "-p" ]
  then
     COPYTOFILE="$2"
  fi
done
echo "Start Process"
echo "Checking for fodler"

if [ ! -d "~/.keras" ];then
echo "Creating .kears"
mkdir ~/.keras
fi

if [ ! -d "~/.keras/datasets" ]; then
echo "Creating datasets"
mkdir ~/.keras/datasets
fi

echo "Moving data to folder"
cp -R /mnt/s3/"$COPYTOFILE"/cifar-10-python.tar.gz ~/.keras/datasets/cifar-10-batches-py.tar.gz
tar -C ~/.keras/datasets/  -xvzf ~/.keras/datasets/cifar-10-batches-py.tar.gz >> progress.log

echo "Finished moving data"

echo "--------------------"
echo "----- Training -----"
echo "--------------------"

EPOCH=100
BATCH=45

#if [ ! -d "/mnt/s3/$COPYTOFILE/weights/" ]; then
#echo "Creating weight folder"
#mkdir /mnt/s3/"$COPYTOFILE"/weights/
#fi

cd inceptionv3/
sudo pip install -r requirements.txt >> install.log

cd train/

python V3.py start-training --batch $BATCH --epoch $EPOCH

cp -R ./weights /mnt/s3/"$COPYTOFILE"/

echo "Finished Training"
