
-- 1. Total number of flights for each aircraft model

SELECT 
    aircraft_model, 
    COUNT(*) AS total_flights
FROM flights
GROUP BY aircraft_model;



-- 2. Aircraft assigned to more than 5 flights

SELECT 
    aircraft_reg, 
    aircraft_model, 
    COUNT(*) AS flight_count
FROM flights
GROUP BY aircraft_reg, aircraft_model
HAVING COUNT(*) > 5;



-- 3. Number of outbound flights for each airport (only >5)

SELECT 
    a.airport_name, 
    COUNT(f.flight_no) AS outbound_flights
FROM flights f
JOIN airport a ON f.origin = a.airport_code
GROUP BY a.airport_name
HAVING COUNT(f.flight_no) > 5;



-- 4. Top 3 destination airports by number of arrivals

SELECT 
    a.airport_name, 
    a.city, 
    COUNT(f.flight_no) AS arriving_flights
FROM flights f
JOIN airport a ON f.destination = a.airport_code
GROUP BY a.airport_name, a.city
ORDER BY COUNT(f.flight_no) DESC
LIMIT 3;



-- 5. Flight type: Domestic or International

SELECT 
    f.flight_no,
    f.origin,
    f.destination,
    CASE 
        WHEN a1.country = a2.country THEN 'Domestic'
        ELSE 'International'
    END AS flight_type
FROM flights f
JOIN airport a1 ON f.origin = a1.airport_code
JOIN airport a2 ON f.destination = a2.airport_code;



-- 6. 5 most recent arrivals at "DEL" airport

SELECT 
    f.flight_no,
    f.aircraft_model,
    a1.airport_name AS departure_airport,
    f.arrival_time
FROM flights f
JOIN airport a1 ON f.origin = a1.airport_code
WHERE f.destination = 'DEL'
ORDER BY f.arrival_time DESC
LIMIT 5;



-- 7. Airports with no arriving flights

SELECT 
    airport_name, 
    airport_code
FROM airport a
WHERE NOT EXISTS (
    SELECT 1 
    FROM flights f 
    WHERE f.destination = a.airport_code
);



-- 8. Number of flights by airline and status

SELECT 
    airline,
    SUM(CASE WHEN status = 'On Time' THEN 1 ELSE 0 END) AS on_time_count,
    SUM(CASE WHEN status = 'Delayed' THEN 1 ELSE 0 END) AS delayed_count,
    SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled_count
FROM flights
GROUP BY airline;



-- 9. All cancelled flights with airports and aircraft

SELECT 
    f.flight_no,
    f.aircraft_model,
    a1.airport_name AS origin_airport,
    a2.airport_name AS destination_airport,
    f.departure_time
FROM flights f
JOIN airport a1 ON f.origin = a1.airport_code
JOIN airport a2 ON f.destination = a2.airport_code
WHERE f.status = 'Cancelled'
ORDER BY f.departure_time DESC;



-- 10. City pairs with more than 2 different aircraft models

SELECT 
    f.origin,
    f.destination,
    COUNT(DISTINCT f.aircraft_model) AS aircraft_model_count
FROM flights f
GROUP BY f.origin, f.destination
HAVING COUNT(DISTINCT f.aircraft_model) > 2;



-- 11. % of delayed flights per destination airport

SELECT 
    f.destination,
    a.airport_name,
    ROUND(100.0 * SUM(CASE WHEN status='Delayed' THEN 1 ELSE 0 END)/COUNT(*), 2) AS delayed_percentage
FROM flights f
JOIN airport a ON f.destination = a.airport_code
GROUP BY f.destination, a.airport_name
ORDER BY delayed_percentage DESC;
