from product.models import Product
import csv


if Product.objects.count() == 0:
    with open("products_20k_mixed.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            if row:
                pid = row[0]
                name = row[1]
                category = row[2]
                brand = row[3]
                price = row[4]
                Product.objects.create(
                    id = pid,
                    title = name,
                    category = category,
                    brand = brand,
                    price = price
                )
