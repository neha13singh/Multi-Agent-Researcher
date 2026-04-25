from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser   # ✅ correct
from tools import web_search,scrape_url
import os
from dotenv import load_dotenv
load_dotenv()
#model setup
llm=ChatOpenAI(model="gpt-4o-mini",temperature=0)

#1st agent
def build_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )

#2nd agent
def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )


#writer chain lcel pipeline
writer_prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are an expert research writer.Write clear, Structured and insightful reports "),
        ("human","""Write a detailed research report on the topic below.
        Topic:{topic}
        Research Gathered:
        {research}
        Structure the report as:
        - Introduction
        - Key Findings (minimum 3 well-explained points)
        - Conclusion
        - Sources (list all URLs used for research)
        Be detailed, factual and professsional."""),
    ]
)
#first chain
writer_chain=writer_prompt |llm| StrOutputParser()

#critic chain
critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()


