import os
from dotenv import load_dotenv

load_dotenv()

try:
    api_key = os.environ.get("GEMINI_API_KEY")
except KeyError:
    raise KeyError("GEMINI_API_KEY not found in environment variables.")



def main():
    print("Hello from bootdev-ai-agent-python!")


if __name__ == "__main__":
    main()
