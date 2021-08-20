# 專案描述檔 package.json
npm init -y # NPM 的初始化(全部回答YES)

# 第三方套件
# 套件使用範圍 Scope：單一專案(在 node_module 中)、全域
# 套件的使用時機：執行階段使用套件 dependencies、開發階段使用套件 devDependencies
# 單一專案中的套件操作
npm install 套件名稱 --save # 安裝執行階段套件
npm install 套件名稱 --save-dev # 安裝開發階段套件
npm update 套件名稱
npm unistall 套件名稱
# 全域的專案操作
npm install 套件名稱 -g # global 套件
npm update 套件名稱 -g
npm unistall 套件名稱 -g

# Webpack 功能
# 核心：模組打包(支援程式模組化)
# 衍伸：專案建置(支援各種特殊與法的載入和編譯)
npm install webpack webpack-cli --save-dev #(後者可讓終端機執行webpack)
# 建立子資料夾 -src(專案程式) -dist(建置完成後的可執行程式碼)
# 在 package.json 的專案描述檔中的 script，定義 webpack 的建置命令 build
npm run build # 終端機執行 webpack 建置命令 

# webpack 設定檔：根目錄中建立 web.config.js
# webpack 核心設定
# 程式入口：指定原始碼中的主要程式檔案(檔案進入點)
# 程式輸出：指定建置後的可執行程式檔案
# 建置模式：開發模式(devlopment)、上線模式(production)

# module 模組
# 方法：透過 import 載入其他程式的資源或檔案
# 種類：可以載入 JS、CSS、image...
# 原生 JS 無法利用 export or import，利用 Webpack 得以解決
import "檔案程式路徑"
export{ variable1, variable2 }
export default variable
import{ variable1 } from "檔案程式路徑"
# mixed:
export{variable1 as default, variable2}
import variable1,{variable2} from "檔案程式路徑"

# Webpack 載入器
# 使用 import 載入模組時，實際用處理載入工作的程式
# 預設載入器：用來載 JS
# css 載入器：安裝 style-loader 與 css-loader 的相關套件
# sass 載入器：安裝 sass-loader 與 node-sass 的相關套件
# 在 webpack 設定檔中設定載入器套用規則
npm install style-loader css-loader --save-dev
npm install sass-loader node-sass --save-dev
# 在 config.js 模組載入規則：
module:{
    rules:[規則一,規則二]
}

# Webpack DevServer
# 好處：測試網站時，更接近實際運作環境/ 自動化建置、執行流程 /  建置專案的效率大大提升(in-memory)
npm install  webpack-dev-derver --save-dev
# 修改設定檔： 設定伺服器位置並添加腳本，寫 start

# 整合 Babel 編譯器
npm install react react-dom --save
# 上 BABEL 官網裝 babel




