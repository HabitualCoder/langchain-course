from dotenv import load_dotenv

load_dotenv()

from langchain import hub
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent



def main():
    print("Hello from langchain-course!")


if __name__ == "__main__":
    main()
