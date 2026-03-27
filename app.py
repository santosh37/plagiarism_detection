import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from plagiarism_model import (
    compute_similarity,
    overall_similarity,
    highlight_matches,
    read_pdf,
    check_web_plagiarism,
    detect_ai_content,
    generate_plagiarism_report,
    generate_ai_report
)

from database import save_doc

st.set_page_config(page_title="Plagiarism Detector", layout="wide")

st.title("AI Plagiarism Detection System")

mode = st.sidebar.radio("Select Mode", ["File Comparison", "Web Comparison"])
threshold = st.sidebar.slider("Similarity Threshold", 0.0, 1.0, 0.7)


# =========================
# 📄 FILE MODE
# =========================
if mode == "File Comparison":

    col1, col2 = st.columns(2)

    with col1:
        file1 = st.file_uploader("Upload Document 1", type=["pdf", "txt"])

    with col2:
        file2 = st.file_uploader("Upload Document 2", type=["pdf", "txt"])

    def extract_text(file):
        if file.name.endswith(".pdf"):
            return read_pdf(file)
        return file.read().decode("utf-8")

    if st.button("Check Plagiarism"):

        if file1 and file2:

            text1 = extract_text(file1)
            text2 = extract_text(file2)

            save_doc(file1.name, text1)
            save_doc(file2.name, text2)

            s1, s2, sim = compute_similarity(text1, text2)

            if sim is None:
                st.error("Unable to compute similarity.")
                st.stop()

            score = overall_similarity(sim)
            percentage = round(score * 100, 2)

            st.subheader(f"Similarity Score: {percentage}%")
            st.progress(int(percentage))

            # Graph
            fig1 = plt.figure()
            plt.bar(["Similarity"], [percentage])
            plt.title("Overall Similarity Score")
            st.pyplot(fig1)

            # AI Detection
            ai_score = detect_ai_content(text1)
            st.subheader(f"AI Content Probability: {ai_score}%")

            # Matches
            matches = highlight_matches(s1, s2, sim, threshold)

            for m in matches:
                st.markdown(f"""
                <div style="background-color:#ffe6e6;padding:10px;border-radius:5px">
                <b>Sentence 1:</b> {m[0]} <br>
                <b>Sentence 2:</b> {m[1]} <br>
                <b>Similarity:</b> {m[2]*100:.2f}%
                </div>
                """, unsafe_allow_html=True)

            # Reports
            plag_file = generate_plagiarism_report(percentage, matches)
            ai_file = generate_ai_report(ai_score)

            with open(plag_file, "rb") as f:
                st.download_button("Download Plagiarism Report", f, file_name=plag_file)

            with open(ai_file, "rb") as f:
                st.download_button("Download AI Report", f, file_name=ai_file)

        else:
            st.warning("Upload both documents")


# =========================
# 🌐 WEB MODE
# =========================
elif mode == "Web Comparison":

    option = st.radio("Input Type", ["Paste Text", "Upload File"])

    def extract_text(file):
        if file.name.endswith(".pdf"):
            return read_pdf(file)
        return file.read().decode("utf-8")

    text = None

    if option == "Paste Text":
        text = st.text_area("Enter text")

    else:
        file = st.file_uploader("Upload file", type=["pdf", "txt"])
        if file:
            text = extract_text(file)

    if st.button("Check Web Plagiarism"):

        if text and text.strip():

            st.info("Searching web...")

            # 🔍 Web results
            results = check_web_plagiarism(text)

            # 🤖 AI Detection (NEW)
            ai_score = detect_ai_content(text)
            st.subheader(f"AI Content Probability: {ai_score}%")

            if results:
                st.subheader("Web Results")

                scores = []
                labels = []

                for link, score in results:
                    percentage = round(score * 100, 2)
                    scores.append(percentage)
                    labels.append(link[:25])

                    st.markdown(f"""
                    <div style="background-color:#e6f2ff;padding:10px;border-radius:5px">
                    <b>Source:</b> {link} <br>
                    <b>Similarity:</b> {percentage}%
                    </div>
                    """, unsafe_allow_html=True)

                # 📊 Graph
                import matplotlib.pyplot as plt
                fig = plt.figure()
                plt.barh(labels, scores)
                plt.title("Web Similarity Comparison")
                st.pyplot(fig)

            else:
                st.warning("No matches found.")

            # =========================
            # 📥 AI REPORT DOWNLOAD (NEW)
            # =========================
            ai_file = generate_ai_report(ai_score)

            with open(ai_file, "rb") as f:
                st.download_button("🤖 Download AI Report", f, file_name=ai_file)

        else:
            st.warning("Provide input text or file.")