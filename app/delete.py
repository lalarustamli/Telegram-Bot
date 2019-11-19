from pymongo import MongoClient, ReturnDocument

DB_URL = "mongodb://ibar:bank12345678@ibarchatbot-shard-00-00-2pyzh.mongodb.net:27017,ibarchatbot-shard-00-01-2pyzh.mongodb.net:27017,ibarchatbot-shard-00-02-2pyzh.mongodb.net:27017/test?ssl=true&replicaSet=ibarchatbot-shard-0&authSource=admin&retryWrites=true"

def deleteAll():
    client = MongoClient(DB_URL)
    db = client['chatbotdb']
    user_states = db['telegram_user_states']
    myquery = {"sender_id": 319346733}

    x = user_states.delete_many(myquery)

    print(x.deleted_count, " documents deleted.")


deleteAll()