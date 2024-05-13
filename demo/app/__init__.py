from supabase import create_client, Client
import os
from flask import Flask

SUPABASE_URL = os.environ.get("RETROSCOPE_DEMO_SUPABASE_URL")
SUPABASE_KEY =  os.environ.get("RETROSCOPE_DEMO_SUPABASE_API_KEY")

print(SUPABASE_URL)
print(SUPABASE_KEY)

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    # Initialize Supabase client
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    app.config['SUPABASE_CLIENT'] = supabase

    return app