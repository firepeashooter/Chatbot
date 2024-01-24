
# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")


def chat_with_bot(prompt):
    

    response = client.chat.completions.create(
        model="local-model", # this field is currently unused
        messages=[
            {"role": "user", "content": prompt},
            
            ],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":

    while True:
        human_input = input("Human: ")

        if human_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_bot(human_input)

        print("Chatbot: ", response)

