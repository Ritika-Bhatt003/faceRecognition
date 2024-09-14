import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-1a621-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data= {
    "321654": {
        "name": "Ritika Bhatt",
        "major": "CS",
        "starting_year": 2022,
        "total_attendance": 6,
        "standing": "G",
        "year": 3,
        "last_attendance_time": "2024-09-07 00:54:34"
    },

    "852741": {
        "name": "Aditya Kirsali",
        "major": "Computer Science",
        "starting_year": 2022,
        "total_attendance": 3,
        "standing": "P",
        "year": 3,
        "last_attendance_time": "2024-09-07 00:54:34"
    },
    "202138": {
        "name": "5050",
        "major": "BISKUT",
        "starting_year": 2024,
        "total_attendance": 0,
        "standing": "G",
        "year": 1,
        "last_attendance_time": "2024-09-07 00:54:34"
    },
}

for key, value in data.items():
    ref.child(key).set(value)