import discord
from discord import *
import re
import main

bot = discord.Bot()
time_pattern = r"^\d:\d{2}:\d{3}$"

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(description="Test") 
async def ping(ctx):
    await ctx.respond(f"Pong! {bot.latency}")

@bot.slash_command()
async def register(ctx: discord.ApplicationContext,
        name: Option(str, "What's your name?")
        ):
    await ctx.respond(name)

@bot.slash_command()
async def add_track(ctx: discord.ApplicationContext,
        track: Option(str, "Select the track", 
        # choices=main.getTracks()
        ),
        time: Option(str, "Enter your time (1:23:456)")
        ):
    track = main.translateTrack(track)
    if not main.checkTracks(track):
        await ctx.send(f"Invalid Name: {track}")
        return
    if re.match(time_pattern, time):
        main.addTime(ctx.author, track, time)
        await ctx.send(f"Done! Added `{track}` with time `{time}`.")
    else:
        await ctx.send(f"Improper time: {time}")
    
@bot.slash_command()
async def display_track(ctx: discord.ApplicationContext,
        track: Option(str, "Select the track", 
                    #   choices=main.getTracks
                    )
        ):
    m = main.translateTrack(track)
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

@bot.slash_command()
async def display_user(ctx: discord.ApplicationContext):
    player_stats = main.playerStats(ctx.author)
    if player_stats:
        formatted_stats = "\n".join(
            [f"{entry[2]} - {entry[3]}" for rank, entry in enumerate(player_stats)]
        )
        await ctx.send(f" **Tracks for {ctx.author.name}** \n{formatted_stats}")
    else:
        await ctx.send(f"No times recorded for {ctx.author.name}")

@bot.slash_command()
async def add_minimum(ctx: discord.ApplicationContext,
        track: Option(str, 
        "Select the track", 
        # choices=main.getTracks
        ),
        time: Option(str, "Enter your time (1:23:456)")
        ):
    track = main.translateTrack(track)
    if not main.checkTracks(track):
        await ctx.send(f"Invalid Name: {track}")
        return
    if re.match(time_pattern, time):
        main.addTime("Minimum", track, time)
        await ctx.send(f"Done! Added `{track}` with time `{time}`.")
    else:
        await ctx.send(f"Improper time: {time}")

@bot.slash_command()
async def clear_minimum(ctx: discord.ApplicationContext,
        track: Option(str, "Select the track", 
        # choices=main.getTracks
        ),                
        ):
    track = main.translateTrack(track)
    if not main.checkTracks(track):
        await ctx.send(f"Invalid Name: {track}")
        return
    main.removeMin(track)
    await ctx.respond(f"Successfully removed {track}")

bot.run("")