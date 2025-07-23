import discord
from discord.ext import commands


# Replace this with your actual Groq API key
GROQ_API_KEY = "whatever"

client = groq.Groq(api_key=GROQ_API_KEY)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def sass(ctx, *, question):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # You can also try llama3-8b-8192
            messages=[
                {"role": "system", "content": "You are a sassy assistant who replies sarcastically."},
                {"role": "user", "content": question}
            ],
            temperature=0.9,
            max_tokens=100
        )
        answer = response.choices[0].message.content.strip()
        await ctx.send(answer)
    except Exception as e:
        print(f"GROQ API error: {e}")
        await ctx.send("Sorry, something went wrong with GROQ.")

# Replace with your Discord bot token


bot.run("whatever")
