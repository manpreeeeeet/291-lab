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
    
    students.delete_many({})

    student = {
            "name": "Askar",
            "grades": [
                {"assignmentName": "a1", "score": 99},
                {"assignmentName": "a2", "score": 99}
             ]
    }

    students.insert_one(student)


