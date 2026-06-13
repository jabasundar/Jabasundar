# ✈️ Air Tracker: Flight Analytics

## Project Overview

Air Tracker: Flight Analytics is an end-to-end aviation data analytics project that collects, stores, analyzes, and visualizes flight-related information using the AeroDataBox API. The project extracts airport, flight, aircraft, and delay data from external APIs, transforms nested JSON responses into a structured relational database, and presents meaningful insights through an interactive Streamlit dashboard.

The application enables users to explore airport information, monitor flight operations, analyze delays, identify busy routes, and gain operational insights from aviation data. This project demonstrates practical skills in API integration, database design, SQL analytics, and dashboard development.

---

## Domain

Aviation Analytics / Data Analytics

---

## Skills Demonstrated

* Python Programming
* API Integration
* JSON Parsing and Data Transformation
* SQL Database Design
* Data Cleaning and Processing
* SQL Query Optimization
* Data Visualization
* Streamlit Dashboard Development
* Analytical Reporting
* Error Handling and Logging

---

## Problem Statement

The aviation industry generates large volumes of operational data every day. Airports, airlines, and analysts require effective tools to understand flight operations, airport performance, aircraft utilization, and delay patterns.

This project aims to build a comprehensive aviation analytics platform using AeroDataBox API data. The system extracts airport, flight, aircraft, and delay information, stores it in a relational database, performs analytical queries, and visualizes the results through an interactive dashboard for better decision-making.

---

## Business Use Cases

### Airport Exploration

Allows users to explore airport information including location, timezone, city, country, and flight activity.

### Flight Trend Analysis

Analyzes departures and arrivals by airline, status, airport, and operational timelines.

### Operational Insights

Provides delay statistics, flight status monitoring, and airport performance analysis.

### Decision Support

Supports airport managers, analysts, and travel planners with data-driven insights for scheduling and resource planning.

---

## Project Architecture

AeroDataBox API

↓

Data Extraction Scripts

↓

JSON Parsing & Transformation

↓

SQL Database Storage

↓

SQL Analysis Queries

↓

Streamlit Dashboard

↓

Interactive Aviation Insights

---

## Data Collection Process

### Step 1: Airport Data Extraction

Selected multiple airport IATA codes and fetched airport information using AeroDataBox Airport API endpoints.

### Step 2: Flight Data Collection

Collected arrival and departure flight information for the selected airports.

### Step 3: Aircraft Data Collection

Extracted unique aircraft registrations from flight records and retrieved aircraft details using Aircraft API endpoints.

### Step 4: Delay Statistics Collection

Retrieved airport delay statistics using AeroDataBox statistical endpoints.

### Step 5: Database Storage

Transformed JSON responses into structured relational tables and stored them in the database.

---

## Database Schema

### Airport Table

Stores airport master information including:

* ICAO Code
* IATA Code
* Airport Name
* City
* Country
* Continent
* Latitude
* Longitude
* Timezone

### Aircraft Table

Stores aircraft information including:

* Registration Number
* Model
* Manufacturer
* ICAO Type Code
* Owner

### Flights Table

Stores flight operational information including:

* Flight Number
* Aircraft Registration
* Origin Airport
* Destination Airport
* Scheduled Departure
* Actual Departure
* Scheduled Arrival
* Actual Arrival
* Flight Status
* Airline Code

### Airport Delays Table

Stores airport delay statistics including:

* Total Flights
* Delayed Flights
* Average Delay
* Median Delay
* Cancelled Flights

---

## SQL Queries Implemented

The project includes analytical SQL queries such as:

1. Total number of flights for each aircraft model.
2. Aircraft assigned to more than five flights.
3. Airports with more than five outbound flights.
4. Top destination airports by arrivals.
5. Domestic and international flight classification.
6. Most recent arrivals at selected airports.
7. Airports with no arriving flights.
8. Flight counts by airline and status.
9. Cancelled flight analysis.
10. Aircraft model usage between city pairs.
11. Delayed arrival percentages by destination airport.

All SQL queries are available in the `queries.sql` file.

---

## Streamlit Dashboard Features

### Dashboard Overview

Displays key performance indicators including:

* Total Airports
* Total Flights
* Total Aircraft
* Average Airport Delay

### Flight Search and Filtering

Users can:

* Search by Flight Number
* Search by Airline
* Filter by Flight Status
* Filter by Origin Airport
* Filter by Destination Airport
* Filter by Date Range

### Airport Explorer

Provides detailed airport information:

* Airport Name
* City
* Country
* Timezone
* Geographic Coordinates
* Associated Flight Activity

### Delay Analysis

Visualizations include:

* Average Delay by Airport
* Delay Percentage Analysis
* Airport Delay Rankings
* Cancelled Flight Statistics

### Route Analytics

Displays:

* Busiest Routes
* Most Active Airports
* Airline Performance Metrics
* Route Traffic Analysis

---

## Technologies Used

### Programming Language

* Python

### Database

* SQLite / MySQL

### API

* AeroDataBox API

### Dashboard

* Streamlit

### Libraries

* Pandas
* Requests
* SQLite3
* Plotly
* NumPy

---

## Project Structure

air-tracker-flight-analytics/

├── data/

│   ├── raw/

│   └── processed/

├── database/

│   ├── schema.sql

│   ├── queries.sql

│   └── aviation.db

├── scripts/

│   ├── extract_airports.py

│   ├── extract_flights.py

│   ├── extract_aircraft.py

│   ├── extract_delays.py

│   ├── load_database.py

│   └── utils.py

├── app.py

├── requirements.txt

├── README.md

└── .env

---

## Key Insights

* Major international airports handle significantly higher flight volumes.
* Certain routes consistently rank among the busiest connections.
* Flight delays are concentrated at specific airports.
* Airline operational performance varies considerably across routes.
* Delay analytics can assist in scheduling optimization and resource allocation.

---

## Challenges Faced

* Handling nested JSON structures from API responses.
* Managing API rate limits and request failures.
* Designing a normalized relational database schema.
* Processing incomplete or inconsistent flight records.
* Building efficient SQL queries for large datasets.
* Creating interactive and responsive Streamlit visualizations.

---

## Future Enhancements

* Real-time flight tracking.
* Weather-based delay prediction.
* Machine learning models for delay forecasting.
* Airline performance prediction.
* Advanced route optimization analytics.
* Cloud deployment and automated data refresh.

---

## Results

The project successfully demonstrates a complete aviation analytics workflow, from API-based data extraction to database storage, SQL analysis, and dashboard visualization. The Streamlit application enables users to explore airport networks, analyze flight operations, investigate delays, and gain actionable insights from aviation data.

---

## Conclusion

Air Tracker: Flight Analytics successfully integrates API data extraction, database management, SQL analytics, and interactive dashboard development into a single solution. The project provides meaningful aviation insights while demonstrating practical skills in Python programming, API integration, relational database design, SQL querying, and data visualization. It serves as a comprehensive example of building an end-to-end data analytics application for the aviation industry.

---

## Author

Jabasunder Samuel

AIML Program – Aviation Analytics Project

Built using Python, SQL, AeroDataBox API, and Streamlit.
