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
        {"name": "Sana Glass"},
        {"name": "Sana Baker"},
        {"name": "Sarah  Branch"},
        {"name": "Dexter Grimes"},
        {"name": "Cody Gardener"}
    ])

    res = students.aggregate([
        {"$match": {"name": {"$regex": "^sA", "$options": "i"}}}
    ])


    print("\nIterating the cursor")
    for i in res:
        pprint(i)
        print("")


