#Removes any common leading whitespace from each line in a string. 
#It is useful when working with multi-line strings where indentation is used for readability but is not meant programmatically
from textwrap import dedent 

#Tasks are individual assignments that agents complete. 
#The task module has the following main attributes:
    #Description: A clear, concise statement of what the task entails.
    #Agent: Specify which agent is responsible for the task.
    #Output: Clear and detailed definition of expected output for the task.
    #Async: Indicates whether the task should be executed asynchronously. 
    #Context: Other tasks that will have their output used as context for this task. The context is defined in the main.py
from crewai import Task 


# Define investment tasks
class InvestmentTasks():
    
    def research(self, agent, company):
        return Task(
            description=dedent(f"""
            Collect and summarize recent news articles, press releases
            and market analyses related to the {company} and its industry.
            Pay special attention to any significant events, market sentiment
            and analysts opinions."""),
            expected_output=dedent(f"""
            A detailed report that includes a comprehensive summary of the latest
            news, any notable shifts in market sentiment and its potential impact on 
            the stock"""),
            agent=agent,
            async_execution=True)

    def analyze(self, agent, company):
        return Task(
            description=dedent(f"""
            Conduct a thorough analysis of the {company} financial health and market 
            performance.
            This includes examining key financial metrics such as:  Revenue Growth, Profit Margin, 
            Cash flow, Debt to Equity ratio, Return on Equity (ROE), Earnings per Share (EPS),
            Price to Earnings ratio (P/E), Price to Book Ratio (P/B), Dividend Yield.
            Also analyze the stock's performance in comparison to its industry peers and overall
            market trends."""),
            expected_output=dedent(f"""
            A detailed report that expands on the summary provided by the Reasercher, now including a 
            clear assessment of the stock's financials, its strength and weaknesses, and how it stands 
            against its competitors in the current market scenario."""),
            agent=agent,
            async_execution=True)
    
    def advise(self, agent, company):
        return Task(
            description=dedent(f"""
            Review and synthesize the analyses provided by the Reasearcher and the Financial Analyst.
            Combine these insights to form a comprehensive investment recommendation for the {company}.
            You must consider all aspects: financial health and market sentiment."""),
            expected_output=dedent(f"""
            A detailed recommendation for your customer. It should be a detailed report, providing a 
            clear investment strance and strategy with supporting evidence for the {company}."""),
            agent=agent,
            async_execution=False)
                                                                         


        

            
           
               





