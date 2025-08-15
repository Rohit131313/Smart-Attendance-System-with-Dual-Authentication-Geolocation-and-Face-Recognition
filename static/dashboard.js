import { auth, database } from "./firebase-config.js";
import { ref, get } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-database.js";
import { signOut, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";
// ImageKit Base URL
import {imagekitBaseUrl} from "./imagekit-config.js"


console.log("🚀 Script Loaded");

// Authentication Check
onAuthStateChanged(auth, (user) => {
    console.log("🔍 Checking Auth State:", user);
    if (!user) {
        console.error("❌ No user logged in! Redirecting...");
        window.location.href = "login.html";
    }
});

// Get Scholar Number from Local Storage
const scholarNumber = localStorage.getItem("userScholarNumber");
console.log("📌 Scholar Number from localStorage:", scholarNumber);

if (!scholarNumber) {
    console.error("❌ No scholar number found in localStorage.");
    showAlert("No user logged in. Redirecting to login...", "error");
    setTimeout(() => window.location.href = "login.html", 2000);
} else {
    loadStudentData(scholarNumber);
}

// Function to load student data
async function loadStudentData(scholarNumber) {
    try {
        const studentRef = ref(database, "Students/" + scholarNumber);
        console.log("📂 Fetching data from:", "Students/" + scholarNumber);
        const snapshot = await get(studentRef);

        if (!snapshot.exists()) {
            console.error("❌ No data found for this user.");
            showAlert("No data found for this user.", "error");
            return;
        }

        const data = snapshot.val();
        console.log("✅ Fetched Student Data:", data);

        // Display student details
        document.getElementById("name").textContent = data.name;
        document.getElementById("scholarNumber").textContent = scholarNumber;
        document.getElementById("batch").textContent = data.batch;
        document.getElementById("major").textContent = data.major;
        document.getElementById("classes").textContent = data.present + data.absent;
        document.getElementById("totalAttendance").textContent = data.present;

        let total_days = data.present + data.absent
        let attendancePercentage = (data.present/ total_days)* 100
        document.getElementById("attendancepercentage").textContent = attendancePercentage.toFixed(2) + "%";

        const profileImage = document.getElementById("profileImage");
        profileImage.src = data.profile_image;

        // Handle Image Loading Errors
        profileImage.onerror = function () {
            console.error("❌ Failed to load image from:", imageUrl);
            profileImage.src = "default-profile.png"; // Fallback Image
        };

        // 🔔 Load and display attendance calendar
        if (data.attendance) {
            console.log(data.attendance)
            renderAttendanceCalendar(data.attendance,data.remarks);
        } else {
            console.warn("📭 No attendance data found.");
        }


    } catch (error) {
        console.error("❌ Error fetching student data:", error);
        showAlert("Error fetching data. Please try again.", "error");
    }
}


// Logout function
document.getElementById("logoutBtn").addEventListener("click", () => {
    signOut(auth)
        .then(() => {
            console.log("✅ Logout successful!");
            showAlert("Logout successful! Redirecting...", "success");
            // <button id="loginBtn" onclick="window.location.href='/login'">Login</button>
            setTimeout(() => {
                window.location.href = "/login";  // Redirect to Flask route
            }, 20000);

        })
        .catch(error => {
            console.error("❌ Error logging out:", error);
            showAlert("Error logging out. Please try again.", "error");
        });
});

// Function to show alerts
function showAlert(message, type) {
    const alertBox = document.getElementById("alertBox");
    alertBox.innerText = message;
    alertBox.className = `alert ${type}`;
    alertBox.style.display = "block";
    setTimeout(() => {
        alertBox.style.display = "none";
    }, 3000);
}

function renderAttendanceCalendar(attendanceData, remarkData = {}) {
    const events = [];

    console.log(remarkData)
    for (const [date, status] of Object.entries(attendanceData)) {
        let color;

        if (remarkData[date] && remarkData[date].trim() !== "") {
            color = "blue"; // Special color for dates with remarks
        } else {
            switch (status) {
                case "present":
                    color = "green";
                    break;
                case "absent":
                    color = "red";
                    break;
                case "leave":
                    color = "yellow";
                    break;
                default:
                    color = "gray";
            }
        }

        events.push({
            title: status.charAt(0).toUpperCase() + status.slice(1),
            start: date,
            color: color
        });
    }

    const calendarEl = document.getElementById("calendar");
    const calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: "dayGridMonth",
        events: events,
        height: "auto",   
        contentHeight: 350, // Set max height to compress
        aspectRatio: 2,  
        headerToolbar: {
            left: "prev,next",
            center: "title",
            right: ""
        }
    });

    calendar.render();

    renderRemarks(remarkData);
}

function renderRemarks(remarkData) {
    const remarksContainer = document.getElementById("remarksContainer");
    remarksContainer.innerHTML = ""; // Clear existing remarks

    const dates = Object.keys(remarkData).sort();

    if (dates.length === 0) {
        remarksContainer.innerHTML = "<p>No remarks available.</p>";
        return;
    }

    const ul = document.createElement("ul");
    for (const date of dates) {
        const remark = remarkData[date];
        if (remark && remark.trim() !== "") {
            const li = document.createElement("li");
            li.innerHTML = `<strong>${date}:</strong> ${remark}`;
            ul.appendChild(li);
        }
    }

    remarksContainer.appendChild(ul);
}

