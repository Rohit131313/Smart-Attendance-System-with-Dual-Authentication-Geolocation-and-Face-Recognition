# @app.route("/run-encode-generator", methods=["GET"])
# def run_encode_generator():
#     """Runs EncodeGenerator.py dynamically."""
#     try:
#         print("🚀 Received request to execute EncodeGenerator.py")
#         sys.stdout.flush()  # Ensures logs appear immediately

#         result = subprocess.run(
#             [sys.executable, "EncodeGenerator.py"], 
#             capture_output=True, 
#             text=True,
#             timeout=30  # Timeout after 30 seconds
#         )

#         if result.returncode != 0:
#             return jsonify({
#                 "error": "EncodeGenerator script failed.",
#                 "stderr": result.stderr
#             }), 500

#         return jsonify({
#             "message": "EncodeGenerator script executed successfully.",
#             "output": result.stdout
#         }), 200

#     except Exception as e:
#         return jsonify({
#             "error": f"Failed to run EncodeGenerator: {str(e)}"
#         }), 500

# Admin API to edit attendance
# @app.route("/admin/edit-attendance", methods=["POST"])
# def edit_attendance():
#     data = request.json
#     student_id = data.get("student_id")
#     date = data.get("date")
#     status = data.get("status")  # "present", "absent", "holiday"
    
#     if not student_id or not date or not status:
#         return jsonify({"error": "Missing student_id, date, or status"}), 400
    
#     student_info = db.reference(f'Students/{student_id}').get()
#     if student_info:
#         prevstatus = student_info["attendance"].get(date, "not marked")
        
#         if prevstatus != "not marked":
#             # Decrement previous status count
#             prev_count = student_info.get(prevstatus, 0)
#             db.reference(f"Students/{student_id}/{prevstatus}").set(max(0, prev_count - 1))
    
#         # Increment new status count
#         new_count = student_info.get(status, 0)
#         db.reference(f"Students/{student_id}/{status}").set(new_count + 1)

#         db.reference(f"Students/{student_id}/attendance/{date}").set(status)
#     else:
#         return jsonify({"error":"student_id doesn't exist"}), 400
#     return jsonify({"message": "Attendance updated successfully"})

# @app.route("/getstudentattendance", methods=["POST"])
# def get_student_attendance():
#     data = request.get_json()
#     print("📩 Received data:", data)  # Debug line

#     student_id = data.get("student")
#     start_date = data.get("start")
#     end_date = data.get("end")

#     if not student_id or not start_date or not end_date:
#         return jsonify({"error": "Missing student ID, start date, or end date"}), 400

#     try:
#         start = datetime.strptime(start_date, "%Y-%m-%d")
#         end = datetime.strptime(end_date, "%Y-%m-%d")
#     except ValueError:
#         return jsonify({"error": "Invalid date format"}), 400

#     delta = (end - start).days + 1

#     ref = db.reference(f"Students/{student_id}")
#     student_data = ref.get()

#     if not student_data:
#         return jsonify({"error": "Student not found"}), 404

#     attendance = student_data.get("attendance", {})
#     result = {}

#     for i in range(delta):
#         current = start + timedelta(days=i)
#         date_str = current.strftime("%Y-%m-%d")
#         status = attendance.get(date_str, "not marked").lower()

#         if status == "present":
#             result[date_str] = 1
#         elif status == "absent":
#             result[date_str] = 0
#         elif status == "holiday":
#             result[date_str] = -1
#         else:
#             result[date_str] = -1

#     return jsonify(result)
