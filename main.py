import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

try:
    api_key = os.environ.get("GEMINI_API_KEY")
except KeyError:
    raise KeyError("GEMINI_API_KEY not found in environment variables.")

client = genai.Client(api_key=api_key)
gemini_model = "gemini-2.5-flash"
test_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

response = client.models.generate_content(
    model = gemini_model, contents = test_prompt
)

def main():
    print("Hello from bootdev-ai-agent-python!")
    print(response.text)


if __name__ == "__main__":
    main()
