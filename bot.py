import discord
import re
import json
from discord.ext import commands
import main


intent = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intent)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def help(ctx):
    message = "add: Adds your time to a specified track! \n leaderboard: Checks the leaderboard for a given track!"
    await ctx.send(message)

@bot.command()
async def add(ctx):
        
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel  # Ensures only the message author is considered
    
    await ctx.send("What course would you like to add?")
    try:
        course_msg = await bot.wait_for("message", check=check, timeout=30.0)  # Wait for course name
    except TimeoutError:
        await ctx.send("Timed out! Please try again.")
        return

    course_name = course_msg.content
    course_name = main.translateTrack(course_name)
    if not main.checkTracks(course_name):
        await ctx.send(f"Invalid Name: {course_name}")
        return


    await ctx.send("What time? (X:XX:XXX)")
    
    time_pattern = r"^\d:\d{2}:\d{3}$"
    
    try:
        time_msg = await bot.wait_for("message", check=check, timeout=30.0)  # Wait for time input
    except TimeoutError:
        await ctx.send("Timed out! Please try again.")
        return

    course_time = time_msg.content
    
    if re.match(time_pattern, course_time):
        main.addTime(ctx.author, course_name, course_time)
        await ctx.send(f"Done! Added `{course_name}` with time `{course_time}`.")
    else:
        await ctx.send(f"Improper time: {course_time}")
        
@bot.command()
async def leaderboard(ctx, *, m: str):
    m = main.translateTrack(m)
    if main.checkTracks(m):  # Check if track name is valid
        leaderboard_data = main.leaderboard(m)
        if leaderboard_data:  # If there are results
                formatted_leaderboard = "\n".join(
                    [f"#{rank+1}: {entry[1]} - {entry[2]} - {entry[3]}" for rank, entry in enumerate(leaderboard_data)]
                )
                await ctx.send(f"🏆 **Leaderboard for {m}** 🏁\n{formatted_leaderboard}")
        else:
            await ctx.send(f"No times recorded for {m}.")

    else:
        await ctx.send(f"❌ Invalid Track Name: `{m}`")
        
@bot.command()
async def stats(ctx):
    player_stats = main.playerStats(ctx.author)
    if player_stats:
        formatted_stats = "\n".join(
            [f"{entry[2]} - {entry[3]}" for rank, entry in enumerate(player_stats)]
        )
        await ctx.send(f" **Statistics for {ctx.author.name}** \n{formatted_stats}")
    else:
        await ctx.send(f"No times recorded for {ctx.author.name}")

bot.run("")