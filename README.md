# TWCC Container Service Tutorial 
以下為兩個使用TWCC Container 的教學：
1. GPU Burn
2. AI Training

## Tutorial 1 -- GPU Burn
  在TWCC建立一個GPGPU容器，並且利用GPU Burn來測試GPU用量是否正常。
  
### Step 0. Preparation
1. 請先申請[iService帳號](https://iservice.nchc.org.tw/nchc_service/index.php)與可使用TWCC資源之計畫
2. 登入[TWCC](https://www.twcc.ai/)

### Step 1. Create Container
  1. 依user guide建立一個GPGPU container，Solution選擇**Tensorflow**。
  ![img](https://snag.gy/3mfqQB.jpg)
  
  2. Image建議選擇支援Python 3的版本，Hardware選擇一顆GPU的設定即可。
  ![img](https://snag.gy/h8R5k4.jpg)
  
  3. 建立container後，待狀態顯示ready，即已成功建立container。
  ![img](https://snag.gy/6obSIT.jpg)

### Step 2. Clone & Run GPU Burn

 1. 從container細節頁面點擊使用Jupyter terminal進入container(或以SSH連線進入)。
![image alt](https://snag.gy/2wV0Na.jpg)

    若欲以Jupyter terminal連線，點擊右側的New<font style="color:maroon;">①</font>與內部的Terminal<font style="color:maroon;">②</font>以開啟連線。
    ![img](https://snag.gy/adzsiX.jpg)
    若以SSH連線，請使用iService主機帳號與密碼登入。
 
 2. 輸入以下指令，從[NCHC_GitHub](https://github.com/TW-NCHC/AI-Services/tree/V3Training) 複製training程式到container。<br>
 `git clone https://github.com/TW-NCHC/AI-Services.git` 
 
 3. 輸入以下指令，進入**AI-Services**目錄。<br>
 `cd AI-Services` 
 
 4. 輸入以下指令，會將GPU_Burn程式下載下來並開始進行GPU。<br>
 `bash gpu_testing.sh` 
 
    完成後可在ternimal可看到如下圖訊息：
 ![img](https://snag.gy/5y8Lh4.jpg)
 

### Step 3. Terminate Container
  從TWCC的container列表可刪除container。

## Tutorial 2 -- AI Training
使用Tensorflow框架在TWCC建立一個GPGPU容器，並且掛載S3 bucket，以S3 tool將Cifar 10 dataset上傳至S3 bucket後，再從GitHub佈建程式進行training，結果再儲存於S3 bucket，以供外部存取。


### Step 0. Preparation
1. 請先申請[iService帳號](https://iservice.nchc.org.tw/nchc_service/index.php)與可使用TWCC資源之計畫
2. 登入[TWCC](https://www.twcc.ai/)
3. 下載S3 tool (S3儲存工具)，如[S3 browser](http://s3browser.com/) (for Windows)或[Cyberduck](https://cyberduck.io/) (for Linux)。

### Step 1. Download Cifar 10 datasets
- 從[Cifar 10](https://www.cs.toronto.edu/~kriz/cifar.html)下載dataset (CIFAR-10 python version)：
![img](https://snag.gy/doqAk4.jpg)

### Step 2. Upload the dataset to S3 Bucket with S3 tool

#### 2-1 先於TWCC確認欲使用之S3 bucket名稱
  - 如下圖所示，進入TWCC首頁後，點擊左上方**SERVICE**按鈕<font style="color:maroon;">①</font>，再點擊**S3 Cloud Storage**項目<font style="color:maroon;">②</font>，進入S3 Storage頁面。
  點擊左側**Bucket Management**項目<font style="color:maroon;">③</font>，確認欲使用之S3 bucket在列表中<font style="color:maroon;">④</font>。
  ![image alt](https://snag.gy/D0IYWQ.jpg)
  
#### 2-2 以工具程式上傳dataset
  - 執行S3 tool，依TWCC S3 Storage Overview提供之URL、Access Key與Secret Key連線，上傳資料(cifar-10-python.tar.gz)。
  ![img](https://snag.gy/14mWX5.jpg)
  
  - 上傳後，可在TWCC S3 bucket列表查看使用空間，或**Search Metadata**搜尋檔案確認上傳成功。
  ![img](https://snag.gy/r97i4I.jpg)
  ![img](https://snag.gy/PiR2rG.jpg)

### Step 3. Create Container & Mount Bucket
  - 依user guide建立一個GPGPU container，Solution選擇**Tensorflow**。
  ![img](https://snag.gy/3mfqQB.jpg)
  
  - Image建議選擇支援Python 3的版本，Hardware選擇一顆GPU的設定即可。
  ![img](https://snag.gy/h8R5k4.jpg)
  
  - Storage需掛載上傳dataset所使用的S3 bucket。
  p.s. 左側Storage選完已建立的S3 bucket後，需點右邊的加號才能完成掛載S3 bucket，完成結果將顯示在下方。
  ![img](https://snag.gy/L2QXkJ.jpg)
  
  - 建立container後，待狀態顯示ready，即已成功建立一個掛載S3 bucket的container。
  ![img](https://snag.gy/6obSIT.jpg)


### Step 4. AI Training

#### 4-1 準備training程式
 1. 從container細節頁面點擊使用Jupyter terminal或以SSH 連線進入container。連線後確認在工作目錄內(/workspace)。
![image alt](https://snag.gy/2wV0Na.jpg)

    若欲以Jupyter terminal連線，點擊右側的New<font style="color:maroon;">①</font>與內部的Terminal<font style="color:maroon;">②</font>以開啟連線。
    ![img](https://snag.gy/adzsiX.jpg)
    若以SSH連線，請使用iService主機帳號與密碼登入。
 
 2. 輸入以下指令，從[NCHC_GitHub](https://github.com/TW-NCHC/AI-Services/tree/V3Training) 複製training程式到container。<br>
 `git clone https://github.com/TW-NCHC/AI-Services.git` 
 
 3. 輸入以下指令，進入**AI-Services**目錄。<br>
 `cd AI-Services` 
 
 4. 輸入以下指令，在GPFS備好dataset。資料將從S3 bucket移至GPFS掛載路徑。<br>
 `bash V3_trainging.sh --path <your_S3_bucket_name>` 

 
    在ternimal可看到如下圖訊息，此訊息表示準備開始訓練模組：
 ![img](https://snag.gy/UtCw7b.jpg)
 
 5. 在training過程中，可在**MONITORING**頁面監控CPU/GPU、記憶體與網路使用狀況。
 ![img](https://snag.gy/d0pT7Z.jpg)
 
 6. Training結果將會存放於S3 bucket裡的weights資料夾，以供外部存取(如使用S3 browser)。


### Step 5. Terminate Container
  從TWCC的container列表可刪除container。
  若S3 bucket內的檔案不需保留，可利用S3 tool刪除檔案。
