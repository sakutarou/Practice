// tell webpack how to build the project
const path=require("path");
module.exports={
    // 建置模式，通常預設上線模式 production，但也可以改成開發模式 development
    mode:"development",
    // 入口
    entry:"./src/index.js",
    // 輸出
    output:{
        filename:"main.js", //輸出檔名
        path:path.resolve(__dirname,"dist") // 輸出路徑
    },
    // devServer 設定
    devServer:{
        contentBase:"./dist"
    },
    // 模組載入規則
    module:{
        rules:[
            // CSS 樣式表載入規則
            {
                test:/\.scss$/i, //當 import 時，檔案結尾是否是 .css (i：不計較大小寫)
                // 寫法 from 正規表示式
                use:["style-loader","css-loader","sass-loader"]
            },
            {
                test: /\.m?js$/,
                exclude: /node_modules/,
                use: {
                  loader: "babel-loader",
                  options: {
                    presets: ['@babel/preset-env']
                  }
                }
              }
        ]
    }
}