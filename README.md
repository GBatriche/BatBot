
# BatBot: AI Chatbot with LangChain

A simple chatbot built with Python using LangChain for natural language processing and AI integration.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/username/ai-chatbot.git
cd ai-chatbot
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

This project implements a conversational AI chatbot using the LangChain framework. The chatbot can maintain contextual conversations and respond to user queries using modern language models.

## Features

- Natural conversation interface
- Contextual memory
- Integration with AI providers (OpenAI, Anthropic)
- Customizable prompts
- Simple web interface

## Technologies

- Python 3.8+
- LangChain
- Streamlit
- OpenAI API
- python-dotenv

## Prerequisites

- Python 3.8 or higher
- API key from your chosen AI provider

## Configuration

1. Copy the environment file:
```bash
cp .env.example .env
```

2. Add your API key to `.env`:
```env
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-3.5-turbo
TEMPERATURE=0.7
```

## Usage

Run the chatbot interface:
```bash
streamlit run app.py
```

Or use it programmatically:
```python
from chatbot import ChatBot

bot = ChatBot()
response = bot.chat("Hello, how are you?")
print(response)
```

## Project Structure

```
ai-chatbot/
├── src/
│   ├── chatbot.py       # Main chatbot class
│   ├── memory.py        # Conversation memory
│   └── utils.py         # Helper functions
├── .env.example         # Environment variables template
├── requirements.txt     # Dependencies
├── app.py              # Streamlit interface
└── README.md           # This file
```

## Contributing

1. Fork the project
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request


## Contact

Gabriel Batriche- batricheg@gmail.com

Project Link: https://github.com/GBatriche/BatBot
