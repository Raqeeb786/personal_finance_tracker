import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import time
import random

# --- SETUP ---
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Session state initialization
if 'chat' not in st.session_state:
    model = genai.GenerativeModel("gemini-1.5-flash-001")
    st.session_state.chat = model.start_chat()
if 'df' not in st.session_state:
    st.session_state.df = None
if 'data' not in st.session_state:
    st.session_state.data = None

# --- HEADER ---
st.set_page_config(layout="wide")
st.title("💰 Personal Finance Analyzer 📊 & Chatbot 🤖")
st.markdown("Upload your **bank statement CSV** or load a sample data to begin.")

with st.sidebar.markdown("ℹ️ About this App"):
    st.markdown("""
    This app analyzes personal finance data from bank statements.
    - Upload CSV or load a sample
    - View dashboard metrics and charts
    - Ask questions via the chatbot
    """)
# --- CSS STYLING ---
st.markdown("""
    <style>
        .stApp {
            background-color: #f0f2f5;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# --- UPLOAD SECTION ---
col1, col2 = st.columns([3, 1])
with col1:
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
with col2:
    if st.button("📁 Load Sample Data"):
        num= str(random.randint(1, 3))
        with open("statement"+num+".json", "r") as f:
            data = json.load(f)
            st.session_state.df = pd.json_normalize(data['transactions'])
            st.session_state.data = data
            st.success("Sample data loaded!")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.session_state.df = df
        st.session_state.data = {
            "accountHolder": {
                "name": "Uploaded File",
                "accountNumber": "-",
                "bankName": "-",
                "currency": "INR"
            },
            "statementPeriod": {
                "startDate": "-",
                "endDate": "-"
            }
        }
        st.success("CSV file loaded.")
    except Exception as e:
        st.error(f"Error: {e}")

df = st.session_state.df
data = st.session_state.data

# --- DETAILS SECTION ---
if df is not None and data is not None:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df.dropna(subset=['date'], inplace=True)

    st.spinner("Analyzing data...")
    time.sleep(2)  # Simulate processing time
    st.session_state.df = df  # Update session state with processed DataFrame
    st.session_state.data = data  # Update session state with data
    st.success("Data processed successfully!")
    st.markdown("### 📄 Transaction Details")
    st.dataframe(df.head(), use_container_width=True)

    st.markdown("---")
    st.subheader("👤 Account Summary")
    acc_col, date_col = st.columns(2)

    with acc_col:
        st.markdown("**Account Details**")
        st.write(f"**Name:** {data['accountHolder']['name']}")
        st.write(f"**Account Number:** {data['accountHolder']['accountNumber']}")
        st.write(f"**Bank:** {data['accountHolder']['bankName']}")
        st.write(f"**Currency:** {data['accountHolder']['currency']}")

    with date_col:
        st.markdown("**Statement Period**")
        st.write(f"**Start:** {data['statementPeriod']['startDate']}")
        st.write(f"**End:** {data['statementPeriod']['endDate']}")
        st.write(f"**Duration:** {df['date'].min().date()} to {df['date'].max().date()}")


#tab1, tab2 = st.tabs(["📊 Dashboard", "🤖 Finance Chatbot"])
tab1, tab2 = st.tabs([
    "📊 **FINANCIAL DASHBOARD ( Insights + Visualizations )**",
    "🤖 **CHAT WITH FINBOT ( AI Assistant )**"
])
with tab1:
    # --- KEY INSIGHTS ---
    if df is not None:
        st.markdown("---")
        st.subheader("📊 Financial Dashboard")

        total_income = df[df['type'] == 'credit']['amount'].sum()
        total_expense = df[df['type'] == 'debit']['amount'].sum()
        net_savings = total_income - total_expense

        m1, m2, m3 = st.columns(3)
        m1.metric("Total Income", f"{total_income:,.2f} {data['accountHolder']['currency']}")
        m2.metric("Total Expense", f"{total_expense:,.2f} {data['accountHolder']['currency']}")
        m3.metric("Net Savings", f"{net_savings:,.2f} {data['accountHolder']['currency']}", delta=f"{net_savings:,.2f}")

        # --- VISUALIZATION ---
        df['month'] = df['date'].dt.to_period('M').astype(str)
        monthly = df.groupby(['month', 'type'])['amount'].sum().unstack().fillna(0)

        vcol1, vcol2 = st.columns(2)

        with vcol1:
            st.markdown("**📅 Monthly Summary**")
            fig1, ax1 = plt.subplots(figsize=(6, 3))
            monthly.plot(kind='bar', ax=ax1, width=0.6)
            ax1.set_ylabel("Amount")
            ax1.set_title("Monthly Income vs Expense")
            st.pyplot(fig1)



        with vcol2:
            st.markdown("**💸 Balance over Time**")
            fig2, ax2 = plt.subplots(figsize=(5, 3))
            df.plot(x='date', y='balance', ax=ax2, color='blue')
            ax2.set_xlabel("Date")
            ax2.set_ylabel("Balance")
            ax2.set_title("Balance Over Time")
            st.pyplot(fig2)
        st.markdown("---")

        st.markdown("#### 🔍 Summary")
        col1, col2 = st.columns(2)
        with col2:
            
            st.write(f"- Total Income: ₹{total_income:,.2f}")
            st.write(f"- Total Expense: ₹{total_expense:,.2f}")
            st.write(f"- Net Savings: ₹{net_savings:,.2f}")
            st.write(f"- Average Monthly Income: ₹{monthly['credit'].mean():,.2f}")
            st.write(f"- Average Monthly Expense: ₹{monthly['debit'].mean():,.2f}")
            st.write(f"- Average Monthly Savings: ₹{(monthly['credit'] - monthly['debit']).mean():,.2f}")
        with col1:
            st.write(f"- Total Transactions: {len(df)}")
            st.write(f"- Total Credit Transactions: {len(df[df['type'] == 'credit'])}")
            st.write(f"- Total Debit Transactions: {len(df[df['type'] == 'debit'])}")
            st.write(f"- Lowest Transaction: ₹{df['amount'].min():,.2f}")
            st.write(f"- Highest Transaction: ₹{df['amount'].max():,.2f}")
            st.write(f"- Average Transaction: ₹{df['amount'].mean():,.2f}")
            
with tab2:
    # --- CHATBOT ---
    if df is not None:
        st.markdown("---")
        st.subheader("🤖 Ask About Your Finances")
        st.markdown("You can ask questions about your transaction history, such as:")
        st.markdown("- What is my total income?")
        st.markdown("- How much did I spend on UPI last month?")
        st.markdown("- What are my top 5 expenses?")
        question = st.text_input("Type a question about your transaction history:")
        if st.button("💬 Get Answer"):
            with st.spinner("Analyzing with Gemini..."):
                try:
                    prompt = (
                        f"Here is the user's transaction dataset:\n{df.to_string(index=False)}\n\n"
                        f"The user asks: {question}\n"
                        "Please analyze and answer clearly based on the data."
                    )
                    response = st.session_state.chat.send_message(prompt)
                    st.markdown("**💬 Chatbot Response:**")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"Chatbot error: {e}")
