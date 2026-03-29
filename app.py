from flask import Flask, request, jsonify, render_template
import anthropic
import PyPDF2
import io
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    text = ""

    if "file" in request.files:
        file = request.files["file"]
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
        for page in pdf_reader.pages:
            text += page.extract_text()
    else:
        text = request.form.get("text", "")

    if not text.strip():
        return jsonify({"error": "No text provided"}), 400

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"Please summarize the following document clearly and concisely:\n\n{text}"
            }
        ]
    )

    return jsonify({"summary": message.content[0].text})

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    document = data.get("document", "")
    question = data.get("question", "")

    if not document or not question:
        return jsonify({"error": "Missing document or question"}), 400

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"Here is a document:\n\n{document}\n\nAnswer this question about it: {question}"
            }
        ]
    )

    return jsonify({"answer": message.content[0].text})

if __name__ == "__main__":
    app.run(debug=True)