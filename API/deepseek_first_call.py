from openai import OpenAI

client = OpenAI(api_key="sk-cf51a9eb231b4d9f85eaf4a8db644183", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model = "deepseek-chat",
    messages = [
        {"role": "system", "content": "You are a helpful assistent"},
        {"role": "user", "content": "Hello"}
    ],
    stream = False
)

print(response.choices[0].message.content)