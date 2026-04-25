from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain
from tools import web_search, scrape_url

def run_research_pipeline(topic:str)->dict:
    #create state which will be accessible to all agents and chains
    state={}
    #step 1
    #search agent working 
    print("\n"+"="*50)
    print("STEP 1 - search agent working ...")
    print("="*50)
    search_agent=build_search_agent()
    search_result=search_agent.invoke({
        "messages":[("user",f"find recent and reliable information on the topic: {topic} using web search tool and return the info in structured format")],

    })
    state["search_results"]=search_result['messages'][-1].content
    print ("\n search result ",state['search_results'])

    #step2
    #reader agent working
    print("\n"+"="*50)
    print("STEP 2 - reader agent is scraping top resources ...")
    print("="*50)
    reader_agent=build_reader_agent()
    reader_results=reader_agent.invoke({
        "messages":[
            (
                "user",
                f"Based on the following search results about '{topic}',"
                f"pick the most relevant URL and scrape it for depper content.\n\n"
                f"Search Results:\n{state['search_results'][:800]}"
            )
        ]
    })
    state["scraped_content"]=reader_results['messages'][-1].content
    print("scraped content \n",state['scraped_content'])

    #step3
    #writer chain working
    print("\n"+"="*50)
    print("STEP 3 - writer is drafting the report ...")
    print("="*50)

    search_combined=(
        f"SEARCH RESULTS:\n {state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT:\n {state['scraped_content']}\n\n"
    )
    state["report"]=writer_chain.invoke(
        {
            "topic":topic,
            "research":search_combined
        }
    )
    print("\n Final report \n",state['report'])
    #step4
    #critic Report
    print("\n"+"="*50)
    print("STEP 4- critic is evaluating the report ...")
    print("="*50)
    state["feedback"]=critic_chain.invoke(
        {
            "report":state['report']
        }
    )
    print("\n Critic's review \n",state['feedback'])

    return state


if __name__=="__main__":
    topic=input("Enter the research topic: ")
    run_research_pipeline(topic)
    







