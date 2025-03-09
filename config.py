import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Database configuration
    # Default to environment variable if set, otherwise use the provided Aiven PostgreSQL URI
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URI', 
        'postgresql://avnadmin:AVNS_NCqE_hUiKS8Fmm47C9y@pg-testdb-pramodtestdb.d.aivencloud.com:16973/defaultdb?sslmode=require'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Application configuration
    MAX_BOOKINGS = 2