from flask import Flask # 載入 Flask
from flask import request # 載入請求物件

# 建立 Application 物件，可以設定靜態檔案的路徑
app = Flask(
    __name__,
    static_folder="static", # 靜態檔案的資料夾名稱，預設 static
    static_url_path="/" # 靜態檔案的對應路徑，預設 /static
) # 所有在 static 資料夾底下的資料都會對應到 "/" 路徑下的檔案名稱

# 動態路由
# 建立網站首頁的回應方式，路由設定(建立路徑 / 的對應處理函式)
@app.route("/") # 根目錄
def index(): # 用來回應路徑 / 連線的函式
    # print("請求方法", request.method)
    # print("通訊協定", request.scheme)
    # print("主機名稱", request.host)
    # print("路徑", request.path)
    # print("完整的網址", request.url)
    print("瀏覽器和作業系統",request.headers.get("user-agent"))
    print("語言偏好",request.headers.get("accept-language"))
    print("引薦網址",request.headers.get("referrer"))
    print("使用者IP",request.remote_addr)
    lang = request.headers.get("accept-language")
    if lang.startswith("en"):
        return "Hello Flask" # 回傳網站首頁的內容
    else:
        return "你好"

# 建立路徑 /data 的對應處理函式
@app.route("/data")
def getData():
    return "Get Data"

# 建立動態路由 /user/<使用者名稱> 的對應處理函式
@app.route("/user/<username>")
def handleUser(username):
    return "Hello "+ username

# 啟動網站伺服器，可透過 port 參數指定埠號
app.run(port=3000) # 預設5000
