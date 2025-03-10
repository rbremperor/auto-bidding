document.addEventListener("DOMContentLoaded", function () {
    const plateForm = document.getElementById("plateForm");
    const platesList = document.getElementById("platesList");

    // Function to Fetch and Display Plates
    async function loadPlates() {
        platesList.innerHTML = "<p>Loading...</p>";
        try {
            const response = await fetch("/api/plates/");
            const plates = await response.json();
            platesList.innerHTML = "";

            plates.forEach(plate => {
                platesList.innerHTML += `
                    <div class="col-md-4">
                        <div class="card">
                            <div class="card-body">
                                <h5 class="card-title">${plate.plate_number}</h5>
                                <p class="card-text">${plate.description}</p>
                                <p><strong>Deadline:</strong> ${plate.deadline}</p>
                                <p><strong>Highest Bid:</strong> ${plate.highest_bid ? plate.highest_bid : "No bids yet"}</p>
                            </div>
                        </div>
                    </div>
                `;
            });
        } catch (error) {
            platesList.innerHTML = "<p>Error loading plates.</p>";
            console.error("Error fetching plates:", error);
        }
    }

    // Handle New Plate Submission (Admin Only)
    if (plateForm) {
        plateForm.addEventListener("submit", async function (e) {
            e.preventDefault();

            const plate_number = document.getElementById("plate_number").value;
            const description = document.getElementById("description").value;
            const deadline = document.getElementById("deadline").value;

            const token = localStorage.getItem("token"); // Get auth token from local storage

            try {
                const response = await fetch("/api/plates/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Token ${token}`
                    },
                    body: JSON.stringify({ plate_number, description, deadline })
                });

                if (response.ok) {
                    alert("Plate added successfully!");
                    plateForm.reset();
                    loadPlates(); // Refresh list
                } else {
                    alert("Error adding plate.");
                }
            } catch (error) {
                console.error("Error:", error);
                alert("Error adding plate.");
            }
        });
    }

    // Load plates on page load
    loadPlates();
});
