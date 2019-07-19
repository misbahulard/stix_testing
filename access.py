from __future__ import print_function
import time
from pymongo import MongoClient

if __name__ == "__main__":

    client = MongoClient('mongodb://localhost:27017')

    db = client['stix_pcap']
    event_coll = db['event']
    bundle_coll = db['bundle']

    start_time = time.time()

    print("Testing access raw event..")
    events = list(event_coll.find())

    print("Time elapsed %.5s seconds" % (time.time() - start_time))

    start_time = time.time()

    print("\nTesting access stix bundle..")
    bundles = list(bundle_coll.find())

    print("Time elapsed %.5s seconds" % (time.time() - start_time))
