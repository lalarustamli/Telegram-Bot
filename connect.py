from pymongo import MongoClient, ReturnDocument

DB_URL = "mongodb://ibar:bank12345678@ibarchatbot-shard-00-00-2pyzh.mongodb.net:27017,ibarchatbot-shard-00-01-2pyzh.mongodb.net:27017,ibarchatbot-shard-00-02-2pyzh.mongodb.net:27017/test?ssl=true&replicaSet=ibarchatbot-shard-0&authSource=admin&retryWrites=true"
client = MongoClient(DB_URL)
db = client['chatbotdb']
user_states = db['telegram_user_states']
def insert_sender(sender):
    """Insert <sender> object to the database.
    """
    user_states.insert_one(sender)
    client.close()


def update_sender(sender, new_values):
    """Update <sender> object with <new_values> in the database.
    """
    updated_sender = user_states.find_one_and_update(
        sender, new_values, return_document=ReturnDocument.AFTER)
    client.close()
    return updated_sender


def find_sender(sender_id, state):
    """Return sender object from the database with <sender_id>.
    """
    updated_sender = user_states.find_one({'sender_id': sender_id, 'state': state, 'status': STATE_STATUS[0]})
    client.close()
    return updated_sender
