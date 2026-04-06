import anthropic
import pandas as pd
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

df = pd.read_csv("sales_data.csv")

summary = f"""
Rows: {df.shape[0]}
Columns: {df.shape[1]}

Revenue by category:
{df.groupby('category')['revenue'].sum().to_string()}

Average return rate by category:
{df.groupby('category')['return_rate'].mean().round(3).to_string()}

Top 3 products by revenue:
{df.nlargest(3, 'revenue')[['product','revenue']].to_string()}

Average weeks to deliver by category:
{df.groupby('category')['weeks_to_deliver'].mean().round(1).to_string()}
"""

print("Data summary:")
print(summary)
print("\nSending to Claude...\n")

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    system="Analyze this data and give insights.",    messages=[
        {"role": "user", "content": f"Here is this week's sales data summary:\n{summary}\n\nGive me the 3 most important insights and one recommended action for each."}
    ]
)

print("Claude's insights:")
print(message.content[0].text)