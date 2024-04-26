const bar = document.getElementById("bar");
const nav = document.getElementById("navbar");
const close = document.getElementById("close");
const search_result = document.getElementById("search-bar");
const dropdown_menu = document.getElementById("drpb");
const navCatalog = document.querySelector(".nav-catalog");
const dropdown_cat = document.getElementById("dropdown-cat");

// Mobile side bar opener
if (bar) {
  bar.addEventListener("click", () => {
    nav.classList.add("active-bar");
  });
}

if (close) {
  close.addEventListener("click", (event) => {
    nav.classList.remove("active-bar");
  });
}

// Search bar opener
if (search_result) {
  search_result.addEventListener("input", () => {
    dropdown_menu.style.display = "inline";
  });
}

document.addEventListener("click", (event) => {
  if (!dropdown_menu.contains(event.target) && event.target !== search_result) {
    dropdown_menu.style.display = "none";
  }
});



var MainImg = document.getElementById("main-image");
var SmallImg = document.getElementsByClassName("small-img");
// Realization of changing of images in row
for (let i = 0; i < SmallImg.length; i++) {
  SmallImg[i].onclick = function () {
    MainImg.src = SmallImg[i].src;
  };
}
function toggleIcon() {
  var icon = $(".nav-catalog i");
  icon.toggleClass("fa-chevron-down fa-chevron-up");
}

// Open modal box
document
  .getElementById("open-modal-btn").addEventListener("click", function (event) {
    document.getElementById("my-modal").classList.add("open");
  });

var innerLinks = document.querySelectorAll('.open-modal-btn');

innerLinks.forEach(function(link) {
  link.addEventListener('click', function(event) {
    event.preventDefault(); // Предотвращаем действие по умолчанию для внутренней ссылки
    event.stopPropagation(); // Предотвращаем всплытие события
    window.location.href = this.parentElement.href; // Переходим по адресу родительской ссылки
  });
});


// close modal
document
  .getElementById("close-my-modal-btn").addEventListener("click", function () {
    document.getElementById("my-modal").classList.remove("open");
  });

// close modal window with esc
window.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    document.getElementById("my-modal").classList.remove("open");
  }
});

// Close modal window with click outside of the box
document
  .querySelector("#my-modal .modal__box")
  .addEventListener("click", (event) => {
    event._isClickWithInModal = true;
  });
document.getElementById("my-modal").addEventListener("click", (event) => {
  if (event._isClickWithInModal) return;
  event.currentTarget.classList.remove("open");
});
