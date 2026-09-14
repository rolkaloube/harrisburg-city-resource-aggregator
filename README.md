## **Prompt**
Create a tool that helps local citizens with financial or medical needs; find local resources that the city, county or state provides. 

## **Problem**
When in need of financial help regarding living or medical challenges, knowing what resources exist and navigating those resources can be challenging. Not everyone has access to a social worker. Having a system that can reliably act as one and aggregate this information would be very useful. 

## **MVP** 
A centralized system that aggregates public assistance resources available to residents of Dauphin County, the City of Harrisburg, and the Commonwealth of Pennsylvania. The goal is to consolidate scattered financial and medical support information into a single, accessible platform so local citizens can more easily discover and navigate available programs. 

Key MVP Components: 
* Aggregation of financial and medical assistance programs 
* Coverage across city (Harrisburg), county (Dauphin), and state (Pennsylvania) levels 
* Centralized, user-friendly access point for public resources 
* Focus on improving discoverability of government-provided aid 

## **Beyond MVP** 
* Build a way to search for the data needed. 
* Integrate the data into a chatbot that can parse the results. 
* Provide a way for a user to add their current challenge, and the results should be tailored to that specific user. 
* Build a UI that can take in user inputs and displays resources and information  

## Available Resources
* https://harrisburgpa.gov/ 
* https://harrisburgpa.gov/community/community_resources.php
* https://www.dauphincounty.gov/
* https://www.pa.gov/
* https://www.upmc.com/patients-visitors

To access to local AI models...
* https://ollama.com/
* https://ollama.com/library/qwen3.5
* https://docs.ollama.com/capabilities/web-search

For web scraping, check a site for a robots.txt file. if the site does not allow for web scraping, then it is discouraged from attempting to scrape that data.
* https://scrape.do/blog/how-to-check-if-a-website-allows-scraping/
* https://realpython.com/beautiful-soup-web-scraper-python/

For storing data (sql lite)...
* https://www.geeksforgeeks.org/python/python-sqlite/
