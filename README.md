# 🔬 AI Research Pipeline

AI Research Pipeline is a multi-agent system built with **Streamlit** and **LangChain** that automatically researches, scrapes, and generates comprehensive reports on any given topic. Watch the agents intelligently search the web, read extensive source contents, draft a high-quality report, and finally critique their own work—all live in a beautiful UI!

## 🚀 Features

- **Live Multi-Agent Pipeline:** Watch each step of the pipeline execute in real-time.
- **Search Agent:** Autonomously searches the web to find the most relevant sources for your topic.
- **Reader / Scraper:** Extracts and parses deep content from the selected web pages.
- **Writer Agent:** Synthesizes the parsed information into a highly detailed, structured final report.
- **Critic Agent:** Reviews the generated report to provide a secondary layer of feedback, highlighting potential gaps and improvements.
- **Beautiful UI:** Built with a fully custom, modern Streamlit dark/light theme, featuring dynamic progress tracking, responsive elements, and clean file downloads.
- **Downloadable Outputs:** Easily download the generated report and critiques as a text file for your records.

## 🛠 Prerequisites

To run this application, you will need:
- **Python 3.9+**
- Applicable API keys (e.g., OpenAI API Key, SerpAPI, or Tavily depending on your Langchain setup).

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/multi_agent_system.git
   cd multi_agent_system
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Ensure you have `streamlit`, `langchain`, and the necessary provider libraries in your `requirements.txt`)*

4. **Set your environment variables:**
   Create a `.env` file in the root directory and add your required API keys.
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 🎮 Usage

Launch the Streamlit interface with the below command:

```bash
streamlit run app.py
```

1. Enter your desired **Research Topic** in the main input box.
2. Click **▶ Run**.
3. Watch as the step-by-step progress cards light up, showing which phase the AI is currently executing.
4. Once completed, you can use the action buttons to view the **Final Report**, review the **Critic Feedback**, or directly **Download the Full Report**.

## 🏗 Project Structure

- `app.py`: The Main Streamlit application containing all frontend UI, CSS, and pipeline coordination logic.
- `agents.py`: Contains the LangChain setups, chains, and LLM initializations for the various specialized agents (Search, Reader, Writer, Critic).
- `pipeline.py` / `tools.py` *(if applicable)*: Custom utilities and pipeline handling logic used by the agents.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
