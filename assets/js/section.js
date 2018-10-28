// Получаем весь блок элементов
var menuElem = document.getElementById('sweeties');
//у элэмента div берем первый элемент с классом title
var titleElem = menuElem.querySelector('.title1');

function name() {
  menuElem.classList.toggle('open');
};
// на p вешаем событие клика 
titleElem.addEventListener("click", name);