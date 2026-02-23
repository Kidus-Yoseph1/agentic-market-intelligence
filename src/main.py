#!/usr/bin/env python
import sys
from crew import Agentic_Market_Intelligence

def run(topic: str):
    inputs = {
        'topic': topic
        }
    try:
        result = Agentic_Market_Intelligence().crew().kickoff(inputs=inputs)
        print("Final Strategy Report")
        print(result.raw)
    except Exception as e:
        print(f"An error occured while running the crew: {e}")

