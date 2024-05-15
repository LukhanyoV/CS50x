-- Keep a log of any SQL queries you execute as you solve the mystery.

-- check the tables in database and how they are structured
.schema

-- check crime scene for 28 July 2023 and street name is Humphrey Street
SELECT description FROM crime_scene_reports
WHERE year = 2023 AND month = 7 AND day = 28
AND street = 'Humphrey Street';

-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.
-- Littering took place at 16:36. No known witnesses

-- check the interview transcripts
SELECT transcript FROM interviews
WHERE year = 2023 AND month = 7 AND day = 28;

-- the thief was seen at the bakery parking lot
-- the thief was also seen earlier withdrawing some money from the ATM in Leggett Street
-- thief was heard in a call planning to take the earlierst flight out of fiftyville tomorrow (29 / July / 2023)
-- thief asked the other person in the call to get them the ticket

-- check bakery security logs
-- crime occured 10:15 am, within 10 minutes the thief left, cutoff 10:25
-- people who left between those times
SELECT name FROM people WHERE license_plate IN (
    -- find the people by their license plates
    SELECT license_plate FROM bakery_security_logs
    WHERE year = 2023 AND month = 7 AND day = 28
    AND hour = 10 AND minute >= 15 AND minute <= 25
    AND activity = 'exit'
);

-- check ATM transaction that day
-- the thief was seen withdrawing money
SELECT name FROM people
WHERE id IN (
    -- find the person_id of the thief
    SELECT person_id FROM bank_accounts
    WHERE account_number IN (
        -- find the thief's bank account
        SELECT account_number FROM atm_transactions
        WHERE year = 2023 AND month = 7 AND day = 28 AND
        atm_location = 'Leggett Street'
        AND transaction_type = 'withdraw'
    )
);

-- calls made on 28 / July / 2023
-- the call lastest less than a minute
SELECT name FROM people
WHERE phone_number IN (
    -- find the call by the thief
    SELECT caller FROM phone_calls
    WHERE year = 2023 AND month = 7 AND day = 28
    AND duration <= 60
);

-- flights booked for 29 / July / 2023
-- ealiest flight is at 08:20
SELECT name FROM people
WHERE passport_number IN (
    -- find people who will be on that flight
    SELECT passport_number FROM passengers
    WHERE flight_id IN (
        -- find the earliest flight
        SELECT id FROM flights
        WHERE year = 2023 AND month = 7 AND day = 29
        ORDER BY hour LIMIT 1
    )
);

-- FIND THE THIEF [Bruce]
-- find the intersection of all my queries to see who's name they have in common
SELECT name FROM people WHERE license_plate IN (
    SELECT license_plate FROM bakery_security_logs
    WHERE year = 2023 AND month = 7 AND day = 28
    AND hour = 10 AND minute >= 15 AND minute <= 25
    AND activity = 'exit'
)
INTERSECT
SELECT name FROM people
WHERE id IN (
    SELECT person_id FROM bank_accounts
    WHERE account_number IN (
        SELECT account_number FROM atm_transactions
        WHERE year = 2023 AND month = 7 AND day = 28
        AND atm_location = 'Leggett Street'
        AND transaction_type = 'withdraw'
    )
)
INTERSECT
SELECT name FROM people
WHERE phone_number IN (
    SELECT caller FROM phone_calls
    WHERE year = 2023 AND month = 7 AND day = 28
    AND duration <= 60
)
INTERSECT
SELECT name FROM people
WHERE passport_number IN (
    SELECT passport_number FROM passengers
    WHERE flight_id IN (
        SELECT id FROM flights
        WHERE year = 2023 AND month = 7 AND day = 29
        ORDER BY hour LIMIT 1
    )
);
-- FIND THE THIEF //

-- FIND THE ACCOMPLICE [Robin]
SELECT name FROM people
WHERE phone_number IN (
    SELECT receiver FROM phone_calls
    WHERE year = 2023 AND month = 7 AND day = 28
    AND duration <= 60
    AND caller = (
        SELECT phone_number FROM people
        WHERE name = 'Bruce'
    )
);
-- FIND THE ACCOMPLICE //

-- ESCAPED TO WHICH CITY [New York City]
SELECT city FROM airports
JOIN flights
ON airports.id = flights.destination_airport_id
WHERE year = 2023 AND month = 7 AND day = 29
ORDER BY hour LIMIT 1;
-- ESCAPED TO WHICH CITY //

