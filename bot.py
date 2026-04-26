import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# Bot ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Ping command
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong 🏓 {round(bot.latency * 1000)}ms")

# Hello command
@bot.command()
async def hi(ctx):
    await ctx.send(f"Hello {ctx.author.mention} 😎")

# Kick command
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason"):
    await member.kick(reason=reason)
    await ctx.send(f"{member} ko kick kar diya ❌")

# Ban command
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason"):
    await member.ban(reason=reason)
    await ctx.send(f"{member} ko ban kar diya 🔨")

# Auto welcome
@bot.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(f"Welcome {member.mention} 🎉")

# Run bot (TOKEN from Railway)
bot.run(os.getenv("TOKEN"))
