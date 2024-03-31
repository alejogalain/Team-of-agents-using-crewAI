from dotenv import load_dotenv
from crewai import Crew
from tasks import InvestmentTasks
from agents import InvestmentAgents


def main():
    load_dotenv()

    #User's input: company of interest
    company = input("What company do you want to analyze?\n")

    #Initialize agents and tasks object
    agents = InvestmentAgents()
    tasks = InvestmentTasks()

    #Create agents
    researcher_agent = agents.researcher()
    financial_agent = agents.financial()
    advisor_agent = agents.advisor()

    #Create tasks
    research_task = tasks.research(researcher_agent, company)
    financial_task = tasks.analyze(financial_agent, company)
    advise_task = tasks.advise(advisor_agent, company)

    advise_task.context = [research_task, financial_task] #The output of th research and financial task is used as context for the advise task

    #Create crew
    crew = Crew(
        agents=[
            researcher_agent,
            financial_agent,
            advisor_agent
            ],
        tasks=[
            research_task,
            financial_task,
            advise_task
            ]
        )
    
    result = crew.kickoff()

    print(result)

if __name__ == "__main__":
    main()