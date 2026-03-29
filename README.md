
[Document Summarizer - Screencastify - March 29, 2026 11_51 AM.webm](https://github.com/user-attachments/assets/7eb853ec-f042-4fb8-8817-c43402e4667c)


# AI Document Summarizer

A full-stack AI-powered web app that summarizes documents and answers questions about them using the Anthropic Claude API.

## Features

- Paste text or upload a PDF and get an instant AI-generated summary
- Ask follow-up questions about the document in natural language
- Clean, minimal web interface built with HTML, CSS, and JavaScript
- Python/Flask backend with secure API key management

## Tech Stack

- **Python** / **Flask** — backend web server and routing
- **Anthropic Claude API** — AI summarization and Q&A
- **PyPDF2** — PDF text extraction
- **HTML / CSS / JavaScript** — frontend interface

## Getting Started

1. Clone the repo
```
   git clone https://github.com/DuncanByrneUT/document-summarizer.git
   cd document-summarizer
```

2. Create and activate a virtual environment
```
   python3 -m venv venv
   source venv/bin/activate
```

3. Install dependencies
```
   pip3 install flask anthropic pypdf2 python-dotenv
```

4. Create a `.env` file in the root directory and add your Anthropic API key
```
   ANTHROPIC_API_KEY=your-api-key-here
```

5. Run the app
```
   python3 app.py
```

6. Open your browser and go to `http://127.0.0.1:5000`

## Usage

- Paste any text into the text box and click **Summarize**
- Or upload a PDF file and click **Summarize**
- Once the summary appears, type a question about the document and click **Ask**
