import streamlit as st
import requests
import json
import os

st.markdown(
    """
    <style>
    .logo { 
        position: absolute;
        top: 15px;
        left: 15px;
        z-index: 100; 
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.image("Logo_USTBusinessSchool.svg", width=120, output_format="SVG")

st.set_page_config(
    page_title="Semantic Search AI App for BA Users",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("Semantic Search AI App for BA Users")
st.markdown("A Semantic Search App for ISOM 6670G.")

st.subheader("What is your question?")
user_query = st.text_input(
    label="Enter your question:",
    placeholder="e.g., Where is HKUST Business School",
    help="Type your natural language question here."
)

# ------------------------------
# 3️⃣ 提交按钮
# ------------------------------

if st.button("Search"):
    if not user_query:
        st.warning("⚠️ Please enter a question before submitting.")
    else:
        # 构造 payload
        payload = {"query": user_query}

        st.info("Processing...")

        # ------------------------------
        # 4️⃣ 调用后端接口（可选真实API）
        # ------------------------------
        # ❗当有后端API时，放开下方注释：
        # response = requests.post("http://localhost:8000/api/search", json=payload)
        # result = response.json()

        # （课堂作业演示时，可用模拟数据）
        simulated_backend_output = {
            "status": "success",
            "semantic_answer": "Semantic search works by comparing the meaning of your query with document embeddings.",
            "confidence": 0.92
        }

        # ------------------------------
        # 5️⃣ 展示结果
        # ------------------------------
        if simulated_backend_output["status"] == "success":
            st.success("Query Processed Successfully!")
            st.subheader("💡 Semantic Result:")
            st.write(simulated_backend_output["semantic_answer"])
            st.caption(f"Confidence Score: {simulated_backend_output['confidence']}")
        else:
            st.error("Backend returned an error. Please try again.")

# ------------------------------
# 6️⃣ 底部说明
# ------------------------------
st.markdown("""
---
ℹ️ **About this module:**  
This Streamlit front-end handles the *user instruction* part of the AI app:  
- Collects user query  
- Sends it to the backend API (semantic retrieval & LLM logic)  
- Displays the processed answer  

You can integrate it with your backend later to complete the RAG workflow.
""")
