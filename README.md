# COSC 482 – Lab Assignment 5

## Scraping, Cleaning, and Analyzing eBay Tech Deals

## Methodology

In this project, a small data pipeline was developed to collect and analyze technology deals from the eBay Global Tech Deals page.

First, a web scraper (`scraper.py`) was implemented using Selenium to extract product information including the timestamp, product title, discounted price, original price, shipping details, and the product URL. The scraped data is saved in a CSV file called `ebay_tech_deals.csv`.

To collect data continuously, GitHub Actions was used to automate the scraping process. The workflow runs the scraper every three hours using the cron expression `0 */3 * * *`, allowing the dataset to grow over time.

After collecting the raw data, a cleaning script (`clean_data.py`) processes the dataset by removing currency symbols, handling missing values, standardizing shipping information, converting price fields to numeric values, and calculating a new column called `discount_percentage`. The cleaned dataset is saved as `cleaned_ebay_deals.csv`.

Finally, exploratory data analysis was performed in `EDA.ipynb` using Python libraries such as Pandas, Matplotlib, and Seaborn to visualize patterns in the data.

## Key Findings

The exploratory data analysis revealed several insights:

* Many products offer noticeable discounts compared to their original prices.
* Some listings do not provide shipping information, requiring data cleaning and standardization.
* Certain product types such as phones, laptops, and tablets appear frequently in the listings.
* Discount percentages vary significantly between products.

## Challenges Faced

Several challenges were encountered during the project:

* The eBay page uses lazy loading, so scrolling was required to load all products before scraping.
* Some products did not include an original price, which required handling missing values during cleaning.
* Shipping information was sometimes missing or inconsistent.
* Configuring GitHub Actions to automate the scraper required additional setup and dependency management.
* Ensuring the cleaning script runs automatically after each scraping cycle required modifying the workflow configuration.

## Potential Improvements

If the project was extended, several improvements could be made:

* Scrape multiple pages of deals instead of a single page.
* Store the collected data in a database instead of CSV files.
* Perform more advanced text analysis on product titles to detect trends.
* Build an interactive dashboard to visualize deal trends and price changes over time.
