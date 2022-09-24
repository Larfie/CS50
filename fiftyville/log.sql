-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Checking the crime report of the robery by searching the crime reports from July 28, 2021 that took place on Humphrey Street
SELECT * FROM crime_scene_reports
WHERE year = 2021
AND month = 7
AND day =28
AND street = "Humphrey Street";

-- The report says that 3 witnesses were interviewed and the trascripts refer "bakery".
SELECT * FROM interviews
WHERE transcript LIKE "%bakery%";

-- One witness saw the thief leaving within ten minutes of the robbery
SELECT license_plate FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day= 28
AND hour = 10
AND minute >= 15
AND minute <= 25
AND activity = "exit";

-- Getting the id associated with the license plates leaving during that time period
SELECT id FROM people
WHERE license_plate IN
    (SELECT license_plate FROM bakery_security_logs
    WHERE year=2021
    AND month = 7
    AND day= 28
    AND hour = 10
    AND minute >=15
    AND minute <=25);

-- Another witness saw the thief withdrawing money from a ATM before the crime on Legget Street, so we get all account numbers that made withdrawals that day on that location
SELECT account_number FROM atm_transactions
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location = "Leggett Street"
AND transaction_type = "withdraw";

-- With the account numbers we check the ids of those people
SELECT person_id FROM bank_Accounts
WHERE account_number IN
    (SELECT account_number FROM atm_transactions
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND atm_location = "Leggett Street"
    AND transaction_type = "withdraw");

-- Another witness heard the thief calling someone after leaving the bakery
SELECT * FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60;

-- Checking the id of the people that made calls (callers) during that day with a duration less than a minute
SELECT id FROM people
WHERE phone_number IN
    (SELECT caller FROM phone_calls
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND duration < 60);

-- During that call, the witness heard the thief say that he was leaving Fiftyville the next day on the earliest flight, so we get that flight id
SELECT id FROM flights
WHERE year = 2021
AND month = 7
AND day=29
AND origin_airport_id =
    (SELECT id FROM airports
    WHERE city = "Fiftyville")
ORDER BY hour, minute ASC LIMIT 1;

-- We also can check the destination of that flight
SELECT city FROM airports
WHERE id =
    (SELECT destination_airport_id FROM flights
    WHERE id =
        (SELECT id FROM flights
        WHERE year = 2021
        AND month = 7
        AND day=29
        AND origin_airport_id =
            (SELECT id FROM airports
            WHERE city = "Fiftyville")
        ORDER BY hour, minute ASC LIMIT 1));

-- Checking the passport numbers of the passengers on that flight
SELECT passport_number FROM passengers
WHERE flight_id =
    (SELECT id FROM flights WHERE year = 2021
    AND month = 7
    AND day=29
    AND origin_airport_id =
        (SELECT id FROM airports
        WHERE city = "Fiftyville")
    ORDER BY hour, minute ASC LIMIT 1);

--Checking the ids associated with those passports
SELECT id FROM people WHERE passport_number IN
    (SELECT passport_number FROM passengers
    WHERE flight_id =
        (SELECT id FROM flights WHERE year = 2021
        AND month = 7
        AND day=29
        AND origin_airport_id =
            (SELECT id FROM airports
            WHERE city = "Fiftyville")
        ORDER BY hour, minute ASC LIMIT 1));

-- Now, after following the clues, we have 4 lists of suspects from differents sources (ids from people on flight, ids from license plates, ids from phone call and ids from bank account).
-- We can intersect this lists to check if anyone shows up in all of them. That person will be our thief.
-- The result of the following query is: BRUCE!!
SELECT name FROM people
WHERE id IN
    (SELECT id FROM people
    WHERE license_plate IN
        (SELECT license_plate FROM bakery_security_logs
        WHERE year=2021
        AND month = 7
        AND day= 28
        AND hour = 10
        AND minute >=15
        AND minute <=25)

    INTERSECT

    SELECT person_id FROM bank_Accounts
    WHERE account_number IN
        (SELECT account_number FROM atm_transactions
        WHERE year = 2021
        AND month = 7
        AND day = 28
        AND atm_location = "Leggett Street"
        AND transaction_type = "withdraw")

    INTERSECT

    SELECT id FROM people
    WHERE phone_number IN
        (SELECT caller FROM phone_calls
        WHERE year = 2021
        AND month = 7
        AND day = 28
        AND duration < 60)

    INTERSECT

    SELECT id FROM people WHERE passport_number IN
        (SELECT passport_number FROM passengers
        WHERE flight_id =
            (SELECT id FROM flights WHERE year = 2021
            AND month = 7
            AND day=29
            AND origin_airport_id =
                (SELECT id FROM airports
                WHERE city = "Fiftyville")
            ORDER BY hour, minute ASC LIMIT 1)));

-- Now to know who the accomplice is we can see the id of the receiver of the call made by the thief
-- First let's get thief phone number, then check the call made on the day of the robbery and check the receiver's phone number. Finally we get the name.
SELECT name FROM people
WHERE phone_number IN
    (SELECT receiver FROM phone_calls
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND duration < 60
    AND caller IN
        (SELECT phone_number FROM people
        WHERE id IN
            (SELECT id FROM people
            WHERE license_plate IN
                (SELECT license_plate FROM bakery_security_logs
                WHERE year=2021
                AND month = 7
                AND day= 28
                AND hour = 10
                AND minute >=15
                AND minute <=25)

            INTERSECT

            SELECT person_id FROM bank_Accounts
            WHERE account_number IN
                (SELECT account_number FROM atm_transactions
                WHERE year = 2021
                AND month = 7
                AND day = 28
                AND atm_location = "Leggett Street"
                AND transaction_type = "withdraw")

            INTERSECT

            SELECT id FROM people
            WHERE phone_number IN
                (SELECT caller FROM phone_calls
                WHERE year = 2021
                AND month = 7
                AND day = 28
                AND duration < 60)

            INTERSECT

            SELECT id FROM people WHERE passport_number IN
                (SELECT passport_number FROM passengers
                WHERE flight_id =
                    (SELECT id FROM flights WHERE year = 2021
                    AND month = 7
                    AND day=29
                    AND origin_airport_id =
                        (SELECT id FROM airports
                        WHERE city = "Fiftyville")
                    ORDER BY hour, minute ASC LIMIT 1)))));
