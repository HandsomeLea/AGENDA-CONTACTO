from supabase import create_client, Client
import os

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

data = supabase.table("contactos").select("*").execute()
print(data)

