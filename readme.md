# python簡易爬蟲範例
含Docker化以及flask API

## 前置作業
如果要在本地開發，則電腦需要先安裝docker, python3，接著安裝python 虛擬環境
```
python -m pip install --user virtualenv
```

## 本地端
1. 先啟用selenium的image(如果電腦沒有，docker會自動幫你pull下來)
```
docker run --rm -d -v /dev/shm:/dev/shm  -p 4444:4444/tcp selenium/standalone-chrome
```
2. python 虛擬環境相關

備註: 如果已經安裝好虛擬環境，可以直接跳過以下步驟。
* 建立虛擬環境
```
python3 -m venv venv
```
* python 啟動虛擬環境，貼以下程式碼在cmd中並直接按Enter
```
# windows系統
.\venv\Scripts\activate.bat 

# mac系統
source ./venv/bin/activate 
```
* 進到虛擬機器之後，cmd的前面會多加一個(venv)的前綴，接著執行以下程式碼以進行安裝套件
```
pip3 install -r requirements.txt
```
* 以上設定完之後，就可以進行開發了

## Docker image
1. 將此專案clone下來之後，只要在cmd執行以下程式碼，就可以建立好docker 的 image檔
```
docker build -t python-web-crawler:1.1.0 .
```
2. 接著在此專案的資料夾底下，執行
```
docker-compose up -d
```
3. 開啟 http://localhost:5000 就可以看到網頁了
4. 補充說明: 可以修改docker-compose.yml中的 WEB_URI 這個參數，就可以修改爬蟲的網頁，例如以下範例(修改好之後，要重新進行第2步驟)
```
# ...
  - WEB_URI=https://tw.yahoo.com
```