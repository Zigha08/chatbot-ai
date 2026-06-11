from flask import Flask, request, jsonify, render_template
from groq import Groq
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

with open("dokumen.txt", "r", encoding="utf-8") as f:
    isi_dokumen = f.read()

system_prompt = f"""
Kamu adalah asisten yang membantu menjawab pertanyaan berdasarkan dokumen berikut.
Jawab hanya berdasarkan informasi yang ada di dokumen.
Kalau tidak ada di dokumen, bilang 'Maaf, informasi tersebut tidak tersedia.'
Selalu jawab dalam Bahasa Indonesia dengan ramah.

ISI DOKUMEN:
{isi_dokumen}
"""

messages = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    pesan = request.json["pesan"]
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
    
    return jsonify({"balasan": balasan})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)