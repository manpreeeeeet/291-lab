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
    students = db["students"]

    students.delete_many({})

    students.insert_many([
        {"name": "Sana Glass", "social": {"twitter": "twitter/sanaglass"}},
        {"name": "Sana Baker", "social": {"twitter": "twitter/sanabaker"}},
        {"name": "Sarah  Branch", "social": {"twitter": "twitter/sarabranch"}},
        {"name": "Dexter Grimes", "social": {"twitter": "twitter/dextergrimes"}},
        {"name": "Cody Gardener", "social": {"twitter": "twitter/cody"}}
    ])
    
    res = students.aggregate([
        {"$match": {"social.twitter": "twitter/sanaglass"}}
    ])

    print("\nIterating the cursor")
    for i in res:
        pprint(i)
        print("")


