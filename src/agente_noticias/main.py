#!/usr/bin/env python
from agente_noticias.crew import AgenteNoticiasCrew
import sys

input_cmd = sys.argv[1]



def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': input_cmd
    }
    AgenteNoticiasCrew().crew().kickoff(inputs=inputs)