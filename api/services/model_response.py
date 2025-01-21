import argparse
import json
import sys

from loguru import logger

from api import OPENAI_API_KEY, summarization_prompt
from api.objects.openai_wrapper import OpenAIWrapper


def model_response(model_args: dict):
    logger.info(f"Initializing model")
    openai = OpenAIWrapper(OPENAI_API_KEY)

    logger.info(f"Agent 1: Summarizing news")
    summary_response = openai.summarize_news(model_args["messages"], summarization_prompt)
    summary = summary_response.choices[0].message.content
    logger.info(f"News summary: {summary}")

    logger.info(f"Agent 2: Making investment decision based on summary")
    decision_messages = [{"role": "user", "content": summary}]
    response = openai.create_completion(decision_messages)

    logger.info(f"Final decision: {response}")

    return response


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_args",
        type=json.loads,
        help="Message to be used in the model",
        required=True,
    )
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    try:
        args = parse_arguments()
        model_response(model_args=args.model_args)
    except Exception as e:
        logger.error(f"The pipeline raised the following error: {e}")
        sys.exit(1)
