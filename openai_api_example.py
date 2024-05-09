import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the OpenAI API client
openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "gpt-3.5-turbo"

# Define the prompt for the code generation task
messages = [{
    "role": "user",
    "content": "Generate a Python function that takes two numbers as input and returns their sum."
}]

# Call the OpenAI API to generate code
response = openai.ChatCompletion.create(
    model=model_engine,
    messages=messages,
    max_tokens=150,
    temperature=0.5,
)

# Extract the generated code from the API response
generated_code = response['choices'][0]['message']['content'].strip()  #

# Print the generated code
print(generated_code)
