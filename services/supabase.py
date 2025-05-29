import os
from supabase import create_client, Client
from decouple import config

SUPABASE_URL = config("SUPABASE_URL")
SUPABASE_ANON_KEY = config("SUPABASE_ANON_KEY")
SUPABASE_SERVICE_ROLE_KEY = config("SUPABASE_SERVICE_ROLE_KEY")

# Client for general operations
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

# Admin client for server-side operations
supabase_admin: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)