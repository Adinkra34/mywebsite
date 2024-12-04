from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
# Updated CORS configuration to allow requests from your frontend domain (empoliv.com)
CORS(app, resources={r"/*": {"origins": "https://empoliv.com"}})

# Initialize SQLite Database (for storing donor details)
def init_donations_db():
    conn = sqlite3.connect('donations.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS donors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Initialize partnerships database
def init_partnerships_db():
    conn = sqlite3.connect('partnerships.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS partnerships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            organization TEXT,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Route to receive donor details
@app.route('/donate', methods=['POST'])
def donate():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    if not name or not email or not phone:
        return jsonify({"error": "All fields are required."}), 400

    # Save the donor's data to the database
    try:
        conn = sqlite3.connect('donations.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO donors (name, email, phone) VALUES (?, ?, ?)', (name, email, phone))
        conn.commit()
        return jsonify({"message": "Thank you for your support!"}), 200

    except sqlite3.Error as e:
        print("Database error:", e)
        return jsonify({"error": "Database error occurred."}), 500

    finally:
        conn.close()

# Route to handle partnership requests
@app.route('/partnership', methods=['POST'])
def partnership():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    organization = data.get("organization")
    message = data.get("message")

    if not name or not email or not message:
        return jsonify({"error": "Name, email, and message are required."}), 400

    # Save partnership request to the database
    try:
        conn = sqlite3.connect('partnerships.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO partnerships (name, email, organization, message) VALUES (?, ?, ?, ?)',
                       (name, email, organization, message))
        conn.commit()
        return jsonify({"message": "Thank you for your partnership request!"}), 200

    except sqlite3.Error as e:
        print("Database error:", e)
        return jsonify({"error": "Database error occurred."}), 500

    finally:
        conn.close()

# Run initialization and start server
if __name__ == '__main__':
    init_donations_db()  # Initialize donations database
    init_partnerships_db()  # Initialize partnerships database
    app.run(debug=True)

