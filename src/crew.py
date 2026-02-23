import os
from crewai import Agent, Task, Process, Crew, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from tools.github_tool import github_repo_auditor


@CrewBase
class Agentic_Market_Intelligence():
    "Agentic market intelligence crew"
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self):
        self.llm = LLM(
            model = os.getenv("MODEL_NAME"),
            api_key = os.getenv("GROQ_API_KEY"),
            temperature = 0.5
            )
        
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config = self.agents_config['researcher'], 
            verbose= True,
            tools = [SerperDevTool()],
            llm = self.llm,
            # max_rpm=10,
            function_calling_llm=self.llm
            )
    
    @agent
    def auditor(self) -> Agent:
        return Agent(
            config = self.agents_config['auditor'],
            verbose = True,
            llm=self.llm,
            tools = [github_repo_auditor]
            )
    
    @agent
    def manager(self) -> Agent:
        return Agent(
            config = self.agents_config['manager'],
            verbose = True,
            llm=self.llm
            )
    
    @task
    def research_task(self) -> Task:
        return Task(
            config = self.tasks_config['research_task']
        )

    @task
    def technical_audit_task(self) -> Task:
        return Task(
            config = self.tasks_config['technical_audit_task']
        )
    
    @task
    def strategy_synthesis_task(self) -> Task:
        return Task(
            config = self.tasks_config['strategy_synthesis_task']
        )

    @crew
    def crew(self) ->Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            manager_llm= self.llm,
            planning= False
        )


