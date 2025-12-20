#Langfuse tracing configuration.
import os
from dotenv import load_dotenv


def init_tracing():
    #Initialize Langfuse tracing.
    load_dotenv()

    required = [
        "LANGFUSE_PUBLIC_KEY",
        "LANGFUSE_SECRET_KEY",
        "LANGFUSE_BASE_URL"
    ]

    missing = [key for key in required if not os.getenv(key)]

    if missing:
        print("langfuse tracing not configured")
        print(f"missing: {', '.join(missing)}")
        return False
    else:
        print("langfuse tracing enabled")
        print(f"host: {os.getenv('LANGFUSE_BASE_URL')}")
        return True