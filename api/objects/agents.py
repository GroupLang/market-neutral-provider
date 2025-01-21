from loguru import logger
import openai
from fastapi import HTTPException, status
from openai.error import ServiceUnavailableError

class NewsAgent:
    def __init__(self, api_key, model_name, temperature):
        self.api_key = api_key
        self.model_name = model_name
        self.temperature = temperature
        openai.api_key = self.api_key

    def summarize_news(self, messages, system_prompt):
        messages.insert(0, {"role": "system", "content": system_prompt})
        try:
            return openai.ChatCompletion.create(
                model=self.model_name,
                messages=messages,
                temperature=self.temperature,
            )
        except ServiceUnavailableError as e:
            logger.error(e)
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="OpenAI service unavailable",
            )
        except Exception as e:
            logger.error(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )

class DecisionAgent:
    def __init__(self, api_key, model_name, temperature, system_prompt_tpl):
        self.api_key = api_key
        self.model_name = model_name
        self.temperature = temperature
        self.system_prompt_tpl = system_prompt_tpl
        openai.api_key = self.api_key

    def make_decision(self, message):
        messages = [
            {"role": "system", "content": self.system_prompt_tpl},
            {"role": "user", "content": message}
        ]
        try:
            return openai.ChatCompletion.create(
                model=self.model_name,
                messages=messages,
                temperature=self.temperature,
            )
        except ServiceUnavailableError as e:
            logger.error(e)
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="OpenAI service unavailable",
            )
        except Exception as e:
            logger.error(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal server error",
            )
