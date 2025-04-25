import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from dotenv import load_dotenv
import os

load_dotenv() 

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': os.getenv('DATABASE_URL')
})

ref = db.reference('Students/')

data = {
    "22U03076":
        {
            "absent":1,
            "attendance":{
                "2025-04-16":"absent",
            },
            "batch":"2026",
            "email":"pritam76@gmail.com",
            "holiday":0,
            "last_attendace_time":"2025-04-15 19:06:36",
            "major":"IT",
            "name": "Pritam Goyal",
            "present":0,
            "profile_image":"https://ik.imagekit.io/yektos0qe/students/22U03076.jpg",
            "total_attendance":0,
            "uid":"adj"
        },
        "22U03065":
        {
            "absent":1,
            "attendance":{
                "2025-04-16":"absent",
            },
            "batch":"2026",
            "email":"rustam65@gmail.com",
            "holiday":0,
            "last_attendace_time":"2025-04-15 19:06:36",
            "major":"IT",
            "name": "Rustam",
            "present":0,
            "profile_image":"https://ik.imagekit.io/yektos0qe/students/22U03065.jpg",
            "total_attendance":0,
            "uid":"adj"
        },
        "22U03004":
        {
            "absent":1,
            "attendance":{
                "2025-04-16":"absent",
            },
            "batch":"2026",
            "email":"deepak04@gmail.com",
            "holiday":0,
            "last_attendace_time":"2025-04-15 19:06:36",
            "major":"IT",
            "name": "Deepak Narve",
            "present":0,
            "profile_image":"https://ik.imagekit.io/yektos0qe/students/22U03004.jpg",
            "total_attendance":0,
            "uid":"adj"
        },
        "22U03055":
        {
            "absent":1,
            "attendance":{
                "2025-04-16":"absent",
            },
            "batch":"2026",
            "email":"nilogrib55@gmail.com",
            "holiday":0,
            "last_attendace_time":"2025-04-15 19:06:36",
            "major":"IT",
            "name": "Nilogrib Ghosh",
            "present":0,
            "profile_image":"https://ik.imagekit.io/yektos0qe/students/22U03055.jpg",
            "total_attendance":0,
            "uid":"adj"
        },
}

for key, value in data.items():
    ref.child(key).set(value)