from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Baca isi dokumen
with open("dokumen.txt", "r", encoding="utf-8") as f:
    isi_dokumen = f.read()

print("Chatbot Dokumen siap!")
print("=====================")

messages = []

system_prompt = f"""
Kamu adalah asisten yang membantu menjawperab pertanyaan berdasarkan dokumen berikut.
Jawab hanya berdasarkan informasi yang ada di dokumen.
Kalau tidak ada di dokumen, bilang 'Maaf, informasi tersebut tidak tersedia.'
Selalu jawab dalam Bahasa Indonesia dengan ramah.

ISI DOKUMEN:
{isi_dokumen}
"""

while True:
    pesan = input("Kamu: ")
    
    if pesan.lower() == "exit":
        print("Sampai jumpa!")
        break
    
    messages.append({"role": "user", "content": pesan})
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            *messages
        ]
    )
    
    balasan = response.choices[0].message.content
    messages.append({"role": "assistant", "content": balasan})
    
    print(f"Bot: {balasan}")
    print()