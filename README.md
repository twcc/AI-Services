
# HowTO

## Step 1 : Download Cifar 10 datasets
**Download the Cifar 10 dataset from the [Cifar-10](https://www.cs.toronto.edu/~kriz/cifar.html)**
![image.png](https://snag.gy/RJL0ga.jpg)

## Step 2 : Upload the following data to S3 Bucket with S3 tool
**Log on to TWCC for S3 acceess and secret key, and use S3 browser(Window) or Cyberduck(linux) to login to S3 bucket and upload the tar file**

**To check if upload successful, go to TWCC website to see if the bucket exists and the size of the bucket.**
![image.png](https://snag.gy/AMfbJL.jpg)

## Step 3 : Create Container & Mount Bucket
**Create a new container and choose the correct bucket.**
**To check if the container is ready, please go to TWCC website to see if the container is ready.**
![image.png](https://snag.gy/WQ9zdx.jpg)

## Step 4 : Ready For Training
**1a. Git clone from [NCHC_GitHub](https://github.com/TW-NCHC/AI-Services/tree/V3Training)<br>
  1b. cd AI-Services**

**2. Change to V3Training Branch**

`git checkout V3Training`

**3. Execute step1.sh by enter your S3 bucket name and the end.<br>
`bash step1.sh --path your_bucket_name`<br>
     the data will move from S3 folder to GPSF. It should show the following messages.**
![image.png](https://snag.gy/oaNM6s.jpg)

**4. Execute step2.sh, if the terminal show the following messages then the training has begun.**
![image.png](https://snag.gy/vwuRYF.jpg)
