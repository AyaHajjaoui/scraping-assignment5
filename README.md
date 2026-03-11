# COSC 482 – Lab Assignment 5

## Scraping, Cleaning, and Analyzing eBay Tech Deals

### Project Overview

In this project, I built a small data pipeline that collects technology deals from eBay and analyzes them. The goal was to practice web scraping, data cleaning, automation, and basic data analysis.

The system scrapes product information from the eBay Global Tech Deals page, stores the data in a dataset, cleans it, and then performs exploratory data analysis (EDA) to understand patterns such as pricing, discounts, and common product categories.

---

# Web Scraping

The scraping process is implemented in **`scraper.py`** using Selenium.

The script opens the eBay Global Tech Deals page, scrolls through the page to load all products, and extracts important information for each item such as:

* Timestamp (when the data was collected)
* Product title
* Discounted price
* Original price
* Shipping details
* Product link

The collected data is saved into a CSV file called **`ebay_tech_deals.csv`**.
Every time the scraper runs, new rows are added so the dataset grows over time.

---

# Automation with GitHub Actions

To continuously collect data, the scraper is automated using **GitHub Actions**.

The workflow runs the scraper **every 3 hours** using the cron schedule:

```
0 */3 * * *
```

This allows the dataset to capture changes in deals throughout the day and over multiple days.

---

# Data Cleaning

The raw scraped data can contain missing values or inconsistent formats, so a cleaning script called **`clean_data.py`** was created.

This script:

* Removes currency symbols and formatting from price columns
* Fills missing original prices when needed
* Standardizes missing shipping information
* Converts prices into numeric values
* Calculates a new column called **discount_percentage**

The cleaned dataset is saved as **`cleaned_ebay_deals.csv`**.

---

# Exploratory Data Analysis (EDA)

The notebook **`EDA.ipynb`** analyzes the cleaned dataset and visualizes important insights.

Some of the analyses include:

* **Deals per hour** to see when most deals appear
* **Price distribution** using histograms and boxplots
* **Discount percentage distribution**
* **Original price vs discounted price comparison**
* **Shipping option frequency**
* **Keyword analysis** of product titles (Apple, Samsung, Laptop, etc.)
* **Top 5 highest discounted deals**

These visualizations help understand how deals vary in price and discount levels.

---

# Key Findings

Some observations from the analysis include:

* Many products show significant discounts compared to their original prices.
* Some items do not include shipping information, which required cleaning.
* Certain product types such as phones, laptops, and tablets appear frequently in the listings.
* Discounts vary widely depending on the product category.

---

# Challenges

Few challenges appeared during the project:

* The webpage uses lazy loading, so scrolling was required to load all products.
* Some products did not have an original price listed.
* Shipping details were sometimes missing or inconsistent.
* Configuring GitHub Actions to run the scraper automatically required additional setup.
* Running the cleaning step automatically after each scraping cycle required extra workflow configuration.
---

# Possible Improvements

If the project were expanded, some improvements could include:

* Scraping multiple pages of deals instead of just one page
* Storing the data in a database instead of CSV files
* Performing more advanced text analysis on product titles
* Building a dashboard to visualize the data interactively

---

# Tools Used

* Python
* Selenium
* Pandas
* Matplotlib / Seaborn
* Jupyter Notebook
* GitHub Actions
