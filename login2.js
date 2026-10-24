$
const $ = (id) => document.getElementById(id);

// Remember which page is selected.
let mode = "login";

// Remember which login method is selected.
let loginMethod = "user";
let signupMethod = "email";

// This function changes what appears on the screen.
function render() {
    const login = mode === "login";

    // Show login OR create account.
    $("loginBox").classList.toggle("hide", !login);
    $("signBox").classList.toggle("hide", login);

    // Change heading and subtitle.
    $("title").textContent = login
        ? "Welcome back"
        : "Create your account";

    $("wel2").textContent = login
        ? "Sign in to continue learning."
        : "Create your account to start learning.";

    // Change main button text.
    $("go").textContent = login
        ? "Sign in"
        : "Create account";

    // Show username OR phone login.
    $("byUser").classList.toggle(
        "hide", loginMethod !== "user"
    );

    $("byPhone").classList.toggle(
        "hide", loginMethod !== "phone"
    );

    // Show email OR phone registration.
    $("sEmailW").classList.toggle(
        "hide", signupMethod !== "email"
    );

    $("sPhoneW").classList.toggle(
        "hide", signupMethod !== "phone"
    );

    $("message").textContent = "";
}

// Sign in button.
$("signin-tab").onclick = function () {
    mode = "login";
    render();
};

// Create Account button.
$("signup-tab").onclick = function () {
    mode = "signup";
    render();
};

// Username button.
$("username-tab").onclick = function () {
    loginMethod = "user";
    render();
};

// Phone login button.
$("phoneno-tab").onclick = function () {
    loginMethod = "phone";
    render();
};

// Email registration button.
$("email-tab").onclick = function () {
    signupMethod = "email";
    render();
};

// Phone registration button.
$("phone-tab").onclick = function () {
    signupMethod = "phone";
    render();
};

// Show or hide passwords.
document.querySelectorAll("[data-eye]").forEach(
    function (button) {
        button.onclick = function () {
            const input = $(button.dataset.eye);

            if (input.type === "password") {
                input.type = "text";
                button.textContent = "Hide";
            } else {
                input.type = "password";
                button.textContent = "Show";
            }
        };
    }
);

// Check the form when the main button is clicked.
$("go").onclick = function () {
    if (mode === "login") {
        const username = loginMethod === "user"
            ? $("lu").value.trim()
            : $("lph").value.trim();

        const password = loginMethod === "user"
            ? $("lp").value
            : $("lpp").value;

        if (username === "" || password === "") {
            $("message").textContent =
                "Please enter your username/phone and password.";
        } else {
            $("message").textContent =
                "Fields filled! Real login needs a backend.";
        }
    } else {
        const contact = signupMethod === "email"
            ? $("le").value.trim()
            : $("sp").value.trim();

        const username = $("su").value.trim();
        const password = $("sw").value;

        if (!contact || !username || !password) {
            $("message").textContent =
                "Please fill in all fields.";
        } else {
            $("message").textContent =
                "Fields filled! Real registration needs a backend.";
        }
    }
};

// Display the first screen.
render();
