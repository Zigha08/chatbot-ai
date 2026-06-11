from groq import Groq
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

with open("dokumen.txt", "r", encoding="utf-8") as f:
    isi_dokumen = f.read()

print("Chatbot Pro siap!")
print("=================")

messages = []
riwayat = []

system_prompt = f"""
Kamu adalah asisten yang membantu menjawab pertanyaan berdasarkan dokumen berikut.
Jawab hanya berdasarkan informasi yang ada di dokumen.
Kalau tidak ada di dokumen, bilang 'Maaf, informasi tersebut tidak tersedia.'
Selalu jawab dalam Bahasa Indonesia dengan ramah.

ISI DOKUMEN:
{isi_dokumen}
"""

waktu_mulai = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
riwayat.append(f"=== Sesi Chat: {waktu_mulai} ===\n")

while True:
    pesan = input("Kamu: ")
    
    if pesan.lower() == "exit":
        print("Sampai jumpa!")
        riwayat.append("=== Chat selesai ===\n")
        break
    
    messages.append({"role": "user", "content": pesan})
    riwayat.append(f"Pelanggan: {pesan}")
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            *messages
        ]
    )
    
    balasan = response.choices[0].message.content
    messages.append({"role": "assistant", "content": balasan})
    riwayat.append(f"Bot: {balasan}\n")
    
    print(f"Bot: {balasan}")
    print()

# Simpan riwayat ke file
with open("riwayat_chat.txt", "a", encoding="utf-8") as f:
    f.write("\n".join(riwayat))
    f.write("\n")

print("Riwayat chat tersimpan di riwayat_chat.txt!")