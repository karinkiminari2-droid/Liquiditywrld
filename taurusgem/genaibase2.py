#genaibase2
from google import genai
from google.genai import types

client = genai.Client()

prompt = input()
print("Loading your prompt")

response = client.models.generate_content(
	model='gemini-3-flash-preview',
	contents=prompt
)
print(response.text)

