# 💬 Gemini LLM Agent Chat – Context-Aware AI Assistant

This project is a lightweight, console-based **LLM-powered AI assistant** built using **Google's Gemini 2.5 Pro** via the `google-generativeai` SDK.  
It supports **multi-turn conversations**, retains chat memory, and demonstrates how LLMs can be integrated into real-world, context-aware applications.

---

## 🔍 Features
- ✅ Built with `models/gemini-2.5-pro`
- ✅ Maintains memory across turns (chat history)
- ✅ Uses `.env` for secure API key storage
- ✅ Minimal, extensible codebase
- ✅ Ready to scale with tool use, RAG, or Streamlit UI

---

## 📂 Project Structure
```
llm-agent-chat/
├── app.py                    # Main chatbot logic
├── requirements.txt          # Required Python packages
├── .env                      # Stores Gemini API Key
├── README.md                 # Project info and instructions
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/llm-agent-chat.git
cd llm-agent-chat
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Your API Key
Create a `.env` file in the root folder:
```
GEMINI_API_KEY=your-api-key-here
```

> 🔑 You can get your API key from [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

---

## 💻 Running the App
```bash
python app.py
```

Then chat:
```
💬 Gemini 2.5 Pro AI Chat - Start chatting (type 'exit' to quit):
You: What is LangChain?
Gemini: LangChain is a framework that...
```

---

## 🔧 Technologies Used
- Python 3.8+
- `google-generativeai` SDK
- `.env` for API key handling
- Gemini 2.5 Pro (`models/gemini-2.5-pro`)

---

## 🔮 Future Enhancements
- [ ] Streamlit Web UI
- [ ] Retrieval-Augmented Generation (RAG)
- [ ] LangChain-style prompt chaining
- [ ] Tool-using agents / file analysis

---

## 📜 License
MIT License — free to use and modify.

---

> 🔗 Built for **Heizen SDE (AI) Intern** role  
> By: [Ponnaganti Pavan Kumar](https://github.com/pavan161617)
