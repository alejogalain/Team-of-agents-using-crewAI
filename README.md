# Team-of-agents-using-crewAI
The goal of this project is to create a team of autonomous AI agents that advise the user on invesments, using:
- **CrewAi** a new framework for orchestrating autonomous AI agents. 
- **Exa** provides search for AI. The LLM can search using natural language from Exa's neural database.

Before kickstarting our crew, we are going to ask the user for the company they are interested in investing.
In return, the team of AI agents will wotk together to provide an investment recommendation.

Some key concepts:
- **Crew**: represents a collaborative group of agents working together to achieve a set of tasks for a specific goal.
- **Tasks**: These are the tasks that our agents will perform. Each task will be assigned to an agent.
- **Agents**: These are the AI agents that will be working for us. Each agent is an expert in a different task. 
- **Tools**: These are the tools that our agents will use to perform their tasks. In this case, they will use a serach engine.
- **Process**: A process dictates the way that our agents will work together. In this case, we will use a sequential process.

### How agents think?
Agents can think for themselves and complete their tasks without us having to tell them what steps to take. All they need is an initial prompt telling them what we expect from them.

In order to do this, they follow the following steps in a loop:
1. **Thought**: Given some context, they use the LLM to “think” what would be the right action to take.
2. **Action**: Given the thought that they just had, they use the LLM again to formulate the action that they want to perform. They choose this action out of a defined list of possible actions. These actions are declared when creating the agent.
3. **Action input**: Each action is essentially a function, so we need to pass an input. The action might be "search the web", so it will take a search query.
4. **Observation**: The agent will then perform the action and give us back the result. This result is called an observation. In the case of the “search the web” action, the observation would be the search results.

After the first iteration, the agent will take the observation, append it to the context, and then repeat the loop. If at any point the agent thinks that it has completed the task, it’s thought will be something like “I now have all the information that I need to complete the task”. At this point, the agent will stop the loop and give us the final result.
