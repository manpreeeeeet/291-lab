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


    res = products.aggregate([
        {"$group": {
            "_id": {"cat": "$category"},
            }
        }
    ])

    

    # returns a cursor object
    print(res)

    print("\nIterating the cursor")
    for i in res:
        print(i)
   
    print("\nIterating the same cursor")
    for i in res:
        print(i)

