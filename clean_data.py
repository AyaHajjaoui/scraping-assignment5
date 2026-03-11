import pandas as pd

def clean_price(value):
    if pd.isna(value):
        return None
    value = str(value).replace("US $", "").replace(",", "").strip()
    if value == "" or value.upper() == "N/A":
        return None
    try:
        return float(value)
    except:
        return None

def clean_shipping(value):
    if pd.isna(value):
        return "Shipping info unavailable"
    value = str(value).strip()
    if value == "" or value.upper() == "N/A":
        return "Shipping info unavailable"
    return value

def main():
    df = pd.read_csv("ebay_tech_deals.csv", dtype=str)

    df["price"] = df["price"].apply(clean_price)
    df["original_price"] = df["original_price"].apply(clean_price)

    df["original_price"] = df.apply(
        lambda row: row["price"] if pd.isna(row["original_price"]) else row["original_price"],
        axis=1
    )

    df["shipping"] = df["shipping"].apply(clean_shipping)

    df["discount_percentage"] = (
        ((df["original_price"] - df["price"]) / df["original_price"]) * 100
    ).round(2)

    df.to_csv("cleaned_ebay_deals.csv", index=False, encoding="utf-8-sig")
    print("Cleaned data saved to cleaned_ebay_deals.csv")

if __name__ == "__main__":
    main()