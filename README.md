<img width="1162" height="803" alt="image" src="https://github.com/user-attachments/assets/bf3c8673-f029-4105-a4d7-2f51be197835" />


#  AI-Powered CSV Assistant

An interactive AI-powered CSV analytics assistant built using Python, Streamlit, FAISS, and SentenceTransformers.

This project is currently focused on analyzing an employee analytics dataset containing:
- Employee names
- Departments
- Salaries
- Years of experience

The assistant allows users to upload the dataset, ask natural language questions, generate analytics, and visualize insights through charts inside a chat-style interface.

---

#  Features

- Upload and analyze employee CSV datasets  
- Ask natural language questions about employee data  
- Interactive AI-style chat interface  
- Dataset summary generation  
- Salary analytics and employee insights  
- Automatic salary chart generation  
- Chat history support  
- Modern Streamlit UI  

---

# How It Works

The application follows a Retrieval-Augmented Generation (RAG)-inspired workflow:

1. CSV data is loaded using Pandas
2. Rows are converted into text format
3. SentenceTransformers generate embeddings
4. FAISS stores embeddings for semantic retrieval
5. User queries are processed through chatbot logic
6. Streamlit provides an interactive frontend

---

#  Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- FAISS
- SentenceTransformers
- Matplotlib

---

#  Project Structure

```bash
ai-csv-assistant/
│
├── app.py
├── chatbot.py
├── requirements.txt
└── README.md



