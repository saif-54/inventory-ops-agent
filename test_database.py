import sqlite3

db_path = "C:/Users/saifh/agent_workspace/abaya_inventory.db"

# Connect and create database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sku TEXT UNIQUE,
    name TEXT,
    fabric TEXT,
    stock INTEGER,
    cost REAL,
    price REAL
)
""")

# Insert sample abaya catalog
items = [
    ("ABY-001", "Classic Crepe Abaya", "Royal Crepe", 25, 450.0, 950.0),
    ("ABY-002", "Linen Summer Abaya", "Pure Linen", 4, 380.0, 850.0),
    ("ABY-003", "Silk Embroidered Kaftan", "Raw Silk", 12, 620.0, 1400.0)
]

cursor.executemany("""
INSERT OR REPLACE INTO products (sku, name, fabric, stock, cost, price)
VALUES (?, ?, ?, ?, ?, ?)
""", items)
conn.commit()

# Query 1: Fetch all items with projected revenue
print("\n--- Current Inventory & Margins ---")
cursor.execute("""
SELECT name, stock, price, (price - cost) AS profit_per_unit, (stock * (price - cost)) AS total_projected_profit
FROM products
""")
for row in cursor.fetchall():
    print(f"Product: {row[0]:<25} | Stock: {row[1]:<3} | Margin: {row[3]:<6.0f} EGP | Total Profit: {row[4]:<8.0f} EGP")

# Query 2: Low-stock alert (stock <= 5)
print("\n--- Low Stock Alert (Threshold <= 5) ---")
cursor.execute("SELECT name, stock FROM products WHERE stock <= 5")
for row in cursor.fetchall():
    print(f"[ALERT] Restock Needed: {row[0]} (Only {row[1]} units left!)")

conn.close()
print(f"\nDatabase successfully saved at: {db_path}\n")