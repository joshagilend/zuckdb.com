
import os
from supabase import create_client, Client

url: str = os.environ.get("TIMETRAVELDB_SUPABASE_URL")
key: str = os.environ.get("TIMETRAVELDB_SUPABASE_API_KEY")
supabase: Client = create_client(url, key)

# Supabase test API calls

response = supabase.table('test').select("*").execute()
print(response.data) 