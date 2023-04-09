import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up the OpenAI API client
openai.api_key = os.getenv("OPENAI_API_KEY")
model_engine = "text-davinci-002"

# Define the prompt for the code generation task
prompt = (
    "Generate a Python function that takes two numbers as input "
    "and returns their sum."
)

# Call the OpenAI API to generate code
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Extract the generated code from the API response
generated_code = response.choices[0].text

# Print the generated code
print(generated_code)
