document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript Loaded.");

    async function fetchPlates() {
        try {
            const response = await fetch("/api/plates/");
            const plates = await response.json();
            console.log(plates);
        } catch (error) {
            console.error("Error fetching plates:", error);
        }
    }

    fetchPlates();
});
