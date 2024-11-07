
# FealtyX-Backend-Assignment

This is a FastAPI project designed to handle basic student data. This README will guide you through setting up and running the project locally, along with installing OLLAMA and pulling the LLaMA model.

## Requirements

- Python 3.7+
- [FastAPI](https://fastapi.tiangolo.com/)
- [OLLAMA](https://github.com/ollama/ollama/blob/main/README.md) for working with LLaMA 3.1 model
- Other dependencies listed in `requirements.txt`

## Setup Instructions

Follow these steps to set up and run the project:

### 1. Clone the Repository

```bash
git clone https://github.com/kanishk128/FealtyX-Backend-Assignment
cd FealtyX-Backend-Assignment
```

### 2. Set Up a Virtual Environment (Recommended)

Using Python’s `venv` module:

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

Or, if you're using Conda:

```bash
conda create -n venv python=3.7
conda activate venv
```

### 3. Install Dependencies

Make sure you are in the project directory, then install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Install OLLAMA

To download and install OLLAMA, visit the [official GitHub repository](https://github.com/ollama/ollama) and follow the installation instructions for your operating system.

### 5. Pull the LLaMA Model

Once OLLAMA is installed, you can download the LLaMA 3.1 model with the following command:

```bash
ollama pull llama3.1
```

This will pull the LLaMA 3.1 model with the desired parameters.

### 6. Run the FastAPI Application

Start the FastAPI application using the following command:

```bash
uvicorn main:app --reload
```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 7. Accessing the API Documentation

FastAPI provides interactive API documentation at:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Project Structure

Here's a basic overview of the project structure:

```plaintext
FealtyX-Backend-Assignment/
│
├── app/
│   ├── main.py               # Main application file
│   ├── models/               # Data models
│   │   └── student.py        # Student data model
│   └── services/             # Service layer for business logic
│       └── student_crud.py   # CRUD operations for student
├── requirements.txt          # Dependencies file
└── README.md                 # Project documentation
```
