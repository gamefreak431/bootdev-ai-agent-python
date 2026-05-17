import os
import argparse
from dotenv import load_dotenv
from config import system_prompt
from config import available_functions
from google import genai
from google.genai import types

def cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("user_prompt", help="The prompt to send to the Gemini API")
    parser.add_argument("--verbose", action="store_true", help="Print additional information about the API response")
    return parser.parse_args()

def api_key_check():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    return api_key

def generate_content(api_key, messages, gemini_model = "gemini-2.5-flash"):
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model = gemini_model,
        contents = messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0,
            tools=[available_functions]
        )
    )
    if response.usage_metadata is None:
        raise RuntimeError("Response does not contain usage metadata. Likely a failed API call, try running the script again.")
    return response

def display_content(prompt, response, verbose):
    prompt_tokens = response.usage_metadata.prompt_token_count
    candidates_tokens = response.usage_metadata.candidates_token_count
    if response.function_calls:
        functions_called = "\n".join([f"Calling function: {function_call.name}({function_call.args})" for function_call in response.function_calls])
    output = functions_called if response.function_calls else response.text
    
    if verbose:
        return f"User prompt: {prompt}\nPrompt tokens: {prompt_tokens}\nResponse tokens: {candidates_tokens}\n{output}"
    return output

def main():
    args = cli_args()
    load_dotenv()
    api_key = api_key_check()

    prompt = args.user_prompt
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

    response = generate_content(api_key, messages)
    print(display_content(prompt, response, args.verbose))


if __name__ == "__main__":
    main()
