from google import genai
from google.genai import types

client = genai.Client()

prompt = "Hello World"

response = client.models.generate_content(
	model='gemini-3-flash-preview',
	contents=prompt
)
print(response.text)
client.close()
