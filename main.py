import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise KeyError("GEMINI_API_KEY not found in environment variables.")
    client = genai.Client(api_key=api_key)
    gemini_model = "gemini-2.5-flash"

    parser = argparse.ArgumentParser()
    parser.add_argument("user_prompt", help="The prompt to send to the Gemini API")
    args = parser.parse_args()
    prompt = args.user_prompt
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    response = client.models.generate_content(
        model = gemini_model, contents = messages
    )
    if response.usage_metadata is None:
        raise RuntimeError("Response does not contain usage metadata. Likely a failed API call, try running the script again.")

    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Response: \n{response.text}")


if __name__ == "__main__":
    main()
