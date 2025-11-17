import streamlit as st
import requests
import json

# ------------------------------
# 1️⃣ 页面基本设置
# ------------------------------
st.set_page_config(
    page_title="Semantic Search AI App",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("🔍 Semantic Search AI App")
st.markdown("This demo allows you to ask questions in **natural language** and get semantic search results.")

# ------------------------------
# 2️⃣ 用户输入区域
# ------------------------------
st.subheader("🗣️ Step 1: Type your question")

# 文本输入框
user_query = st.text_input(
    label="Enter your question:",
    placeholder="e.g., What is semantic search?",
    help="Type your natural language question here."
)

# ------------------------------
# 3️⃣ 提交按钮
# ------------------------------

if st.button("🔎 Submit Query"):
    if not user_query:
        st.warning("⚠️ Please enter a question before submitting.")
    else:
        # 构造 payload
        payload = {"query": user_query}

        st.info("Sending your query to the backend for processing...")

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
            st.success("✅ Query processed successfully!")
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
