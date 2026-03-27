import nltk
nltk.download('punkt')

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from PyPDF2 import PdfReader
import numpy as np

import requests
from bs4 import BeautifulSoup

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')


# =========================
# 📄 PDF Reader
# =========================
def read_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + " "
    return text


# =========================
# ✂ Sentence Split
# =========================
def get_sentences(text):
    return nltk.sent_tokenize(text)


# =========================
# 🧠 SIMILARITY
# =========================
def compute_similarity(doc1, doc2):
    s1 = get_sentences(doc1)
    s2 = get_sentences(doc2)

    if len(s1) == 0 or len(s2) == 0:
        return None, None, None

    e1 = model.encode(s1)
    e2 = model.encode(s2)

    if len(e1) == 0 or len(e2) == 0:
        return None, None, None

    sim_matrix = cosine_similarity(e1, e2)
    return s1, s2, sim_matrix


def overall_similarity(sim_matrix):
    if sim_matrix is None or not isinstance(sim_matrix, np.ndarray) or sim_matrix.size == 0:
        return 0
    return sim_matrix.max(axis=1).mean()


def highlight_matches(s1, s2, sim_matrix, threshold=0.7):
    matches = []
    for i in range(len(s1)):
        for j in range(len(s2)):
            if sim_matrix[i][j] > threshold:
                matches.append((s1[i], s2[j], sim_matrix[i][j]))
    return matches


# =========================
# 🌐 WEB SEARCH
# =========================
def search_web(query):
    url = "https://duckduckgo.com/html/"
    params = {"q": query}

    try:
        response = requests.post(url, data=params)
        soup = BeautifulSoup(response.text, "html.parser")

        links = []
        for a in soup.find_all("a", {"class": "result__a"}, href=True):
            links.append(a["href"])
            if len(links) >= 5:
                break

        return links
    except:
        return []


def extract_web_text(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()
    except:
        return ""


def check_web_plagiarism(input_text):
    links = search_web(input_text[:200])

    results = []

    for link in links:
        web_text = extract_web_text(link)

        if web_text.strip():
            s1, s2, sim = compute_similarity(input_text, web_text)
            score = overall_similarity(sim)
            results.append((link, score))

    return results


# =========================
# 🤖 AI DETECTION
# =========================
def detect_ai_content(text):
    sentences = get_sentences(text)

    if len(sentences) == 0:
        return 0

    avg_len = sum(len(s.split()) for s in sentences) / len(sentences)
    long_sentences = sum(1 for s in sentences if len(s.split()) > avg_len)

    score = (long_sentences / len(sentences)) * 100
    return round(score, 2)


# =========================
# 📄 REPORT GENERATION
# =========================
def generate_plagiarism_report(score, matches, filename="plagiarism_report.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []
    content.append(Paragraph(f"Plagiarism Score: {score:.2f}%", styles['Title']))

    for m in matches:
        content.append(Paragraph(f"Sentence 1: {m[0]}", styles['Normal']))
        content.append(Paragraph(f"Sentence 2: {m[1]}", styles['Normal']))
        content.append(Paragraph(f"Similarity: {m[2]*100:.2f}%", styles['Normal']))
        content.append(Paragraph(" ", styles['Normal']))

    doc.build(content)
    return filename


def generate_ai_report(ai_score, filename="ai_report.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []
    content.append(Paragraph("AI Content Detection Report", styles['Title']))
    content.append(Paragraph(f"AI Probability: {ai_score}%", styles['Normal']))

    doc.build(content)
    return filename