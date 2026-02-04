#genaibase2
from google import genai
from google.genai import types

client = genai.Client()

prompt = "given savings and spending goals can you predict income for the next few months"

response = client.models.generate_content(
	model='gemini-3-flash-preview',
	contents=prompt
)
print(response.text)

