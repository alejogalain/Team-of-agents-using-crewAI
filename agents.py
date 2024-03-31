from textwrap import dedent

#An agent is an autonomous unit programmed to perform tasks and making decisions.
#The agent module has the following main attributes:
    #Role: Defines the agent's function within the crew. It determines the kind of tasks the agent is best suited for.
    #Goal: The individual objective that the agent aims to achieve. It guides the agent's decision-making process.
    #Backstory: Provides context to the agent's role and goal, enriching the interaction and collaboration dynamics.
    #Verbose: Enables detailed logging of the agent's execution
    #Tools: Set of capabilities or functions that the agent can use to perform tasks. 
from crewai import Agent 

from tools import ExaTools

#Define investment agents
class InvestmentAgents():
    def researcher(self):
        return Agent(
            role="Research Analyst",
            goal="Gather and analyze company's data",
            backstory="The best research analyst, specialized in analyzing news, company announcements and market sentiments",
            verbose=True,
            tools=ExaTools.tools())

    def financial(self):
        return Agent(
            role="Financial Analyst",
            goal="Gather and analyze financial data",
            backstory="The best financial analyst, specialized in stock markets and investment strategies",
            verbose=True,
            tools=ExaTools.tools())
    
    #The investor does not need tools, the context for his investment recommendation comes from the analysts.
    def advisor(self):
        return Agent(
            role="Investment Advisor",
            goal="Make investment recommendations for stocks",
            backstory="You're the most experienced investment advisor and you combine various analytical insights to formulate strategic investment advice.",
            verbose=True)

        
                            

        