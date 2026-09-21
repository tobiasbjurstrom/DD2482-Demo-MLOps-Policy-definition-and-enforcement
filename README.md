# DD2482-Demo-MLOps-Policy-definition-and-enforcement
Demo for defining, enforcing, and automatically testing policies for an AI agent. Part of DD2482.


## Usage

- Import google-genai: `pip install google-genai`
- Set API key: `export GEMINI_API_KEY="your-gemini-api-key"`
- Enable the virtual env: `source .venv/bin/activate`
- Start script with: `python3 gemini_cli.py`
- Install promptfoo: `sudo npm install -g promptfoo@latest`
- Evaluate promptfoo tests: `promptfoo eval`
- View latest promptfoo test: `promptfoo view`

## Notes
- Changing the wrapper is done in the python file for the interactive sessions and in the promptfooconfig-yaml file for the promptfoo testing. There are three tiers of wrappers, increasingly "unsafe".
- I have set up my gemini key in the repo so that it is used for the tests on the prs.