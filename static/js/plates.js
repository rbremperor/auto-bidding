async function loadPlates() {
    platesList.innerHTML = "<p>Loading...</p>";
    try {
        const response = await fetch("/home/plates/");  // API returns only the user's plates
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
