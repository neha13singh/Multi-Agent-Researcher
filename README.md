# 🔬 AI Research Pipeline

AI Research Pipeline is a multi-agent system built with **Streamlit** and **LangChain** that automatically researches, scrapes, and generates comprehensive reports on any given topic. Watch the agents intelligently search the web, read extensive source contents, draft a high-quality report, and finally critique their own work—all live in a beautiful UI!

## 🤖 Agents & Tools Architecture

The heart of the system relies on specialized LangChain agents powered by OpenAI's `gpt-4o-mini`, utilizing custom tools to gather and process information accurately.

### The Agents & Chains
- **Search Agent (`build_search_agent`)**: An autonomous agent designated to accept an open-ended topic and use its tool-calling capabilities to perform live web queries.
- **Reader Agent (`build_reader_agent`)**: Evaluates the output of the Search Agent, picks the most promising/relevant URL, and scrapes its deep content for synthesis.
- **Writer Chain (`writer_chain`)**: A structured LCEL (LangChain Expression Language) pipeline that prompts the LLM to act as an expert research writer. It formats the raw scraped content into a professional report with Key Findings and Sources.
- **Critic Chain (`critic_chain`)**: A strict evaluation LCEL pipeline that reviews the Writer Chain's output. It grades the report out of 10 and provides actionable Strengths, Areas to Improve, and a One-line verdict.

### The Tools
- **`web_search` Tool**: Integrates directly with the `TavilyClient`. This allows the AI to programmatically fetch the top 5 most recent and reliable web results, cleanly returning the Titles, URLs, and Snippets.
- **`scrape_url` Tool**: Uses the `requests` library and `BeautifulSoup4` to deep-scrape full HTML pages. It is equipped to filter out junk tags (like scripts, navbars, and footers) to feed only clean, structured text back to the LLM context window (up to 3000 characters).
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
