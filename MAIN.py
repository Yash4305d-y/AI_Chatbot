from groq import Groq

client = Groq(api_key="API_KEY")   #Add you groq api key (can be claimed for free!)

def chat_with_bot(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        reply = chat_with_bot(user_input)
        print("Chatbot:", reply)
        print("\n")
