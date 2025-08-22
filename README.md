# BatBot - AI Chatbot

A conversational AI chatbot built with Python using LangChain that can chat about content from websites, PDFs, and YouTube videos.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/username/batbot.git
cd batbot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## About

BatBot is a friendly AI assistant that can analyze and answer questions about various types of content. Simply provide a website URL, PDF file, or YouTube video, and BatBot will use that information to have contextual conversations with you.

## Features

- Chat with website content
- Analyze PDF documents
- Process YouTube video transcripts
- Contextual conversation memory
- Simple command-line interface

## Technologies

- Python 3.8+
- LangChain
- Groq (Llama3-8B model)
- WebBaseLoader for websites
- PyPDFLoader for PDF files
- YoutubeLoader for video transcripts
- python-dotenv

## Prerequisites

- Python 3.8 or higher
- Groq API key

## Configuration

1. Copy the environment file:
```bash
cp .env.example .env
```

2. Add your Groq API key to `.env`:
```env
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

Run the chatbot:
```bash
python main.py
```

Follow the prompts:
1. Choose content type (1=Website, 2=PDF, 3=YouTube)
2. Provide the URL or file path
3. Start chatting about the content
4. Type 'x' to exit

Example conversation:
```
Welcome to BatBot
Digite 1 se você quiser conversar com um site
Digite 2 se você quiser conversar com um PDF  
Digite 3 se você quiser conversar com um vídeo do YouTube
1
Digite a url do site: https://example.com
Usuario: What is this website about?
Bot: Based on the website content, this site is about...
Usuario: x
```

## Project Structure

```
batbot/
├── main.py             # Main chatbot application
├── .env.example        # Environment variables template
├── requirements.txt    # Dependencies
└── README.md          # This file
```

## Dependencies

Add these to your `requirements.txt`:
```
langchain
langchain-groq
langchain-community
python-dotenv
pypdf
youtube-transcript-api
beautifulsoup4
```

## Contributing

1. Fork the project
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Contact

Your Name - your.email@example.com

Project Link: https://github.com/username/batbot
