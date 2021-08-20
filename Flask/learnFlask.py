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


