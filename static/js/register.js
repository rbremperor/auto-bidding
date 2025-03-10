document.querySelector("form").addEventListener("submit", function(event) {
    event.preventDefault();  // Prevent default form submission

    fetch("{% url 'register' %}", {
        method: "POST",
        body: new FormData(this),
        headers: { "X-CSRFToken": "{{ csrf_token }}" }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = "{% url '' %}"; // Redirect after success
        } else {
            alert("Registration failed!");
        }
    });
});
