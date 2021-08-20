// // import da,{x} from "./lib.js";
// // console.log(da,x);

// // 載入 css 樣式表
// import "./style.scss";

// {/* <div class="title"> Title</div>
// <ul>
//     <li>Css Loader</li>
//     <li>Sass Loader</li>
//     <li>Babel Loader</li>
// </ul>
// <h1>Hello</h1> */}

import title from "./title.js";
document.body.appendChild(title);

import list from "./list.js";
document.body.appendChild(list);

import "./style.scss";
import React from "react";
import ReactDOM from "react-dom";
// let app = React.createElement("div",{},"Hello World");
// let app = <div> Hello World </div>

class App extends React.Component{
    constructor(props){
        super(props);
    }
    render(){
        return<>
            <h3> DEMO </h3>
            <ul>
                <li>hi</li>
                <li>pig</li>
                <li>me</li>
            </ul>
        </>;
    }
}
ReactDOM.render(<App/>,document.getElementById("root"));