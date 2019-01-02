
# TWCC Container Service Tutorial 
本教學內容是使用tensorflow框架在TWCC建立一個GPGPU容器，並且掛載S3 bucket，以S3 tool將Cifar 10 dataset上傳至S3 bucket後，再從gitHub佈建程式進行training，結果再儲存於S3 bucket，以供外部存取。

## 事前準備
1. 請先申請iService帳號與可使用TWCC資源之計畫。
2. 存取S3 storage之工具程式，如S3 browser (for Windows)或Cyberduck (for Linux)。

## Step 1. Download Cifar 10 datasets
從[Cifar 10](https://www.cs.toronto.edu/~kriz/cifar.html)下載dataset。
![img](https://snag.gy/doqAk4.jpg)

## Step 2. Upload the dataset to S3 Bucket with S3 tool
### 2-1 先於TWCC確認欲使用之S3 bucket名稱
  如圖所示，進入TWCC首頁後，點擊右上方**SERVICE**按鈕<font style="color:maroon;">①</font>，再點擊**S3 Cloud Storage**項目<font style="color:maroon;">②</font>，進入S3 Storage頁面。
  點擊左側**Bucket Management**項目<font style="color:maroon;">③</font>，確認欲使用之S3 bucket在列表中<font style="color:maroon;">④</font>。
  ![image alt](https://snag.gy/D0IYWQ.jpg)
  
### 2-2 以工具程式上傳dataset
  執行工具程式，依TWCC S3 Storage Overview提供之URL、Access Key與Secret Key連線，上傳資料(cifar-10-python.tar.gz)。
  ![img](https://snag.gy/14mWX5.jpg)
  上傳後，可在TWCC S3 bucket列表查看使用空間，或**Search Metadata**搜尋檔案進行確認。
  ![img](https://snag.gy/r97i4I.jpg)
  ![img](https://snag.gy/PiR2rG.jpg)

## Step 3. Create Container & Mount Bucket
  依user guide建立一個container，Solution選擇**Tensorflow**，映像檔建議選擇支援Python 3的版本，硬體選擇一顆GPU的設定即可。
  ![img](https://snag.gy/3mfqQB.jpg)
  ![img](https://snag.gy/h8R5k4.jpg)
  
  另外要記得掛載上傳dataset所使用的S3 bucket。
  ![img](https://snag.gy/L2QXkJ.jpg)
  
  建立container後，待狀態顯示ready，即已成功建立一個掛載S3 bucket的container。
  ![img](https://snag.gy/6obSIT.jpg)


## Step 4. AI Training
### 4-1 準備training程式
 1. 從container細節頁面點擊使用Jupyter terminal或以SSH 連線進入container。
 ![image alt](https://snag.gy/2wV0Na.jpg)
 
 2. `git clone https://github.com/TW-NCHC/AI-Services.git` 從[NCHC_GitHub](https://github.com/TW-NCHC/AI-Services/tree/V3Training) 複製程式到container
 
 3. `cd AI-Services` 進入**AI-Services**目錄。
 
 4. `git checkout V3Training` 切換至V3Training branch。
 
 5. `bash step1.sh --path <your_S3_bucket_name>` 在GPFS備好dataset。資料將從S3 bucket移至GPFS掛載路徑。在ternimal可看到如下圖訊息。
 ![img](https://snag.gy/PXscav.jpg)
 
 6. `bash step2.sh --path <your_S3_bucket_name>` 開始training。在ternimal可看到如下圖訊息。
 ![img](https://snag.gy/UtCw7b.jpg)
 
 7. 在training過程中，可在**MONITORING**頁面監控CPU/GPU、記憶體與網路使用狀況。
 ![img]()
 
 8. Training結果將會存放於S3 bucket，以供外部存取。


## Step 5. Terminate Container
  從container列表可刪除container。
  若S3 bucket內的檔案不需保留，可利用S3 tool刪除檔案。
