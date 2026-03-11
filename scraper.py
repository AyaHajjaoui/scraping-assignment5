from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os
import time
from datetime import datetime


def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def scroll_page(driver, pause_time=2):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def safe_text(element, selector, default="N/A"):
    try:
        return element.find_element(By.CSS_SELECTOR, selector).text.strip()
    except:
        return default


def safe_attr(element, selector, attr, default="N/A"):
    try:
        return element.find_element(By.CSS_SELECTOR, selector).get_attribute(attr)
    except:
        return default


def scrape_ebay_tech_deals():
    url = "https://www.ebay.com/globaldeals/tech"
    driver = setup_driver()
    driver.get(url)
    time.sleep(5)

    scroll_page(driver, pause_time=2)

    products = driver.find_elements(By.CSS_SELECTOR, "div.dne-itemtile")
    rows = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for product in products:
        title = safe_text(product, ".dne-itemtile-title span")
        price = safe_text(product, ".dne-itemtile-price .first")
        original_price = safe_text(product, ".dne-itemtile-original-price")
        shipping = safe_text(product, ".dne-itemtile-delivery")
        item_url = safe_attr(product, "a.dne-itemtile-detail", "href")

        rows.append({
            "timestamp": timestamp,
            "title": title,
            "price": price,
            "original_price": original_price,
            "shipping": shipping,
            "item_url": item_url
        })

    driver.quit()

    df = pd.DataFrame(rows)

    file_name = "ebay_tech_deals.csv"

    if os.path.exists(file_name):
        df.to_csv(file_name, mode="a", header=False, index=False, encoding="utf-8-sig")
    else:
        df.to_csv(file_name, index=False, encoding="utf-8-sig")

    print(f"Scraped {len(df)} products and saved to {file_name}")


if __name__ == "__main__":
    scrape_ebay_tech_deals()