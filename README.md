# learn_langgraph

This repo is created to help set up the environment for the Hackathone about agentic frameworks and in particular the LangGraph framework.

LangGraph is a library for building stateful, multi-actor applications with LLMs, used to create agent and multi-agent workflows. Compared to other LLM frameworks, it offers these core benefits: cycles, controllability, and persistence. LangGraph allows you to define flows that involve cycles, essential for most agentic architectures, differentiating it from DAG-based solutions. As a very low-level framework, it provides fine-grained control over both the flow and state of your application, crucial for creating reliable agents. Additionally, LangGraph includes built-in persistence, enabling advanced human-in-the-loop and memory features. LangGraph is inspired by Pregel and Apache Beam. The public interface draws inspiration from NetworkX. LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain.

Is it suitable for our tasks?

Can we use LangGraph without LangChain?

Can we use something else with similar functional?

### Environment setup

1. Clone the repo.
2. During the development UV packet manager was used. You can take it here and install everything:
   Otherwise just use pip install -e
3. Run something.
4. keys in .env_example
5. setup
