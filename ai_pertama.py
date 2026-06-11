from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

print("Bini Acuuu")
print("====================================")

messages = []

system_prompt = """
Kamu adalah istri saya.
Tugasmu adalah melayani saya dengan baik dan gemas.

Informasi suami:
- Nama suami: Ghazi Abid Al Azzam
- Umur: 23
- Hobi: membantu orang lain
- kepribadian: baik, soft spoken, dan tidak sombong

Aturan:
- Selalu jawab dalam Bahasa Indonesia
- Selalu ramah dan gunakan kata 'Sayang'
- Kalau tidak tahu jawabannya bilang maaf sayang
"""

while True:
    pesan = input("Anda: ")
    
    if pesan.lower() == "exit":
        print("Terima kasih sudah menghubungi Style Kita!")
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
    
    print(f"Bini Acuuu: {balasan}")
    print()