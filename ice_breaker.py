import os
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

## from third_parties.linkedin import scrape_linkedin_profile


information = """
Elon Reeve Musk (/ˈiːlɒn/; born June 28, 1971) is a businessman and investor known for his key roles in space company SpaceX and automotive company Tesla, Inc. Other involvements include ownership of X Corp., formerly Twitter, and his role in the founding of The Boring Company, xAI, Neuralink and OpenAI. He is one of the wealthiest people in the world; as of July 2024, Forbes estimates his net worth to be US$221 billion.[4] 
"""

if __name__ == "__main__":
    load_dotenv()

    print("Hello Jorge  - Lab Langchain")
    print(os.environ['OPENAI_API_KEY'])

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them

    Give me the reply using bullets points.
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], 
                                             template=summary_template)

    llm = ChatOpenAI(temperature=0, 
                     model_name="gpt-3.5-turbo")

#    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    chain = summary_prompt_template | llm

##     linkedin_data = scrape_linkedin_profile(
##         linkedin_profile_url="https://www.linkedin.com/in/eden-marco/"
##     )

    res = chain.invoke(input={"information": information})

    print(res)