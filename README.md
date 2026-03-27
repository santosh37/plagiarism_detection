# plagiarism_detection
“AI-powered plagiarism detection system using NLP and transformer models with semantic similarity, web comparison, AI content detection, visualization, and PDF report generation.”
# 🚀 AI-Based Plagiarism Detection System

## 📌 Overview

The **AI-Based Plagiarism Detection System** is an intelligent application that detects both **exact and semantic plagiarism** using Natural Language Processing (NLP) and Machine Learning techniques.

It also includes **AI-generated content detection**, **web-based plagiarism checking**, and **automated PDF report generation**, making it a complete academic integrity solution.

---

## ✨ Key Features

### 🔍 Plagiarism Detection

* Detects **semantic similarity** using transformer-based models
* Works on **text files and PDF documents**
* Highlights **matching sentences**
* Provides **similarity percentage (%)**

### 🌐 Web-Based Detection

* Compares input content with **online sources**
* Displays similarity with multiple websites
* Visual comparison using graphs

### 🤖 AI Content Detection

* Identifies probability of **AI-generated text**
* Uses heuristic-based analysis
* Generates a **separate AI detection report**

### 📊 Visualization

* 📈 Similarity distribution graphs
* 📊 Overall score representation
* 📉 Web comparison charts

### 📄 Report Generation

* Downloadable **Plagiarism Report (PDF)**
* Downloadable **AI Detection Report (PDF)**

### 💻 User Interface

* Built with **Streamlit**
* Clean and responsive dashboard
* File upload and real-time results

---

## 🧠 Technologies Used

* **Programming Language:** Python
* **Libraries & Frameworks:**

  * `sentence-transformers` (BERT-based embeddings)
  * `scikit-learn` (cosine similarity)
  * `NLTK` (text preprocessing)
  * `Streamlit` (UI development)
  * `Matplotlib` (visualization)
  * `BeautifulSoup` (web scraping)
  * `ReportLab` (PDF generation)
  * `PyPDF2` (PDF reading)

---

## 📁 Project Structure

```
plagiarism_detection/
│
├── app.py                  # Main Streamlit application
├── plagiarism_model.py     # Core AI + ML logic
├── database.py             # Data storage (SQLite)
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
│
├── data/                   # Sample dataset
│   ├── doc1.txt
│   ├── doc2.txt
│   └── doc3.txt
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone <your-repo-link>
cd plagiarism_detection
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
python -m streamlit run app.py
```

Then open in browser:
👉 http://localhost:8501

---

## 🧪 How It Works

1. Input document (text or PDF)
2. Text preprocessing (tokenization)
3. Sentence embedding using **Sentence Transformers**
4. Similarity calculation using **cosine similarity**
5. Output:

   * Similarity score
   * Highlighted matches
   * Graph visualization
   * Downloadable reports

---

## 📊 Output Example

* Similarity Score: **85%**
* AI Content Probability: **42%**
* Highlighted matched sentences
* Graphs showing similarity distribution

---

## 🎯 Applications

* Academic institutions (assignment checking)
* Research paper validation
* Content originality verification
* AI-generated content detection

---

## ⚠️ Limitations

* Web comparison uses **public data only**
* Does not access paid databases (e.g., IEEE, Scopus)
* AI detection is **heuristic-based (not perfect)**

---

## 🚀 Future Enhancements

* Deep learning-based AI detection
* Integration with academic databases
* Multi-language plagiarism detection
* Cloud deployment
* User authentication system

---

## 🎤 Viva Summary

> This system uses NLP and transformer-based embeddings to detect semantic plagiarism, integrates web-based comparison, visual analytics, and generates automated reports for both plagiarism and AI content detection.

---

## 👨‍💻 Author

**Santosh Prakash Shinde**
M.Sc. Computer Science

---

## ⭐ Conclusion

This project demonstrates the practical application of **AI, NLP, and data visualization** to solve real-world problems related to academic integrity and content originality.

---
