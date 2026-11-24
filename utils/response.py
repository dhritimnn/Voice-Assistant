import os
import sys
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown


load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("KEY"),
)

question = " ".join(sys.argv[1:])

if not question:
    print("Usage: ask \"your question\"")
    sys.exit(1)

response = client.chat.completions.create(
    model="liquid/lfm-3-1.7b:free",
    messages=[
        {"role": "user", "content": question},
        {"role": "system", "content": """
    You are a terminal-based AI assistant.

    Follow these formatting rules:
    - Keep the responses short as possible
    - Dont through garbage. Keep respones efficient
    - Never use LaTeX.
    - Never use \\frac, \\sqrt, \\begin or mathematical delimiters.
    - Write fractions using (a)/(b).
    - Use Unicode symbols such as ×, ÷, π, √.
    - Write derivatives as dy/dx or f'(x).
    - Keep equations readable in a plain terminal.
    - Use simple Markdown only when necessary.
    """}
   ]
)
answer = response.choices[0].message.content
console = Console()
console.print(Markdown(answer))
