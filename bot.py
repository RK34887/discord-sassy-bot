import discord
from discord.ext import commands
import requests
import os

# Load your GROQ_API_KEY from environment or set directly here
GROQ_API_KEY = os.getenv("GROQ_API_KEY") or "your-groq-api-key"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

def get_groq_reply(question):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a sassy assistant who replies sarcastically."},
            {"role": "user", "content": question}
        ],
        "temperature": 0.9,
        "max_tokens": 100
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=data
    )

    return response.json()['choices'][0]['message']['content'].strip()

@bot.command()
async def sass(ctx, *, question):
    try:
        answer = get_groq_reply(question)
        await ctx.send(answer)
    except Exception as e:
        print(f"GROQ API error: {e}")
        await ctx.send("Sorry, something went wrong with GROQ.")

# Run your bot
bot.run("your-discord-bot-token")
