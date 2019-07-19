from __future__ import print_function
from pymongo import MongoClient

if __name__ == "__main__":

    client = MongoClient('mongodb://localhost:27017')

    db = client['stix_pcap']
    actor_coll = db['actor_analytics']
    target_coll = db['target_analytics']

    query = {
        "$group": { 
            "_id": { 
                "ip": "$ip", 
                "country": "$country" 
            }, 
            "count": {"$sum": "$number_observed"}
        },
    }

    query_sort = {
        "$sort": { "count": -1 }
    }

    print("==============ACTOR==============")
    print("\nTesting Top 10")
    result = list(actor_coll.aggregate([query, query_sort]))

    if len(result) >= 10:
        for index in range(10):
            print(result[index])
    else:
        for index in range(len(result)):
            print(result[index])

    print("\n==============TARGET==============")
    print("\nTesting Top 10")
    result = list(target_coll.aggregate([query, query_sort]))
    if len(result) >= 10:
        for index in range(10):
            print(result[index])
    else:
        for index in range(len(result)):
            print(result[index])

    # COUNTRY

    query = {
        "$group": { 
            "_id": "$country",
            "count": {"$sum": "$number_observed"}
        },
    }

    query_sort = {
        "$sort": { "count": -1 }
    }

    print("==============ACTOR==============")
    print("\nTesting Top 10")
    result = list(actor_coll.aggregate([query, query_sort]))

    if len(result) >= 10:
        for index in range(10):
            print(result[index])
    else:
        for index in range(len(result)):
            print(result[index])

    print("\n==============TARGET==============")
    print("\nTesting Top 10")
    result = list(target_coll.aggregate([query, query_sort]))
    if len(result) >= 10:
        for index in range(10):
            print(result[index])
    else:
        for index in range(len(result)):
            print(result[index])
