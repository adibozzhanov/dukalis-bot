import os

import interactions

from dotenv import load_dotenv

load_dotenv()

tok = os.getenv('token')

bot = interactions.Client(token=tok)


@bot.command(
    name="hai",
    description="Says hello",
)
async def my_first_command(ctx: interactions.CommandContext):
    await ctx.send("HAI BICH")


bot.start()
