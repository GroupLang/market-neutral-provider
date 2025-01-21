from api import baseline_system_prompt_tpl, model_name, temperature
from .agents import NewsAgent, DecisionAgent

class OpenAIWrapper:
    def __init__(self, api_key):
        self.news_agent = NewsAgent(api_key, model_name, temperature)
        self.decision_agent = DecisionAgent(api_key, model_name, temperature, baseline_system_prompt_tpl)

    def create_completion(self, messages):
        return self.decision_agent.make_decision(messages[0]['content'])

    def summarize_news(self, messages, system_prompt):
        return self.news_agent.summarize_news(messages, system_prompt)
