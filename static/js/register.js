document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent page reload

    const formData = new FormData(this);
    const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

    fetch(this.action, {
        method: "POST",
        body: formData,
        headers: { "X-CSRFToken": csrftoken }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = "/bids/"; // Redirect on success
        } else {
            alert("Registration failed! Check the errors.");
            console.log(data.errors); // Show errors in console
        }
    })
    .catch(error => console.error("Error:", error));
});
