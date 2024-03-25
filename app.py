from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

# Dummy prayer times data
prayer_times = {
    "Fajr": "5:30 AM",
    "Dhuhr": "12:30 PM",
    "Asr": "3:45 PM",
    "Maghrib": "6:15 PM",
    "Isha": "8:00 PM"
}

@app.route('/prayer-times', methods=['GET'])
def get_prayer_times():
    return jsonify(prayer_times)

if __name__ == '__main__':
    app.run(debug=True)
