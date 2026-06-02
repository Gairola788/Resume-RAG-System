print("1")

from langchain_text_splitters import RecursiveCharacterTextSplitter

print("2")

def chunk_text(text: str):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )
    
    chunks = splitter.split_text(text)
    
    return chunks

resume = '''AKSHAT GAIROLA
Email: akshat@example.com
Phone: +91-9876543210
LinkedIn: linkedin.com/in/akshatgairola
GitHub: github.com/Gairola788

--------------------------------------------------
PROFESSIONAL SUMMARY
--------------------------------------------------

Computer Science Engineering student specializing in AI/ML with hands-on experience in NLP, Machine Learning, FastAPI, LangChain, and Agentic AI systems. Passionate about building intelligent applications using LLMs, RAG pipelines, and vector databases.

--------------------------------------------------
SKILLS
--------------------------------------------------

Programming Languages:
Python, Java, C++, SQL

AI / Machine Learning:
Scikit-Learn, XGBoost, NLP, Deep Learning

LLM & Agentic AI:
LangChain, LangGraph, RAG, Prompt Engineering, Tool Calling

Backend:
FastAPI, REST APIs

Databases:
MySQL, FAISS, ChromaDB

Tools:
Git, GitHub, VS Code, Postman

--------------------------------------------------
EDUCATION
--------------------------------------------------

Graphic Era Hill University
B.Tech in Computer Science Engineering (AI/ML)

CGPA: 7.5

Expected Graduation: 2027

--------------------------------------------------
PROJECTS
--------------------------------------------------

1. AI Resume Screener

Developed an intelligent resume screening system that evaluates resumes against job descriptions.

Features:
- TF-IDF similarity scoring
- Semantic similarity using sentence transformers
- Weighted skill matching
- Resume ranking system

Technologies:
Python, Scikit-Learn, FastAPI, Sentence Transformers

--------------------------------------------------

2. Multi Tool AI Assistant

Built an AI assistant capable of dynamically selecting tools based on user queries.

Implemented:
- Calculator Tool
- Weather Tool
- Internet Search Tool
- Conversation Memory

Technologies:
Python, LangChain, FastAPI, Streamlit, Groq API

--------------------------------------------------

3. Resume RAG System

Designed a Retrieval-Augmented Generation system that allows recruiters to query resumes using natural language.

Implemented:
- PDF Parsing
- Text Chunking
- Embedding Generation
- Vector Search
- Context Retrieval

Technologies:
Python, FAISS, LangChain, Sentence Transformers

--------------------------------------------------
INTERNSHIP EXPERIENCE
--------------------------------------------------

AI Engineering Intern

Worked on developing NLP pipelines for document processing and information retrieval.

Responsibilities:
- Text preprocessing
- Embedding generation
- Similarity search
- API development

Duration:
May 2025 - July 2025

--------------------------------------------------
CERTIFICATIONS
--------------------------------------------------

Machine Learning Specialization

Deep Learning Fundamentals

Prompt Engineering for Developers

--------------------------------------------------
ACHIEVEMENTS
--------------------------------------------------

- Built multiple end-to-end AI applications.
- Participated in AI hackathons.
- Published technical content on LinkedIn related to Agentic AI and RAG systems.

--------------------------------------------------
INTERESTS
--------------------------------------------------

Artificial Intelligence
Large Language Models
Agentic AI
Backend Development
Machine Learning Systems'''

print(chunk_text(resume))