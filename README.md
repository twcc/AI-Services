# TWCC Container Service Tutorials
以下為使用TWCC Container 的教學：

[Preparation](#PREP)

[Tutorial 1 -- MNIST(手寫數字辨識資料集)](#MNIST)

[Tutorial 2 -- GPU Burn Testing](#GPUBURNING)

- 在TWCC建立一個GPGPU容器，並且利用GPU Burn來測試GPU用量是否正常。

[Tutorial 3 -- InceptionV3 Training](#V3TRAINING)

- 使用Tensorflow框架在TWCC建立一個GPGPU容器，並且掛載S3 bucket，以S3 tool將Cifar 10 dataset上傳至S3 bucket後，再從GitHub佈建程式進行training，結果再儲存於S3 bucket，以供外部存取。

[Tutorial 4 -- InceptionV3 Inference](#V3INFERENCE)


<h2 id = PREP>Preparation</h2>

### Step 1. 帳號與登入
1. 請先申請[iService帳號](https://iservice.nchc.org.tw/nchc_service/index.php)與可使用TWCC資源之計畫
2. 登入[TWCC](https://www.twcc.ai/)

### Step 2. Create Container

1. 依user guide建立一個GPGPU container，Solution選擇**Tensorflow**。<br>
![img](https://snag.gy/3mfqQB.jpg)
  
2. Image建議選擇支援Python 3的版本，Hardware選擇一顆GPU的設定即可。<br>
![img](https://snag.gy/h8R5k4.jpg)
  
3. **掛載S3 Bucket(Only for Tutorial 3)**

  - 如下圖所示，進入TWCC首頁後，點擊左上方**SERVICE**按鈕<font style="color:maroon;">①</font>，再點擊**S3 Cloud Storage**項目<font style="color:maroon;">②</font>，進入S3 Storage頁面。
  點擊左側**Bucket Management**項目<font style="color:maroon;">③</font>，確認欲使用之S3 bucket在列表中<font style="color:maroon;">④</font>。
  ![image alt](https://snag.gy/D0IYWQ.jpg)
  
  - Storage需掛載上傳dataset所使用的S3 bucket。
  p.s. 左側Storage選完已建立的S3 bucket後<font style="color:maroon;">①</font>，需點右邊的加號才能完成掛載S3 bucket<font style="color:maroon;">②</font>，完成結果將顯示在下方<font style="color:maroon;">③</font>。
  ![img](https://snag.gy/po81zv.jpg)
  
  - 下載S3 tool (S3儲存工具)，如[S3 browser](http://s3browser.com/) (for Windows)或[Cyberduck](https://cyberduck.io/) (for Linux)。
  

4. 建立container後，待狀態顯示ready，即已成功建立container。<br>
![img](https://snag.gy/6obSIT.jpg)


### Step 3. Clone Git
1. 從Container細節頁面點擊使用Jupyter terminal進入container(或以SSH連線進入)。
![image alt](https://snag.gy/2wV0Na.jpg)

    若欲以Jupyter terminal連線，點擊右側的New<font style="color:maroon;">①</font>與內部的Terminal<font style="color:maroon;">②</font>以開啟連線。
    ![img](https://snag.gy/adzsiX.jpg)
    若以SSH連線，請使用iService主機帳號與密碼登入。
2. 輸入以下指令，將[NCHC_GitHub](https://github.com/TW-NCHC/AI-Services/tree/V3Training) training程式複製到container。<br>
 `git clone https://github.com/TW-NCHC/AI-Services.git`


<h2 id = MNIST>Tutorial 1 -- MNIST</h2>
在TWCC建立一個GPGPU容器，並使用Jupyter Notebook進行MNIST(手寫數字辨識資料集)的AI訓練。

### Step 1. Start & Run Jupyter Notebook
1. 回到Container細節頁面並連線到Jupyter Notebook<br>
![image alt](https://snag.gy/lPLJIM.jpg)

2. 點進AI-Services/Tutorial_One，點擊右側的New再點選內部的Python3以開啟notebook。<br>
![image alt](https://snag.gy/XhZaWM.jpg)

3. 開啟Notebook後請將原目錄底下的Keras_MNIST.txt內的程式碼複製到Notebook內<br>
![image alt](https://snag.gy/tmYpXB.jpg)

4. 將程式碼複製完後，點選Run按鈕即可開始訓練<br>
![image alt](https://snag.gy/8UTEwJ.jpg)<br>
訓練的結果會顯示在程式下方<br>
![image alt](https://snag.gy/fGgMH8.jpg)<br>

---------------------------------------------
<h2 id = GPUBURNING>Tutorial 2 -- GPU Burn Testing</h2>

### Step 1. Clone & Run GPU Burn
1. 從container細節頁面點擊使用Jupyter terminal或以SSH 連線進入container。
![image alt](https://snag.gy/2wV0Na.jpg)

    若欲以Jupyter terminal連線，點擊右側的New<font style="color:maroon;">①</font>與內部的Terminal<font style="color:maroon;">②</font>以開啟連線。
    ![img](https://snag.gy/adzsiX.jpg)
    若以SSH連線，請使用iService主機帳號與密碼登入。 

2. 輸入以下指令，進入**Tutorial_Two**目錄。<br>
 `cd AI-Services/Tutorial_Two` 
 
3. 輸入以下指令，會將GPU_Burn程式下載下來並開始進行GPU。<br>
 `bash gpu_testing.sh` 
 
4. 當看到以下訊息表示已測試完畢<br>
![image alt](https://snag.gy/l3Q6m7.jpg)

---------------------------------------------
<h2 id = V3TRAINING>Tutorial 3 -- InceptionV3 Training</h2>

### Step 1. Download Cifar 10 datasets
1. 從[Cifar 10](https://www.cs.toronto.edu/~kriz/cifar.html)下載dataset (CIFAR-10 python version)：
![img](https://snag.gy/doqAk4.jpg)

### Step 2. Upload the dataset to S3 Bucket with S3 tool
  - 執行S3 tool，依TWCC S3 Storage Overview提供之URL、Access Key與Secret Key連線，上傳資料(cifar-10-python.tar.gz)。
  ![img](https://snag.gy/14mWX5.jpg)
  
  - 上傳後，可在TWCC S3 bucket列表查看已使用的空間是否因資料上傳而增加，或**Search Metadata**搜尋檔案確認上傳成功。
  ![img](https://snag.gy/r97i4I.jpg)
  ![img](https://snag.gy/PiR2rG.jpg)
  
### Step 3. AI Training

#### 3-1 準備training程式
 1. 從container細節頁面點擊使用Jupyter terminal或以SSH 連線進入container。
![image alt](https://snag.gy/2wV0Na.jpg)

    若欲以Jupyter terminal連線，點擊右側的New<font style="color:maroon;">①</font>與內部的Terminal<font style="color:maroon;">②</font>以開啟連線。
    ![img](https://snag.gy/adzsiX.jpg)
    若以SSH連線，請使用iService主機帳號與密碼登入。 
 
 2. 輸入以下指令，進入**Tutorial_Three**目錄。<br>
 `cd AI-Services/Tutorial_Three` 
 
 3. 輸入以下指令，在GPFS備好dataset。資料將從S3 bucket移至GPFS掛載路徑且準備進行訓練。<br>
 `bash V3_trainging.sh --path <your_S3_bucket_name>` 

 
    在ternimal可看到如下圖訊息，此訊息表示準備開始訓練模組：
 ![img](https://snag.gy/UtCw7b.jpg)
 
 5. 在training過程中，可在**MONITORING**頁面監控CPU/GPU、記憶體與網路使用狀況。
 ![img](https://snag.gy/d0pT7Z.jpg)
 
 6. Training結果將會存放於S3 bucket裡的weights資料夾(如下圖S3 browser所示)供外部存取。
 ![img](https://snag.gy/c9yaDs.jpg)



### Step 4. Terminate Container
  從TWCC的container列表可刪除container。
  若S3 bucket內的檔案不需保留，可利用S3 tool刪除檔案。


---------------------------------------------
<h2 id = V3INFERENCE>Tutorial 4 -- InceptionV3 Inference</h2>
