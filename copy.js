var buttons = document.querySelectorAll(".copy-btn");

for (var i = 0; i < buttons.length; i++) {
    buttons[i].onclick = function () {

        // find the code that is in the same box as this button
        var box = this.parentElement;
        var text = box.querySelector("code").textContent;

        navigator.clipboard.writeText(text);

        var btn = this;
        btn.textContent = "copied!";
        setTimeout(function () {
            btn.textContent = "copy";
        }, 2000);
    };
}