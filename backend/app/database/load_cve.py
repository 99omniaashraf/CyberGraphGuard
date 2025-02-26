import os
import pandas as pd
from arango import ArangoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to ArangoDB
client = ArangoClient(hosts=os.getenv("DATABASE_URL"))
db = client.db('cybergraphguard', username=os.getenv("DB_USERNAME"), password=os.getenv("DB_PASSWORD"))

# Create collection if not exists
if not db.has_collection('CVE'):
    db.create_collection('CVE')

# Load CSV data
DATA_PATH = os.path.join(os.path.dirname(__file__), 'cve_data', 'CVE.csv')
df = pd.read_csv(DATA_PATH)

# Clean column names
df.columns = df.columns.str.strip().str.replace(" ", "_")

# Convert invalid numbers to NaN and fill missing values
for col in df.select_dtypes(include=['object']).columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df.fillna(0, inplace=True)

# Add unique `_key` if missing
if "_key" not in df.columns:
    df["_key"] = df.index.astype(str)

# Insert data in bulk
collection = db.collection('CVE')
try:
    collection.import_bulk(df.to_dict(orient="records"), overwrite=True)
    print("✅ CVE data successfully loaded into ArangoDB!")
except Exception as e:
    print(f"❌ Error inserting data: {e}")
