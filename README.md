# learn_langgraph

This repo is created to help set up the environment for the Hackathone about agentic frameworks and in particular the LangGraph framework.


From [LangGraph](https://www.langchain.com/langgraph) documentation:

> LangGraph is a library for building stateful, multi-actor applications with LLMs, used to create agent and multi-agent workflows. Compared to other LLM frameworks, it offers these core benefits: cycles, controllability, and persistence. LangGraph allows you to define flows that involve cycles, essential for most agentic architectures, differentiating it from DAG-based solutions. As a very low-level framework, it provides fine-grained control over both the flow and state of your application, crucial for creating reliable agents. Additionally, LangGraph includes built-in persistence, enabling advanced human-in-the-loop and memory features. LangGraph is inspired by Pregel and Apache Beam. The public interface draws inspiration from NetworkX. LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain.


### Environment Setup

1. Fork the repo.
2. Use any package manager you prefer (I used [uv](https://astral.sh/blog/uv) during development). All dependencies are listed in the `pyproject.toml` file (you can also use `pip install -e`).
3. Explore patterns in the [boilerplate notebook](https://github.com/DmitryKutsev/learn_langgraph/blob/main/boilerplate.ipynb), or experiment with your own ideas.
4. Configure environment variables: Rename `.env_example` to `.env` and add your keys. I used [Together API](https://www.together.ai/) and OpenAI models.
5. Marcus Aurelius quotes: The [markus_quotes.txt](https://github.com/DmitryKutsev/learn_langgraph/blob/main/marcus_quotes.txt) file contains quotes for vector search. You can use assertions and patterns to prompt the agent to respond in a specific tone or for any emotional requests.
6. Set `LANGCHAIN_TRACING_V2=true` if you want to set up integration (logging/tracing, charts etc.) with [LangSmith](https://www.langchain.com/langsmith). Otherwise set `false`.
7. 

### Goals

Is LangGraph suitable for our tasks? Can we use LangGraph independently from LangChain, or are there other tools with similar functionality that we should consider?

Let’s find out!

In the [/utils](https://github.com/DmitryKutsev/learn_langgraph/tree/main/utils) folder, you’ll find templates for various useful tools. The main objective is to build an *agent/agents* while retaining as much control as possible over the output from each tool. Aim to have the LLM return structured outputs such as `json`, `list`, or `str` formats.

**Summary of goals:**

1. Explore options for strict output control by using any agentic framework.
2. LangGraph is preferred but not mandatory.
3. If using LangGraph, try to assess LangGraph’s suitability and its functionality without LangChain.
4. If using another framework, try to compare functionality to LangGraph.
