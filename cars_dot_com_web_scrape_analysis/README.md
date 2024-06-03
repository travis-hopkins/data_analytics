# Cars.com Scraper

This repository contains a Python script that scrapes car information from Cars.com for various popular cities in the United States. The script collects data from the first 10 pages of each city's listings.

## Purpose

I created this project as part of my data analyst portfolio to demonstrate my web scraping skills and ability to collect and organize data from online sources.

## Usage

1. Clone the repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Run the `cars_scraper.py` script to start the scraping process.

## Locations Scraped

The script scrapes car listings from the following cities:

- Atlanta, GA
- Chicago, IL
- Columbus, OH
- Dallas, TX
- Denver, CO
- Houston, TX
- Los Angeles, CA
- New York, NY
- Philadelphia, PA
- Phoenix, AZ
- San Diego, CA
- Seattle, WA

The script retrieves data from the first 10 pages of each city's listings on Cars.com.

## Output

The script saves the scraped data to a CSV file named `cars_by_popular_city.csv`. The CSV file contains information about the cars, including their location, exterior color, interior color, drivetrain, MPG, fuel type, transmission, engine, mileage, status, year, brand, and model.

Feel free to explore the CSV file to analyze the collected car data.
