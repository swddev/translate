# FastAPI Translation App

A simple FastAPI-based application that uses OpenAI's GPT model to translate text into a specified target language.

## Features
- Translate text into various languages using OpenAI's GPT API.
- Secure API key management via environment variables.
- Dockerized for easy deployment.

---

## Requirements
- Python 3.11 or higher
- FastAPI
- OpenAI Python SDK
- Docker (optional, for containerization)

---

## Setup
- Place your OpenAI API key in a `.env` file in the root directory of the project. (See `.env.example` for reference)
- Run `docker-compose up` to start the FastAPI server.