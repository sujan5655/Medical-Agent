# Medical Chatbot

A medical question-answering chatbot built with Python, LangChain, Hugging Face, OpenAI, FAISS, Sentence Transformers, and Streamlit.

## Prerequisites

- Python 3.10 or later
- Pip

## Setup Instructions

### 1. Navigate to the project directory

```bash
cd "Medical Chatbot New Project"
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows (Command Prompt):**

```bash
venv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 4. Install the required packages

```bash
python -m pip install sentence-transformers
python -m pip install -U openai huggingface_hub python-dotenv
python -m pip install -U langchain-openai
python -m pip install -U langchain-classic
python -m pip install -U langchain langchain-community langchain-huggingface pypdf
python -m pip install streamlit
python -m pip install faiss-cpu
```

### 5. Configure environment variables

Create a `.env` file in your project root.

For OpenAI:

```env
OPENAI_API_KEY=your_openai_api_key
```

For Hugging Face, if required:

```env
HF_TOKEN=your_huggingface_token
```

Replace the placeholders with your actual credentials. Never share your API keys or commit your `.env` file to GitHub.

### 6. Check your FAISS database

Ensure that your vector database has already been created. For example:

```text
vectorstore/
└── db_faiss/
```

The embedding model used to load the database must match the model used to create it.

### 7. Run the chatbot

```bash
streamlit run medibot.py
```

Open the local URL displayed in your terminal to access the chatbot.

## Troubleshooting

### Missing Python package

Install the missing package in your activated virtual environment:

```bash
python -m pip install package-name
```

### OpenAI API error

Check that `OPENAI_API_KEY` is configured correctly and that your API account has access to the model and available API credits.

### Hugging Face inference error

Check model availability, provider support, token permissions, and inference credits.

### FAISS database not found

Verify the database path in your Python code and ensure that the vector database exists.

### Streamlit command not found

```bash
python -m pip install streamlit
```

Then run:

```bash
streamlit run medibot.py
```

## Medical Disclaimer

This chatbot provides informational and educational responses only. It does not replace professional medical diagnosis, treatment, or advice. Consult a qualified healthcare professional for medical concerns.

## License

Add your preferred license if you plan to distribute this project.
