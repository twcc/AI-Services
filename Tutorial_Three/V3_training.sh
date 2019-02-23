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

if [ ! -d "~/.keras/datasets" ]; then
echo "Creating ~/.keras/datasets"
mkdir -p ~/.keras/datasets
fi


# checking s3 path exist or not
# if s3 path not exist, try local path
s3path=/mnt/s3/"$COPYTOFILE"
ffpath="$COPYTOFILE"

if [ -d "$s3path" ]; then
  ffpath=$s3path
fi

echo "copy data to ~/.keras/datasets/cifar-10-batches-py.tar.gz"
cp $ffpath/cifar-10-python.tar.gz ~/.keras/datasets/cifar-10-batches-py.tar.gz
if [ -f ~/.keras/datasets/cifar-10-batches-py.tar.gz ]; then
  echo "Finished copy data "
fi

echo "extract cifar-10-batches-py.tar.gz"
tar -C ~/.keras/datasets/  -xvzf ~/.keras/datasets/cifar-10-batches-py.tar.gz > progress.log
if [ -d ~/.keras/datasets/cifar-10-batches-py ]; then
  echo "Finished extract data "
fi


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

echo "starting rsync ./weights to $ffpath"
rsync -av --progress  ./weights $ffpath && echo "Finished Training"
