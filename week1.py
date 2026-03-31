import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    system="You are a senior retail analytics expert. Be concise and tie everything to business impact.",
    messages=[
        {"role": "user", "content": "What are 3 trends in retail analytics right now?"}
    ]
)

print(message.content[0].text)