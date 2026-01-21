import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "aviation_data.db")

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS airport (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    airport_code TEXT,
    airport_name TEXT,
    city TEXT,
    country TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flight_no TEXT,
    airline TEXT,
    origin TEXT,
    destination TEXT,
    departure_time TEXT,
    arrival_time TEXT,
    aircraft_model TEXT,
    aircraft_reg TEXT,
    status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS airport_delays (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    airport_code TEXT,
    avg_delay_minutes INTEGER,
    delay_reason TEXT
)
""")

cursor.execute("DELETE FROM airport")
cursor.execute("DELETE FROM flights")
cursor.execute("DELETE FROM airport_delays")

cursor.executemany(
    "INSERT INTO airport (airport_code, airport_name, city, country) VALUES (?, ?, ?, ?)",
    [
        ("DEL", "Indira Gandhi International", "Delhi", "India"),
        ("HYD", "Rajiv Gandhi International", "Hyderabad", "India"),
        ("PNQ", "Pune Airport", "Pune", "India"),
        ("GOI", "Dabolim Airport", "Goa", "India"),
        ("AMD", "Sardar Vallabhbhai Patel International", "Ahmedabad", "India"),
        ("COK", "Cochin International Airport", "Kochi", "India"),
        ("MAA", "Chennai International Airport", "Chennai", "India"),
        ("CCU", "Netaji Subhas Chandra Bose Airport", "Kolkata", "India"),
        ("JFK", "John F Kennedy International", "New York", "USA"),
        ("LHR", "Heathrow", "London", "UK"),
        ("DXB", "Dubai International Airport", "Dubai", "UAE"),
        ("SIN", "Changi Airport", "Singapore", "Singapore")
    ]
)

cursor.executemany(
    "INSERT INTO flights (flight_no, airline, origin, destination, departure_time, arrival_time, aircraft_model, aircraft_reg, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
    [
        ("AI101", "Air India", "DEL", "JFK", "10:00", "15:30", "Boeing 777", "VT-AAA", "On Time"),
        ("BA202", "British Airways", "LHR", "JFK", "12:45", "18:00", "Airbus A320", "G-BAAA", "Delayed"),
        ("EK404", "Emirates", "DXB", "SIN","11:15", "17:15", "Boeing 777", "A6-AAA", "On Time"),
        ("SQ12", "Singapore Airlines", "SIN", "DEL","01:15", "05:35", "Airbus A350", "9V-SQA", "Cancelled"),
        ("SG301", "SpiceJet", "MAA", "CCU", "10:00", "15:30", "Boeing 737", "VT-SGA", "On Time"),
        ("SG302", "SpiceJet", "CCU", "MAA", "10:00", "15:30", "Boeing 737", "VT-SGB", "Delayed"),
        ("AI303", "Air India", "HYD", "PNQ", "10:00", "15:30", "Airbus A320", "VT-AAB", "On Time"),
        ("6E404", "IndiGo", "GOI", "AMD", "10:00", "15:30", "Airbus A320", "VT-6E4", "On Time"),
        ("AI505", "Air India", "COK", "DEL", "10:00", "15:30", "Boeing 777", "VT-AAC", "Delayed"),
        ("6E606", "IndiGo", "DEL", "COK", "10:00", "15:30", "Airbus A320", "VT-6E6", "Cancelled")
    ]
)


cursor.executemany(
    "INSERT INTO airport_delays (airport_code, avg_delay_minutes, delay_reason) VALUES (?, ?, ?)",
    [
        ("DEL", 20, "Weather"),
        ("JFK", 30, "Congestion"),
        ("LHR", 15, "Staffing"),
        ("DXB", 25, "Air Traffic"),
        ("SIN", 10, "Maintenance")
    ]
)

conn.commit()
conn.close()

print("Database created and sample data inserted successfully!")
