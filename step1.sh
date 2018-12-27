echo "Checking for folder"
if [ ! -d "~/.keras/datasets" ]; then
echo "Creating folder"
mkdir ~/.keras/datasets
fi
echo "Moving data to folder"
cp -R ~/lustre/cifar-10-batches-py ~/.keras/datasets/
echo "Finished moving data"

