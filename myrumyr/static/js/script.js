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


// Getting open-button collection for iteration
var modalBtns = document.getElementsByClassName("openModalBtn");

// Iterating through every modalButton and adding Event Listeners for each of them
for (var i = 0; i < modalBtns.length; i++) {
    modalBtns[i].onclick = function () {
        var productId = this.getAttribute("data-product-id");
        var modal = document.getElementById("productModal" + productId);
        modal.style.display = "block";

        //added listener to close modal window with ESC
        window.addEventListener('keydown', (e) => {
            if (e.key === "Escape") {
                modal.style.display = "none";
            }
        });
        // added Listener to close modal window if clicked aside
        // modal.addEventListener('click', event => {
        //     if (event._isClickWithInModal) return;
        //     modal.style.display = "none";
        // });
    }
}

// Getting close-button collection for iteration
var closeBtns = document.getElementsByClassName("close");

// Iterating through every modalButton and adding Event Listeners for each of them
for (var j = 0; j < closeBtns.length; j++) {
    closeBtns[j].onclick = function () {
        var productId = this.getAttribute("data-product-id");
        var modal = document.getElementById("productModal" + productId);
        modal.style.display = "none";
    }
}

