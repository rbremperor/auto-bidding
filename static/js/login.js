document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("loginForm");

    loginForm.addEventListener("submit", async function (e) {
        e.preventDefault();

        const username = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        try {
            const response = await fetch("/api/login/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ username, password })
            });

            if (response.ok) {
                const data = await response.json();
                localStorage.setItem("token", data.token); // Store token
                alert("Login successful!");
                window.location.href = "/plates/"; // Redirect to plates page
            } else {
                alert("Invalid username or password.");
            }
        } catch (error) {
            console.error("Error:", error);
            alert("Error logging in.");
        }
    });
});
