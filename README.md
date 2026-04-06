# 🛒 Shopsy - E-Commerce Website

![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)

**Shopsy** is a modern, inquiry-based e-commerce web application. It features a fast, responsive user interface built with React/Vite and a robust, high-performance backend powered by Python and FastAPI, utilizing MongoDB for flexible data management.

---

## 🚀 Tech Stack

### Frontend
* **Framework:** React.js (via Vite)
* **Languages:** JavaScript, HTML, CSS
* **Directory:** `/Frontend`

### Backend
* **Framework:** FastAPI (Python)
* **Database:** MongoDB
* **Entry Point:** `main.py`

---

## ✨ Features

* **Inquiry-Based Shopping:** Allows users to easily browse products and submit inquiries.
* **Modern UI/UX:** Fast and responsive design utilizing React.
* **High-Performance API:** Asynchronous API routes powered by FastAPI for quick data retrieval and processing.
* **Scalable Database:** Document-based data storage using MongoDB for products, user inquiries, and application data.

---

🛠️ Getting Started

Follow these instructions to set up the project locally for development and testing.
Prerequisites

    Node.js (v16+ recommended)

    Python (v3.8+ recommended)

    MongoDB (Local instance or Atlas URI)

1. Clone the Repository
Bash

git clone [https://github.com/heetdudani/Shopsy---E-commerce-website.git](https://github.com/heetdudani/Shopsy---E-commerce-website.git)
cd Shopsy---E-commerce-website

2. Backend Setup (FastAPI)

    Ensure you are in the root directory where main.py is located.

    Create a virtual environment (optional but recommended):
    Bash

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

    Install the required Python dependencies:
    Bash

    pip install fastapi uvicorn pymongo
    # Add any other dependencies your project requires

    Start the FastAPI development server:
    Bash

    uvicorn main:app --reload

    The backend API will run at http://localhost:8000. You can view the interactive API docs at http://localhost:8000/docs.

3. Frontend Setup (React)

    Open a new terminal instance and navigate to the frontend directory:
    Bash

    cd Frontend

    Install the necessary Node dependencies:
    Bash

    npm install

    Start the Vite development server:
    Bash

    npm run dev
## 📁 Project Structure

```text
Shopsy---E-commerce-website/
├── Frontend/               # React frontend source code, components, and assets
│   ├── src/
│   ├── public/
│   └── package.json
├── main.py                 # FastAPI backend application entry point
├── README.md               # Project documentation
└── .gitignore              # Files and folders ignored by Git


