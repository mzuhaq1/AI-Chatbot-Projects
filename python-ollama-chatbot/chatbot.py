import ollama

print("AI Chatbot (TinyLlama)")
print("Type 'exit' to stop\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = ollama.chat(
        model="tinyllama",
        messages=[{"role": "user", "content": user_input}]
    )

    print("Bot:", response["message"]["content"])