# These lines are importing the necessary modules and functions required for the script.
# ChatOpenAI is likely a class in langchain.chat_models that represents the chat model provided by OpenAI.
# LLMChain (Language Learning Model Chain) could be a class that handles the execution of chat scenarios with the model.
# ChatPromptTemplate, SystemMessagePromptTemplate, and HumanMessagePromptTemplate are classes or functions to manage the structure of prompts.
# load_dotenv is a function from the dotenv module that loads environment variables from a .env file, if you have one.

from langchain.chat_models import ChatOpenAI
from langchain import LLMChain
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from dotenv import load_dotenv


# Loads environment variables from a .env file.
load_dotenv()


def chat_model_example():
    # Here, we initialize an instance of ChatOpenAI with temperature set to 0.
    # The temperature parameter controls the randomness of the model's output, with a lower temperature resulting in more deterministic output.
    chat = ChatOpenAI(temperature=0)

    # This string sets up a system message template, which is used to provide context to the AI model.
    # The placeholders {your_name} and {information_about_you} will be replaced by the actual values provided later.
    template = """
    You are {your_name}. 
    This is an small brief of you: {information_about_you}.

    In every user question provide a helpful and kind answer.
    """

    # This line converts the string template into a SystemMessagePromptTemplate object.
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    # This pair of lines creates a human message prompt template that includes a question about the character.
    human_template = "{question_about_you}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    # This line combines the system and human prompts into a single chat prompt.
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    # This line creates an instance of LLMChain, which links together the chat model and the prompt.
    chain = LLMChain(llm=chat, prompt=chat_prompt)

    # Set up variables for the assistant
    your_name = "Charly"
    information_about_you = (
        "I love programming and teaching people how to make things, I'm 24 years old"
    )

    # Start an interactive session where the user can ask multiple questions.
    while True:
        # Get the user's question.
        question_about_you = input("Please enter your question: ")

        # If the user types 'quit', end the session.
        if question_about_you.lower() == "quit":
            break

        # Run the chat model with the user's question and print the response.
        response = chain.run(
            your_name=your_name,
            information_about_you=information_about_you,
            question_about_you=question_about_you,
        )
        print(response)
        print("\n---\n")


# This is a Python convention that means the chat_model_example() function will be run if this script is run directly. If this script is imported as a module into another script, the function will not be run.
if __name__ == "__main__":
    chat_model_example()
