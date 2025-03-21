# -*- coding: utf-8 -*-
"""prompts.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dtwJlw8-6t9yHyN-826k2fpDYGD8RsDl
"""

pip install openai

pip install langchain-community

pip install langchain

import os
os.environ["OPENAI_API_KEY"] ="Please generate and place a new OPENAPI Key"

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#zero shot example

from langchain.llms import OpenAI

llm=OpenAI(temperature=1)

text = "Micheal jordon"
print(llm(text))

#one-Shot example

from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate

example =[
    {
        "player":"Micheal Jordon",
        "stats":"""
        dunks:2400, shoes:11""",
    }
]

example_prompt = PromptTemplate(input_variables=["player","stats"],template="player:{player}\n stats:{stats}")
print(example_prompt.format(**example[0]))

Prompt=FewShotPromptTemplate(
    examples=example,
    example_prompt=example_prompt,
    suffix="player:{player}\n stats:",
    input_variables=["player"]
)

print(Prompt.format(player="Micheal Jordon"))

print(llm(Prompt.format(player="Micheal Jordon")))

#Few Shot

examples =[
    {
        "player":"Lewis Hamilton",
        "Nationality":"British",
        "stats":"""
        Championships:7 currentTeam:ferrari""",
    },
     {
        "player":"Max Verstappen",
        "Nationality":"Dutch",
        "stats":"""
        Championships:4 currentTeam:RedBull""",
    },
     {
        "player":"Sergio Perez",
        "Nationality":"Mexican",
        "stats":"""
        Championships:0 currentTeam:Redbull""",
    }


]

example_prompt = PromptTemplate(
    input_variables=["player","Nationality","stats"],
    template="player:{player}\n {Nationality}\n {stats}")
print(example_prompt.format(**example[0]))

Prompt=FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="player:{player}\n",
    input_variables=["player"]
)

print(Prompt.format(player="manideep"))

print(llm(Prompt.format(player="charles")))

#chain of Thoughts

from langchain.chat_models import ChatOpenAI
llm=ChatOpenAI(model="gpt-3.5-turbo",temperature=0)

question="The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1? please show how you got the answer "
print(llm.invoke(question))

