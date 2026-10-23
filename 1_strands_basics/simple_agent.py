from strands import Agent

# TODO: Step 1 - Add debug logging to see what your agent is thinking
import logging

# Configure the root strands logger
logging.getLogger("strands").setLevel(logging.DEBUG)

# Add a handler to see the logs
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

# TODO: Step 2 - Create the agent with the following system prompt: "You are a game master for a fantasy role-playing game"
agent = Agent(system_prompt = ("You are a game master for a fantasy role-playing game"))

# TODO: Step 3 - Invoke your agent with a basic query such as "Hi, I am an adventurer ready for adventure!"
agent = Agent()
agent("Why would I use Strands over LangGraph?")