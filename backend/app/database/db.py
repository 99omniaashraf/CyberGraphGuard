import os
from arango import ArangoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to the database
client = ArangoClient(hosts=os.getenv("DATABASE_URL"))

try:
    db = client.db(
        os.getenv("DB_NAME"),
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
    )
    
    # Check if the connection is successful
    if db.has_collection("CVE"):
        print("✅ Successfully connected to ArangoDB!")
    else:
        print("❌ Connected, but 'CVE' collection does not exist.")
except Exception as e:
    print(f"❌ Error connecting to ArangoDB: {e}")
