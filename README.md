````markdown
# LangGraph Chatbot

A stateful conversational AI application built with LangGraph, LangChain, and Streamlit. The application provides a clean chat interface with conversation threads, message history, and streaming AI responses.

## Overview

This project demonstrates how to build a conversational AI application using LangGraph for workflow and state management, LangChain for LLM integration, and Streamlit for the frontend interface.

The application supports multiple independent conversations, allowing users to create new chats and switch between existing conversation threads.

## Features

- Stateful conversations using LangGraph
- Multiple independent conversation threads
- Conversation history
- Streaming AI responses
- Interactive Streamlit interface
- New conversation creation
- Modular backend architecture
- LLM integration through LangChain
- Environment-based API configuration

## Architecture

```text
                    ┌─────────────────────┐
                    │      Streamlit      │
                    │         UI          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Chat Controller   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      LangGraph      │
                    │   State / Workflow  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     LangChain       │
                    │    LLM Interface    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │        LLM          │
                    └─────────────────────┘
````

## How It Works

The application is divided into two primary layers:

### Frontend

The Streamlit interface handles:

* User input
* Displaying messages
* Conversation selection
* Creating new conversations
* Rendering streamed responses

### Backend

The backend uses LangGraph to manage:

* Conversation state
* Message flow
* LLM execution
* Thread-based conversations
* Streaming responses

## Conversation Threads

Each conversation is assigned a unique thread ID.

```text
Thread 1
│
├── User Message
├── AI Response
├── User Message
└── AI Response

Thread 2
│
├── User Message
└── AI Response
```

This keeps conversations independent and allows users to switch between different conversations without mixing their message history.

## Streaming Responses

The application supports streaming AI responses.

Instead of waiting for the entire response to be generated, the response is progressively displayed in the Streamlit interface.

```text
User Message
      │
      ▼
LangGraph Workflow
      │
      ▼
LLM Generation
      │
      ▼
Streaming Response
      │
      ▼
Streamlit UI
```

## Project Structure

```text
Chatbot/
│
├── .gitignore
├── chatbot.ipynb
├── code.py
├── requirements.txt
├── streaming.py
├── threading.py
├── ui.py
└── README.md
```

## File Description

| File               | Description                                  |
| ------------------ | -------------------------------------------- |
| `ui.py`            | Streamlit frontend and chatbot interface     |
| `threading.py`     | Conversation thread management               |
| `streaming.py`     | Streaming chatbot responses                  |
| `code.py`          | Core chatbot implementation                  |
| `chatbot.ipynb`    | Notebook for experimentation and development |
| `requirements.txt` | Project dependencies                         |
| `.gitignore`       | Files and directories excluded from Git      |

## Tech Stack

| Technology       | Purpose                                     |
| ---------------- | ------------------------------------------- |
| Python           | Application development                     |
| LangGraph        | State management and workflow orchestration |
| LangChain        | LLM integration                             |
| Streamlit        | Web-based user interface                    |
| Jupyter Notebook | Experimentation and development             |

## Getting Started

### Prerequisites

Make sure the following are installed:

* Python 3.10 or higher
* pip
* Git

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ANNON17-byte/Chatbot.git
```

### 2. Navigate to the Project

```bash
cd Chatbot
```

### 3. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the root directory.

Add the required API credentials for your LLM provider.

Example:

```env
API_KEY=your_api_key_here
```

Do not commit the `.env` file or API keys to GitHub.

## Running the Application

Start the Streamlit application:

```bash
streamlit run ui.py
```

The application will normally be available at:

```text
http://localhost:8501
```

## Usage

1. Start the Streamlit application.
2. Open the application in your browser.
3. Enter a message in the chat input.
4. Send the message to the chatbot.
5. The response will be streamed to the interface.
6. Create a new chat using the New Chat button.
7. Switch between conversations using the conversation history.

## Example

```text
User:
Explain what LangGraph is.

AI:
LangGraph is a framework for building stateful,
multi-step applications with LLMs...
```

## Conversation Flow

```text
                User
                 │
                 ▼
          Streamlit Interface
                 │
                 ▼
          Thread Identification
                 │
                 ▼
            LangGraph
                 │
                 ▼
              LLM
                 │
                 ▼
        Streaming Response
                 │
                 ▼
          Streamlit UI
```

