document.addEventListener("DOMContentLoaded", () => {
    fetch("rank.txt")
        .then((response) => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.text();
        })
        .then((data) => {
            const lines = data.split("\n");
            const percentage = parseFloat(lines[1]);
            const imageUrl = lines[3];
            console.log("Percentage:", percentage);
            console.log("Image URL:", imageUrl);
            document.getElementById("line1").textContent = lines[0];
            document.getElementById("line2").textContent = lines[2] + "%";
            document.querySelector(".image").src = imageUrl;
            document.documentElement.style.setProperty("--percentage", `${percentage}%`);
        })
        .catch((error) => {
            console.error("Error fetching ", error);
        });
});
