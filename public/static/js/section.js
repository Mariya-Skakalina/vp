// Получаем весь блок элементов
let menuElem = document.getElementById('sweeties');
//у элэмента div берем первый элемент с классом title
let titleElem = menuElem.querySelector('.title1');

function name() {
  menuElem.classList.toggle('open');
};
// на p вешаем событие клика 
titleElem.addEventListener("click", name);
