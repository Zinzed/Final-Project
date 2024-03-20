window.onload=function()
{
    const navElements = document.querySelector('.explore-link');
    const hamburger = document.querySelector('.hamburger');

    if (hamburger)
    {
        hamburger.addEventListener("click", () =>
        {
            navElements.classList.toggle("explore-link--open")
            hamburger.classList.toggle("hamburger--open");
        });
    }

    if (navElements)
    {
        navElements.addEventListener("click", () =>
        {
            navElements.classList.remove("explore-link--open")
            hamburger.classList.remove("hamburger--open");
        });
    }
}