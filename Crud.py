import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]  # Replace "mydatabase" with your preferred database name
collection = db["mycollection"]  # Replace "mycollection" with your preferred collection name

# Create (Insert) operation
def create_document(data):
    result = collection.insert_one(data)
    print("Document inserted with ID:", result.inserted_id)

# Read (Find) operation
def find_documents(query):
    documents = collection.find(query)
    for doc in documents:
        print(doc)

# Update operation
def update_document(query, new_data):
    result = collection.update_one(query, {"$set": new_data})
    print("Modified documents:", result.modified_count)

# Delete operation
def delete_document(query):
    result = collection.delete_one(query)
    print("Deleted documents:", result.deleted_count)

if __name__ == "__main__":
    # Create
    data = {"name": "John Doe", "age": 30, "city": "New York"}
    create_document(data)

    # Read
    query = {"city": "New York"}
    print("Documents matching the query:")
    find_documents(query)

    # Update
    update_query = {"name": "John Doe"}
    new_data = {"age": 32}
    update_document(update_query, new_data)

    # Read after update
    print("Documents matching the query after update:")
    find_documents(query)

    # Delete
    delete_query = {"age": 32}
    delete_document(delete_query)

    # Read after delete
    print("Documents matching the query after delete:")
    find_documents(query)