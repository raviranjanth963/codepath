// ---------- 1. Get all the elements from the page ----------
var title = document.getElementById("title");
var sub = document.getElementById("sub");
var msg = document.getElementById("msg");
var goBtn = document.getElementById("go");

var tLogin = document.getElementById("tLogin");
var tSign = document.getElementById("tSign");

var loginBox = document.getElementById("loginBox");
var signinBox = document.getElementById("signinBox");

var usernameTab = document.getElementById("username-tab");
var phonenoTab = document.getElementById("phoneno-tab");
var byUser = document.getElementById("byUser");
var byPhone = document.getElementById("byPhone");

var emailTab = document.getElementById("email-tab");
var phoneTab = document.getElementById("phone-tab");
var sEmailW = document.getElementById("sEmailW");
var sPhoneW = document.getElementById("sPhoneW");

// ---------- 2. Variables to remember what is selected ----------
var mode = "login";      // "login" or "sign"
var loginType = "user";  // "user" or "phone"
var signType = "email";  // "email" or "phone"
var users = [];          // saved accounts (lost when page refreshes)

// ---------- 3. Small helper to show a message ----------
function showMessage(text, isGood) {
    msg.textContent = text;
    if (isGood) {
        msg.className = "ok";   // green
    } else {
        msg.className = "err";  // red
    }
}

// ---------- 4. Main tabs: Sign in / Create account ----------
tLogin.onclick = function () {
    mode = "login";
    loginBox.classList.remove("hide");
    signinBox.classList.add("hide");
    tLogin.classList.add("on");
    tSign.classList.remove("on");
    title.textContent = "Welcome back";
    sub.textContent = "Sign in to continue learning.";
    goBtn.textContent = "Sign in";
    showMessage("");
};

tSign.onclick = function () {
    mode = "sign";
    signinBox.classList.remove("hide");
    loginBox.classList.add("hide");
    tSign.classList.add("on");
    tLogin.classList.remove("on");
    title.textContent = "Create your account";
    sub.textContent = "First time here? Set up your login.";
    goBtn.textContent = "Create account";
    showMessage("");
};

// ---------- 5. Sign in: Username / Phone number ----------
usernameTab.onclick = function () {
    loginType = "user";
    byUser.classList.remove("hide");
    byPhone.classList.add("hide");
    usernameTab.classList.add("on");
    phonenoTab.classList.remove("on");
};

phonenoTab.onclick = function () {
    loginType = "phone";
    byPhone.classList.remove("hide");
    byUser.classList.add("hide");
    phonenoTab.classList.add("on");
    usernameTab.classList.remove("on");
};

// ---------- 6. Create account: Email / Phone number ----------
emailTab.onclick = function () {
    signType = "email";
    sEmailW.classList.remove("hide");
    sPhoneW.classList.add("hide");
    emailTab.classList.add("on");
    phoneTab.classList.remove("on");
};

phoneTab.onclick = function () {
    signType = "phone";
    sPhoneW.classList.remove("hide");
    sEmailW.classList.add("hide");
    phoneTab.classList.add("on");
    emailTab.classList.remove("on");
};

// ---------- 7. Show / Hide password buttons ----------
var eyeButtons = document.querySelectorAll("[data-eye]");

for (var i = 0; i < eyeButtons.length; i++) {
    eyeButtons[i].onclick = function () {
        var inputId = this.getAttribute("data-eye");   // example: "lp"
        var input = document.getElementById(inputId);

        if (input.type === "password") {
            input.type = "text";
            this.textContent = "Hide";
        } else {
            input.type = "password";
            this.textContent = "Show";
        }
    };
}

// ---------- 8. The big button (Sign in / Create account) ----------
goBtn.onclick = function () {

    if (mode === "sign") {
        // ----- CREATE ACCOUNT -----
        var contact = "";
        if (signType === "email") {
            contact = document.getElementById("le").value.trim();
        } else {
            contact = document.getElementById("sp").value.trim();
        }
        var username = document.getElementById("su").value.trim();
        var password = document.getElementById("sw").value;

        // check everything
        if (signType === "email" && contact.indexOf("@") === -1) {
            showMessage("Enter a valid email.");
            return;
        }
        if (signType === "phone" && contact.length < 7) {
            showMessage("Enter a valid phone number.");
            return;
        }
        if (username.length < 3) {
            showMessage("Username must be at least 3 characters.");
            return;
        }
        if (password.length < 8) {
            showMessage("Password must be at least 8 characters.");
            return;
        }

        // check if username already used
        for (var i = 0; i < users.length; i++) {
            if (users[i].username === username) {
                showMessage("That username is taken.");
                return;
            }
        }

        // save the new user
        users.push({ username: username, password: password, contact: contact });
        showMessage("Account created! Welcome, " + username + ".", true);

    } else {
        // ----- SIGN IN -----
        var id = "";
        var pass = "";
        if (loginType === "user") {
            id = document.getElementById("lu").value.trim();
            pass = document.getElementById("lp").value;
        } else {
            id = document.getElementById("lph").value.trim();
            pass = document.getElementById("lpp").value;
        }

        if (id === "" || pass === "") {
            showMessage("Please fill in all fields.");
            return;
        }

        // look for a matching user
        var found = false;
        for (var j = 0; j < users.length; j++) {
            var u = users[j];
            var idMatch = (loginType === "user") ? (u.username === id) : (u.contact === id);
            if (idMatch && u.password === pass) {
                found = true;
            }
        }

        if (found) {
            showMessage("Signed in. Welcome back!", true);
        } else {
            showMessage("No match found. New here? Create an account.");
        }
    }
};

// ---------- Continue with Google (practice) ----------
var googleBtn = document.getElementById("google");

googleBtn.onclick = function () {

    // 1. Ask the user for a Gmail address
    var email = prompt("Enter your Gmail address:");

    // 2. If the user pressed Cancel
    if (email === null) {
        return;
    }

    // 3. Check that it looks like a Gmail address
    if (email.indexOf("@gmail.com") === -1) {
        showMessage("Enter a valid Gmail address.");
        return;
    }

    // 4. Show the welcome message
    showMessage("Signed in with Google as " + email, true);
};