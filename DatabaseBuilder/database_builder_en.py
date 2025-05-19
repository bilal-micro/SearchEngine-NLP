import random
import csv

categories = [
    "Electronics", "Fashion", "Home & Kitchen", "Books", "Toys",
    "Sports", "Automotive", "Beauty", "Health", "Grocery"
]

brands = [
    "Samsung", "Apple", "Nike", "Sony", "Adidas", "HP", "Dell",
    "LG", "Lenovo", "Canon", "Philips", "Asus", "Panasonic", "Puma"
]

product_types = [
    "Laptop", "Smartphone", "Sneakers", "Headphones", "Camera", "Watch",
    "TV", "Tablet", "Backpack", "Mixer", "Book", "Toy Car", "T-shirt",
    "Perfume", "Supplements", "Chocolate", "Shampoo", "Football"
]

products = []
for i in range(1, 10001):
    category = random.choice(categories)
    brand = random.choice(brands)
    ptype = random.choice(product_types)
    name = f"{brand} {ptype} {random.randint(100, 999)}"
    price = round(random.uniform(10, 1500), 2)
    products.append([i, name, category, brand, price])

csv_path = "./products_20k_mixed.csv"
with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "category", "brand", "price"])
    writer.writerows(products)


categories_ar = [
    "إلكترونيات", "أزياء", "المنزل والمطبخ", "كتب", "ألعاب",
    "رياضة", "سيارات", "تجميل", "صحة", "بقالة"
]

brands_ar = [
    "سامسونج", "آبل", "نايكي", "سوني", "أديداس", "إتش بي", "ديل",
    "إل جي", "لينوفو", "كانون", "فيليبس", "أسوس", "باناسونيك", "بوما"
]

product_types_ar = [
    "لاب توب", "هاتف ذكي", "حذاء رياضي", "سماعات", "كاميرا", "ساعة",
    "تلفاز", "جهاز لوحي", "حقيبة", "خلاط", "كتاب", "سيارة لعبة", "قميص",
    "عطر", "مكملات غذائية", "شوكولاتة", "شامبو", "كرة قدم"
]

for i in range(10001, 20001):
    category = random.choice(categories_ar)
    brand = random.choice(brands_ar)
    ptype = random.choice(product_types_ar)
    name = f"{brand} {ptype} {random.randint(100, 999)}"
    price = round(random.uniform(10, 1500), 2)
    products.append([i, name, category, brand, price])

csv_path_ar = "./products_20k_mixed.csv"
with open(csv_path_ar, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "category", "brand", "price"])
    writer.writerows(products)

