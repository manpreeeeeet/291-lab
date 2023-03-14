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
            "price_avg": {"$avg": "$price"},
            "price_sum": {"$sum": "$price"},
            "count": {"$sum": 1},
            "pids": {"$push": "$pid"}
            }
            },
        {"$match": {"price_avg": {"$gt": 150}}}
        ])

    print("\nIterating the command cursor")
    for i in res:
        print(i)

    
    res1 = products.find()
    res2 = res1.clone().skip(2)


    print("\nIterating the cursor.CursorType")
    for i in res1:
        print(i)

    print("\nIterating the cursor res1 again")
    for i in res1:
        print(i)
    
    res1.rewind()
    print("\nRewinding the cursor res1")
    for i in res1:
        print(i)

    print("\nIterating the cursor res2 which is a clone")
    for i in res2: print(i)










