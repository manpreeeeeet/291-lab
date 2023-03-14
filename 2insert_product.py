from pymongo import MongoClient
import sys

# Setup and insert

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        sys.exit()

    port_name = int(sys.argv[1])
    print(f"connecting to port: {port_name}")

    client = MongoClient('localhost', port_name)

    db = client["cmput291db"]
    students = db["students"]
    products = db["products"]

    products.delete_many({})
    products.insert_many([
        {"pid": 101, "price": 120.0, "category": "B"},
        {"pid": 102, "price": 130.0, "category": "B"},
        {"pid": 103, "price": 140.0, "category": "B"},
        {"pid": 104, "price": 200.0, "category": "A"},
        {"pid": 105, "price": 240.0, "category": "A"},
        {"pid": 106, "price": 230.0, "category": "A"},
        {"pid": 107, "price": 240.0, "category": "A"},
        ])

