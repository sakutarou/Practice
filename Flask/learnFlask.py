#  <!-- -*- coding: utf-8 -*- -->
# 網址 Web Address / URL
# 透過連線到特定網路服務的地址
# 網址的組成：通訊協定://主機名稱:埠號/路徑?要求字串
# 通訊協定 protocol: 透過後端以及網路環境決定使用 http 或 https
# 主機名稱 Hostname: 購買網域、設定 DNS 紀錄、應用 AWS 雲端服務決定主機名稱
# 埠號 Port: 透過後端程式或設定檔決定
# 路徑 Route: 透過後端程式或設定檔決定，決定網址路徑和處理函式的對應關係
# 要求字串 Request String: 透過後端程式決定


# 基本路由設定
# 透過函式的裝飾器來設定路由

# 靜態檔案處理 Static Files
# 不執行程式，直接將檔案送回前端 e.g. 圖檔、影片、HTML、CSS、JavaScript
# Flask 提供預設路徑處理
# 建立 static 資料夾
# 使用 static/檔案名稱 連線取得檔案
# 也可以自定路徑，在 application 物件中透過參數指定
Flask(__name__,static_folder="資料夾名稱",static_url_path="對應路徑")

# 請求物件 HTTP Request
# 前端主動發出請求給後端的伺服器，並且附帶上相關資訊
# 後端被動從前端接收請求，並取得附帶相關資訊
# 請求流程：前端發送請求 → flask 套件協助我們處理網路連線底層：
# 負責接收請求，並且將相關資訊封裝在 request 物件之中，根據路由決定怎麼處理請求

# 載入 request 物件
# 在路由對應的函式中，直接使用 request 取得物件
# 取得當前請求的各種基礎資訊:
# method 請求方法 / scheme 通訊協定 / host 主機名稱 / path 路徑 / url 完整網址
# Request Headers:
# 取得標頭(附加資訊)，user-agent/accept-language/referrer

# 要求字串的處理
# 格式： 參數名稱=資料&參數名稱=資料&...
# 前端送出：提供要求字串
# 要求字串中的參數值 = request.args.get("參數名稱",預設值)
# data = request.args.get("max",None)

# 回應方式 Reponse
# 直接回應字串
# 回應JSON格式的字串:透過 json.dumps()將 {}型態 的資料轉成 JSON 交出去
# 重新導向：使用 redirect(網址路徑)

# 樣版引擎 template engieen
# 網站後端回應給網站前端的一種方式，也就是 respone a template engieen
# 根據樣板檔案，產生字串，傳送到前端
# 方便撰寫複雜的前端程式、方便在回應中動態帶入資料
# 其檔案為純文字檔，並建立在 templates 的資料夾底下
# 使用上透過 render_template(檔案路徑) 來表示
# 定義動態資料欄位 {{資料欄位名稱}}
# render_template(檔案路徑,資料欄位名稱=資料)

# 前端發出 Request 請求，網站後端回應 html 程式碼
<form action="網址路徑">
    <input type="text" name="data"></input>
    <button> 點擊送出表單 </button>
</form>
#發出請求到 網址路徑?data=使用者輸入
@app.route("網址路徑")
def handle():
    input=request.args.get("data","") #後面的內容表示預設值
    return "給前端的回應"

# 連線方法 Method :GET、POST、PUT、DELETE、PATCH
# 網址：收件地址
# 方法：平信、限時
# 透過表單設定連線方法，不寫時預設 get
<form action="網址路徑" method="GET">
    <input type="text" name="data">
    <button>點擊送出表單</button>
</form>
# 使用 GET 方法，發出請求到 網址路徑?name=使用者輸入
@app.route("網址路徑",methods=["GET"])
def handle():
    input=request.args.get("data","")
    return 給前端的回應內容
# 使用 POST 方法，data=使用者輸入 的要求字串不會顯示在網址後面，而另外存放
@app.route("網址路徑",methods=["POST"])
def handle():
    input = request.form["data"]
    # input = request.form.get["data"]
    return 給前端的回應內容
# 前後端互動：直接輸入網址(GET)、超連結(GET)、表單(set GET or POST)


# 每次連線具有獨立性，因為 HTTP 屬於無狀態的通訊協定
# 管理使用者狀態可以解決這個問題，它可以記憶使用者對象
# 建立 session 保存使用者資料
name = request.args.get("name",None)
session["data"] = name
return "你好" + name
# 存入資料 session 中的 data
name = session["name"]
return name + "很高興認識你"