import os
import sys
from pathlib import Path
from google import genai


WRAPPER_PATH = Path("prompts/customer_support_wrapper_bad.txt")
MODEL_ID = "gemini-3.5-flash-lite"


def run_cli():
    if "GEMINI_API_KEY" not in os.environ:
        print("Error: GEMINI_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)

    if not WRAPPER_PATH.exists():
        print(f"Error: Template file not found at {WRAPPER_PATH}", file=sys.stderr)
        sys.exit(1)

    template = WRAPPER_PATH.read_text()
    client = genai.Client(http_options={'api_version': 'v1'})

    print("Type your message and press Enter. Type 'exit' to stop.\n")

    while True:
        try:
            user_input = input("You > ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

        if not user_input:
            continue
        if user_input.lower() in ("exit"):
            break

        # Inject the terminal input into the customer support template
        wrapped_prompt = template.replace("{{query}}", user_input)

        try:
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=wrapped_prompt,
            )
            print(f"\nGemini > {response.text}\n")
        except Exception as e:
            print(f"\nAPI Error: {e}\n", file=sys.stderr)

if __name__ == "__main__":
    run_cli()