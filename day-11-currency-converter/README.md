# Project 11: Currency Converter with Live Exchange Rates

## Project Overview

A command-line currency converter that fetches real-time exchange rate data from the ExchangeRate-API. Users can input a base currency, a target currency, and an amount to receive an accurate, up-to-date conversion. This project reinforces API consumption skills and introduces more complex data validation and error handling scenarios.

## What You'll Learn

-   **Consuming a different API**: Interacting with a new API endpoint and understanding its unique JSON structure.

-   **Handling API Errors**: Parsing API-specific error messages to provide better feedback to the user.

-   **Data Validation**: Ensuring user-provided currency codes and amounts are in a valid format.

-   **Code Organization**: Structuring the code logically to separate data fetching, user input, and calculation.

-   **Formatted Output**: Using f-strings to format numerical output for better readability (e.g., adding commas and decimal points).

## Features

-   **Live Data**: Uses a free API to get the most current exchange rates.

-   **Any-to-Any Conversion**: Supports conversion between any of the 160+ currencies offered by the API.

-   **Robust Error Handling**: Provides clear messages for invalid API keys, unrecognized currency codes, and network issues.

-   **User-Friendly Interface**: A simple, clean command-line interface that guides the user through the process.

-   **Continuous Use**: Allows for multiple conversions without needing to restart the application.

## Crucial Setup: API Key

This application requires a free API key from ExchangeRate-API to function.

1.  **Sign Up**: Go to the [ExchangeRate-API website](https://www.exchangerate-api.com/ "null") and sign up for the "Free Plan".

2.  **Get API Key**: Once you've confirmed your email and logged in, your API key will be available on your dashboard.

3.  **Add Key to Code**: Open the `currency_converter.py` file and replace the placeholder text `"YOUR_API_KEY_HERE"` with the key you just copied.

## How to Run

1.  **Install Dependencies**: Make sure you have the `requests` library installed.

    ```
    pip install -r requirements.txt

    ```

2.  **Run the Script**:

    ```
    python currency_converter.py

    ```

Sample Output
-------------

```
==========================================
  💱 Live Currency Converter 💱
==========================================
Enter the base currency (e.g., USD, EUR, JPY): USD
Enter the target currency (e.g., USD, EUR, JPY): INR
Enter the amount in USD: 50

Fetching exchange rates for USD...

------------------------------------------
           ✅ CONVERSION RESULT ✅
------------------------------------------
  50.00 USD is equal to
  4,175.50 INR
------------------------------------------

Perform another conversion? (y/n): n

Thank you for using the Currency Converter! 👋

```

Code Structure
--------------

-   `currency_converter.py`: The main application script.

-   `get_exchange_rates()`: Fetches the latest conversion rates for a specified base currency and handles API errors.

-   `get_user_input()`: Prompts the user for the base currency, target currency, and amount, with validation.

-   `perform_conversion()`: Takes the user data and the retrieved rates to calculate the final amount.

-   `main()`: The primary function that controls the application's main loop.

Enhancements (Optional)
-----------------------

-   **GUI Interface**: Use a framework like Tkinter or PyQt5 to build a graphical user interface with dropdown menus for currencies.

-   **Offline Caching**: Save the last successful API response to a local file. If the API is unreachable, use the cached data (and notify the user that it's not live).

-   **Show Common Currencies**: On startup, display a list of popular currency codes (USD, EUR, GBP, JPY, INR) to help the user.

-   **Conversion History**: Keep a log of the last 5 conversions and display it to the user.

Time Estimate
-------------

**Beginner**: 90-120 minutes **With enhancements**: 4-7 hours

Key Concepts
------------

-   REST APIs and JSON

-   Error Handling (Network & API-specific)

-   Data Validation

-   Modular Function Design

-   User Interface (CLI)