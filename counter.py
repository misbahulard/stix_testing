from __future__ import print_function
from pymongo import MongoClient

if __name__ == "__main__":

    client = MongoClient('mongodb://localhost:27017')

    db = client['stix']
    actor_coll = db['actor_test']
    target_coll = db['target_test']

    query_ip = {
        "$group": {
           "_id": { 
				"ip": "$ip"
			},
           "count": { "$sum": 1 }
        },
    }

    query_name = {
        "$group": {
           "_id": { 
				"name": "$name"
			},
           "count": { "$sum": 1 }
        },
    }

    query_sort = {
        "$sort": { "count": -1 }
    }

    print("==============ACTOR==============")
    print("Testing Top 10 IP..")
    result_ip = list(actor_coll.aggregate([query_ip, query_sort]))
    for index in range(10):
        print(result_ip[index])

    print("\nTesting Top 10 Location..")
    result_name = list(actor_coll.aggregate([query_name, query_sort]))
    for index in range(10):
        print(result_name[index])

    print("\n==============TARGET==============")
    print("Testing Top 10 IP..")
    result_ip = list(target_coll.aggregate([query_ip, query_sort]))
    for index in range(10):
        print(result_ip[index])

    print("\nTesting Top 10 Location..")
    result_name = list(target_coll.aggregate([query_name, query_sort]))
    for index in range(10):
        print(result_name[index])
