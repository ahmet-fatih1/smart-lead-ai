import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret-key")
    DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///smartlead.db")
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
    AI_PROVIDER = os.environ.get("AI_PROVIDER", "groq")
    BUSINESS_CONTEXT = os.environ.get(
        "BUSINESS_CONTEXT",
        "Sen Mihenk'in yapay zeka asistanısın."
    )
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*")

