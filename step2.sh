#!/bin/bash
ar=($@)
EPOCH=100
BATCH=45
for arg in "${!ar[@]}"
do
   if [ "${ar[$arg]}" == "--path" ] || [ "${ar[$arg]}" == "-p" ]
   then
      COPYTOFILE="${ar[$(($arg + 1))]}"
   fi
   if [ "${ar[$arg]}" == "--epoch" ] || [ "${ar[$arg]}" == "-e" ]
   then
      EPOCH="${ar[$(($arg + 1))]}"
   fi
   if [ "${ar[$arg]}" == "--batch" ] || [ "${ar[$arg]}" == "-b" ]
   then
      BATCH="${ar[$(($arg + 1))]}"
   fi
done

if [ ! -d "/mnt/s3/$COPYTOFILE/weights/" ]; then
echo "Creating weight folder"
mkdir /mnt/s3/"$COPYTOFILE"/weights/
fi

cd inceptionv3/
sudo pip install -r requirements.txt >> install.log 

cd train/

echo "/mnt/s3/$COPYTOFILE/" 
python V3.py start-training --batch $BATCH --epoch $EPOCH 

cp -R ./weights /mnt/s3/"$COPYTOFILE"/weights



