# 💰 Personal Finance Analyzer with Chatbot 🤖

An interactive Streamlit application to analyze personal bank statements and chat with an AI-powered assistant to gain financial insights.

---

## 📌 Features

- 📤 **Upload CSV or Load Sample Data**
- 📊 **Visual Financial Dashboard**
  - Monthly income vs. expenses
  - Balance over time
  - Net savings and key metrics
- 🔍 **Transaction Overview**
  - Total credits/debits
  - Average, highest, and lowest transactions
- 🤖 **AI Chatbot Assistant**
  - Ask questions like:
    - "What was my highest expense?"
    - "How much did I save in March?"
    - "What are my top spending categories?"

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Raqeeb786/personal_finance_tracker
````

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, here’s the list:

```bash
pip install streamlit pandas matplotlib seaborn python-dotenv google-generativeai
```

### 4. Add Your API Key

Generate your Google API key from Google AI studio and Create a `.env` file in the root directory (add your api):

```
GOOGLE_API_KEY= your_gemini_api_key
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📷 Screenshots

### 🧾 Upload or Load Statement

![image](https://github.com/user-attachments/assets/cb96d911-c05a-46f2-a986-9b4afb944e21)
![Screenshot 2025-05-29 123750](https://github.com/user-attachments/assets/9fac0b73-af0a-4e98-b7d1-85b13a3e613c)



### 📊 Financial Dashboard

![Screenshot 2025-05-29 125127](https://github.com/user-attachments/assets/6ebaa5a2-6771-42c7-b4c4-c1322a423021)
![Screenshot 2025-05-29 125147](https://github.com/user-attachments/assets/b3cb6da9-5436-43bf-a702-4a374b469743)


### 🤖 Chatbot Interface

![Screenshot 2025-05-29 125147](https://github.com/user-attachments/assets/e733bf92-0ae5-4576-ae27-3c286a2d835b)
![Screenshot 2025-05-29 125509](https://github.com/user-attachments/assets/bcde70fa-4593-4420-bd38-7e5b53fdf566)


---

## ✨ Future Improvements

* Categorize transactions automatically
* Export analysis to PDF
* Include multi-account comparison
* Persistent chatbot history

---

## 🧠 Powered By

* [Streamlit](https://streamlit.io/)
* [Google Gemini API](https://ai.google.dev/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)

---

## 🙌 Acknowledgments

Thanks to Google for API support, and the Streamlit community for the awesome tools.

``
