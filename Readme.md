# 📚 Student Attendance Portal

A facial recognition-based attendance system with real-time database storage and a mobile-friendly admin/student dashboard.


## 🚀 How to Set Up and Run

### 1. Clone the Repository
```bash
git clone https://github.com/Rohit131313/Smart-Attendance-System-with-Dual-Authentication-Geolocation-and-Face-Recognition.git
cd Smart-Attendance-System-with-Dual-Authentication-Geolocation-and-Face-Recognition
```

---

### 2. Create and Activate a Conda Environment
```bash
conda create -n attendance-portal python=3.12
conda activate attendance-portal
```

---

### 3. Install Dlib
Download the appropriate `.whl` file for your Python version from [this link](https://github.com/z-mahmud22/Dlib_Windows_Python3.x).

Or install directly (for Python 3.12, Windows 64-bit):
```bash
python -m pip install dlib-19.24.99-cp312-cp312-win_amd64.whl
```

---

### 4. Install Project Requirements
```bash
pip install -r requirements.txt
```

---

### 5. Configure Firebase and ImageKit

- Use the `AddDatatoDatabase.py` file provided to populate your **Firebase Realtime Database**.
- The database should follow this format:

```json
{
  "Students": {
    "1": {
      "absent": 1,
      "attendance": {
        "2025-04-16": "absent"
      },
      "batch": "2026",
      "email": "a1@gmail.com",
      "holiday": 0,
      "last_attendace_time": "2025-04-16 09:06:36",
      "major": "IT",
      "name": "a",
      "present": 0,
      "profile_image": "imagekit_url_endpoint/students/1.jpg",
      "total_attendance": 0,
      "uid": "uid should be enter here"
    },
    "2": {
      "absent": 0,
      "attendance": {
        "2025-04-16": "present",
        "2025-04-17": "holiday"
      },
      "batch": "2026",
      "email": "b2@gmail.com",
      "holiday": 1,
      "last_attendace_time": "2025-04-17 09:06:36",
      "major": "IT",
      "name": "b",
      "present": 1,
      "profile_image": "imagekit_url_endpoint/students/2.jpg",
      "total_attendance": 0,
      "uid": "uid should be enter here"
    },
  }
}
```

- Enable **Firebase Authentication** and create users for each student. Store each student's UID inside the database.

- Upload each student’s image to **ImageKit** inside the `students/` folder.

- Update each student's `profile_image` URL in the database according to their uploaded ImageKit image.

---

### 6. Run the Server Locally
```bash
python app.py --host=0.0.0.0 --port=5000
```
Then open [http://localhost:5000](http://localhost:5000) on your **laptop browser**.

---

### 7. Access on Mobile (Better Location Accuracy)

- Open a second terminal.
- Activate the environment again:

```bash
conda activate attendance-portal
```

- Start **ngrok**:

```bash
ngrok http 5000
```

- Copy the generated **ngrok URL** (e.g., `https://randomid.ngrok-free.app`).

- Update `BASE_URL` in these files:
  - `templates/index.html`
  - `static/adminDashboard.js`

- Now open the **ngrok URL** on your mobile browser.

---
