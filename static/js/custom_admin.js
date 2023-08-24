// custom_admin.js
document.addEventListener("DOMContentLoaded", function () {
    const menuIcon = document.querySelector(".menu-icon");
    const slidingMenu = document.querySelector(".sliding-menu");

    menuIcon.addEventListener("click", () => {
        slidingMenu.classList.toggle("open");
    });
});