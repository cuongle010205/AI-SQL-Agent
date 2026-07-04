# 🤖 AI SQL Agent

An AI-powered SQL Agent that converts natural language questions into SQL queries using Google's Gemini API and executes them on Microsoft SQL Server.

---

## 📌 Features

- 💬 Ask questions in natural language (Vietnamese or English)
- 🧠 Multi-turn conversation (Context Memory)
- 🤖 AI generates SQL automatically
- ✅ SQL validation before execution
- 🗄 Execute queries on SQL Server
- 📊 Automatically visualize results with charts
- 📥 Export query results to Excel
- ⚡ SQL Cache & Result Cache
- 📝 Query logging
- 🎯 Planner to determine whether a database query is required

---

## 🏗 Project Architecture

```
                User
                  │
                  ▼
             Streamlit UI
                  │
                  ▼
              Planner
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
 General Question      Database Question
        │                   │
        ▼                   ▼
    Gemini API       Generate SQL
                            │
                            ▼
                     SQL Validator
                            │
                            ▼
                     SQL Server
                            │
                            ▼
                    Query Results
                            │
           ┌────────────────┼──────────────┐
           ▼                ▼              ▼
      DataFrame         Chart         Excel Export
                            │
                            ▼
                    Natural Language Answer
```

---

## 🛠 Technologies

- Python
- Google Gemini API
- SQL Server
- SQLAlchemy
- PyODBC
- Streamlit
- Pandas
- OpenPyXL

---

## 📂 Project Structure

```
PROJECT AI AGENT DATABASE
│
├── app.py                 # Streamlit interface
├── LLM.py                 # Gemini API
├── fake_llm.py            # Generate SQL from natural language
├── planner.py             # Determine if database access is required
├── prompt.py              # Prompt templates
├── memory.py              # Conversation history
├── cache.py               # SQL cache & result cache
├── validator.py           # Validate SQL
├── SQLexecutor.py         # Execute SQL
├── databaseconnect.py     # SQL Server connection
├── schema.py              # Read database schema
├── explainer.py           # Explain SQL results
├── visualizer.py          # Draw charts
├── exporter.py            # Export Excel
├── logger.py              # Save query logs
├── utils.py               # Helper functions
│
├── database/
│   └── Qlsv.sql           # Database script
│
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙ Installation

### 1. Clone repository

```bash
git clone https://github.com/cuongle010205/AI-SQL-Agent.git
cd AI-SQL-Agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

Copy `.env.example`

```
GEMINI_API_KEY=YOUR_API_KEY

SERVER=YOUR_SQL_SERVER
DATABASE=YOUR_DATABASE

DRIVER=ODBC Driver 18 for SQL Server
```

Example

```
SERVER=MSI
DATABASE=Qlsv
DRIVER=ODBC Driver 18 for SQL Server
```

---

### 4. Restore database

Restore

```
database/Qlsv.sql
```

using Microsoft SQL Server Management Studio.

---

### 5. Run

```bash
streamlit run app.py
```

---

## 💬 Example Questions

```
Có bao nhiêu sinh viên?

Liệt kê sinh viên khoa Công nghệ thông tin.

Khoa nào có nhiều sinh viên nhất?

Liệt kê 5 sinh viên có điểm cao nhất.

Có bao nhiêu sinh viên theo từng khoa?

Vẽ biểu đồ số sinh viên theo khoa.
```

---

## 📸 Screenshots

Add screenshots here.

```
screenshots/home.png
screenshots/chart.png
screenshots/result.png
```

---

## 🚀 Future Improvements

- Retrieval-Augmented Generation (RAG) for schema retrieval
- Tool Calling
- Multi-Agent workflow
- User Authentication
- Support multiple databases (MySQL, PostgreSQL)
- Docker deployment
- REST API
- Voice interaction
- AI-generated dashboard

---

## 📈 Skills Demonstrated

- Large Language Models (LLM)
- AI Agent
- Prompt Engineering
- Text-to-SQL
- SQL Server
- Streamlit
- Python
- Data Visualization
- Software Engineering

---

## 👨‍💻 Author

**LÊ Cương**

Third-year student in Electronics Physics and Computer Technology

University of Science, VNU-HCM

Interested in AI, LLM Applications, and AI Agents.
