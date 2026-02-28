import re
import json

with open("raw.txt", "r", encoding="utf-8") as f:
    text = f.read()

def normalize_price(price):
    price = price.replace(" ", "").replace(",", ".")
    return float(price)

product_pattern = re.findall(
    r"\d+\.\s*\n(.+?)\n\s*\d+,\d+\s*x\s*([\d\s,]+)",
    text,
    re.DOTALL
)

products = []
prices = []

for name, price in product_pattern:
    clean_name = " ".join(name.split())
    value = normalize_price(price)
    products.append({
        "name": clean_name,
        "price_per_item": value
    })
    prices.append(value)

total_match = re.search(r"ИТОГО:\s*([\d\s,]+)", text)
total_amount = normalize_price(total_match.group(1)) if total_match else 0

payment_match = re.search(r"(Банковская карта|Наличные)", text)
payment_method = payment_match.group(1) if payment_match else "Unknown"

datetime_match = re.search(
    r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})",
    text
)

date = datetime_match.group(1) if datetime_match else ""
time = datetime_match.group(2) if datetime_match else ""

calculated_total = round(sum(prices), 2)

result = {
    "date": date,
    "time": time,
    "payment_method": payment_method,
    "total_from_receipt": total_amount,
    "calculated_total": calculated_total,
    "products": products
}

print(json.dumps(result, indent=4, ensure_ascii=False))