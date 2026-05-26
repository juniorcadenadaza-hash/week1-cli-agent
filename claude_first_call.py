import os
from datetime import datetime
from anthropic import Anthropic, BadRequestError, AuthenticationError, APIConnectionError, RateLimitError

api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError("ANTHROPIC_API_KEY is missing. Set it in PowerShell before running this script.")

client = Anthropic(api_key=api_key)

prompt = "Explain AI automation in 4 simple bullet points for a beginner learning Python."

try:
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    response_text = message.content[0].text

    print(response_text)

    with open("claude_response_log.txt", "a", encoding="utf-8") as file:
        file.write("\n--- New Claude Response ---\n")
        file.write(f"Time: {datetime.now()}\n")
        file.write(f"Prompt: {prompt}\n")
        file.write("Response:\n")
        file.write(response_text + "\n")

except BadRequestError as error:
    print("The request reached Anthropic, but Anthropic rejected it.")
    print("Most likely reason: billing, credits, model access, or request format.")
    print(error)

    with open("claude_error_log.txt", "a", encoding="utf-8") as file:
        file.write("\n--- Claude API Error ---\n")
        file.write(f"Time: {datetime.now()}\n")
        file.write(f"Prompt: {prompt}\n")
        file.write("Error type: BadRequestError\n")
        file.write(str(error) + "\n")

except AuthenticationError as error:
    print("Authentication failed. Check your ANTHROPIC_API_KEY.")
    print(error)

except RateLimitError as error:
    print("Rate limit reached. Try again later.")
    print(error)

except APIConnectionError as error:
    print("Could not connect to Anthropic. Check your internet connection.")
    print(error)