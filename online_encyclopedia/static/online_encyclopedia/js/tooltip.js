document.addEventListener("DOMContentLoaded", function () {
    let tooltip = document.getElementById("tooltip");

    document.body.addEventListener("mouseover", function (event) {
        let target = event.target.closest("a.encyclopedia-term");
        if (!target) return;

        let termSlug = target.getAttribute("href").split("/").slice(-2, -1)[0];

        fetch(`/online_encyclopedia/get-term-definition/${termSlug}/`)
            .then(response => response.json())
            .then(data => {
                tooltip.innerHTML = data.definition;
                tooltip.style.display = "block";
                tooltip.style.opacity = "1";
            });

        document.body.addEventListener("mousemove", function (event) {
            tooltip.style.left = event.pageX + 15 + "px";  // მარჯვენა მხარეს გადატანა
            tooltip.style.top = event.pageY + 15 + "px";   // ქვემოთ ოდნავ ჩამოწევა
        });
    });

    document.body.addEventListener("mouseout", function (event) {
        if (event.target.classList.contains("encyclopedia-term")) {
            tooltip.style.opacity = "0";
            setTimeout(() => {
                tooltip.style.display = "none";
            }, 200);
        }
    });
});
