let list = document.createElement("ul");
let item = document.createElement("li");
item.textContent="CSS Loader";
list.appendChild(item);

item = document.createElement("li");
item.textContent="Sass Loader";
list.appendChild(item);

item = document.createElement("li");
item.textContent="Babel Loader";
list.appendChild(item);

export default list;