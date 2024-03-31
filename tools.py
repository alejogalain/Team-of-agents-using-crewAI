import os
from exa_py import Exa
from langchain.agents import tool


#Define investments tools
class ExaTools():
    def _exa():
        return Exa(api_key=os.environ.get('EXA_API_KEY'))
    
    #The description is inside the method (not as markdown) because it is what the agent reads to decide whether to use the tool or not
    @tool
    def search(query:str):
        """Search for a webpage based on the query""" 
        return ExaTools._exa().search(f"{query}", use_autoprompt=True, num_results=3)

    @tool
    def find_similar(url:str):
        """Search for webpages similar to a given URL. The URL passed in shiuld be the one returned from 'search'"""
        return ExaTools._exa().find_similar(url, num_results=3)

    @tool
    def get_contents(ids:str):
        """Get the content of a webpage. The ids must be passed in as a list, returned from 'search'"""
        ids = eval(ids)

        contents = str(ExaTools._exa().get_contents(ids))
        contents = contents.split("URL:")
        contents = [content[:1000] for content in contents]
        
        return "\n\n".join(contents)
    
    def tools():
        return [ExaTools.search, ExaTools.find_similar,ExaTools.get_contents]