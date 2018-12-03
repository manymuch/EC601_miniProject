import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

def connect_mongo():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["twitter"]
    collection = mydb["twitter_images"]
    return collection

def insert(collection,USER_NAME,TWITTER_NAME,URL,LABEL):
    dictionary ={"user_name":USER_NAME, "twitter_account":TWITTER_NAME, "url":URL, "label":LABEL}
    collection.insert_one(dictionary)

def search(collection,keyword):
    #query =  { "label": {"$search": keyword }}
    query = { "label": { "$regex": keyword } }
    for x in collection.find(query):
        print(x)

def user(collection,user_name):
    answer = collection.find({"user_name":user_name})
    i=0;
    for x in answer:
        i=i+1
    return i

def clear_table(collection):
    collection.drop()

def printall(collection):
    for x in collection.find():
        print(x)
