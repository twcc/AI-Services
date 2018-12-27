for arg in "$@"
do 
   if [ "$arg" == "--path" ] || [ "$arg" == "-p" ]
   then
      COPYTOFILE="$2"
   fi
done
echo "Start Process"
tar -C /mnt/s3/"$COPYTOFILE"  -xvzf /mnt/s3/"$COPYTOFILE"/cifar-10-python.tar.gz

echo "Checking for folder"
if [ ! -d "~/.keras/datasets" ]; then
echo "Creating folder"
mkdir ~/.keras/datasets
fi
echo "Moving data to folder"
cp -R /mnt/s3/"$COPYTOFILE"/cifar-10-batches-py ~/.keras/datasets/
echo "Finished moving data"

