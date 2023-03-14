from pymongo import MongoClient
import sys
from pprint import pprint

# Setup and insert

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        sys.exit()

    port_name = int(sys.argv[1])
    print(f"connecting to port: {port_name}")

    client = MongoClient('localhost', port_name)

    db = client["cmput291db"]
    reviews = db["reviews"]
    products = db["products"]
    
    reviews.delete_many({})
    reviews.insert_many([
        {"pid": 101, "rating": 5.0},
        {"pid": 101, "rating": 4.0},
        {"pid": 102, "rating": 1.0}
        ]
    )
    
    # Lookup
    res = products.aggregate([
        {"$lookup": {
            "from": "reviews", # Collection to join
            "localField": "pid", # Fields from the input document: here it is
            # products
            "foreignField": "pid", # field from the 'from' collection
            "as": "customer_reviews" # <output array field
            }
        }
    ])
            


    print("\nIterating the cursor")
    for i in res:
        pprint(i)
        print("")


