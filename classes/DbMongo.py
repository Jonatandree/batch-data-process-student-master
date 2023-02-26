import pymongo
import os

class DbMongo:
    
    @staticmethod
    def getDB():
        user = os.environ['USER']
        password = os.environ['PASSWORD']
        cluster = os.environ['CLUSTER']
        query_string = 'retryWrites=true&w=majority'


        ## Connection String
        uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
            user
            , password
            , cluster
            , query_string
        )

        print(uri)
 
        client = pymongo.MongoClient(uri)
        db = client[os.environ['DB']]

        return client, db