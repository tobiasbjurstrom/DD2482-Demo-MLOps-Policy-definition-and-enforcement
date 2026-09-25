import os
import sys
from pathlib import Path
from google import genai


WRAPPER_PATH = Path("prompts/customer_support_wrapper_bad.txt")
MODEL_ID = "gemini-3.5-flash-lite"


def run_cli():
    if "GEMINI_API_KEY" not in os.environ:
        print("GEMINI_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)

    if not WRAPPER_PATH.exists():
        print(f"Template file not found at {WRAPPER_PATH}", file=sys.stderr)
        sys.exit(1)

    template = WRAPPER_PATH.read_text()
    client = genai.Client(http_options={'api_version': 'v1'})

    print("Type your message and press Enter. Type 'exit' to stop.\n")

    chat = client.chats.create(
    model=MODEL_ID,
    )

    while True:
        try:
            user_input = input("You > ").strip()
        except (KeyboardInterrupt):
            break

        if not user_input:
            continue
        if user_input.lower() == "exit":
            break

        # Inject the terminal input into the customer support template
        wrapped_prompt = template.replace("{{query}}", user_input)

        try:
            response = chat.send_message(wrapped_prompt)
            print(f"\nGemini > {response.text}\n")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    run_cli()