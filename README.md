# Prompts-in-GEnai
LangChain Fundamentals - Study prompt engineering to improve AI response quality.


Have you ever wondered “What Is Prompt?” (or ) “Say Why is prompt More important in GenAi or LLM”?
Prompts refer to the style of Creating inputs to pass into the model. 
These Information, sentences, or questions that you enter into generative AI tools have a big influence on the quality of output that you receive. Once you enter the prompt into the GenAi model or LLM, it analyzes your input and generates a response based on the patterns it has learned through its training.

Few of the Prompting Techniques that are in use in the real world:

Zero-Shot Prompting:
This is a simplest way to prompt a model is by giving it direct instructions or asking a question without providing examples. This approach relies on the model's pre-trained knowledge to generate responses. Additionally, you can refine the prompt by framing it as a question or assigning the model a specific role to guide its output.

One-Shot Prompt:
It Enhances the zero-shot prompting by giving an example to the model to imitate. For example consider the below snapshot.

Few Shot or Multi Shot Prompt:
Few- and multi-shot prompting shows the model more examples of what you want it to do. It works better than zero-shot for more complex tasks where pattern replication is wanted, or when you need the output to be structured in a specific way that is difficult to describe.

Chain -of -Thoughts:
Chain of Thought (CoT) prompting encourages the LLM to explain its reasoning. Combine it with few-shot prompting to get better results on more complex tasks that require reasoning before a response.


References.
1.https://developers.google.com/machine-learning/resources/prompt-eng
2.https://outshift.cisco.com/blog/advanced-ai-prompt-engineering-techniques
3.https://www.youtube.com/watch?v=SNxe2kwgPi4
4.https://learnprompting.org/docs/basics/few_shot
