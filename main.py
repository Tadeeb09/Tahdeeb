import discord
from jishaku.codeblocks import codeblock_converter
import os
from discord.ext import commands
import jishaku
import keep_alive
from discord.ext import commands
import re
import asyncio
import discord
import datetime as timedelta
from datetime import datetime, timedelta
import datetime as dt

token = "MTIwNjE0NDE5NDk0MzY0NzgxNA.Gfj1eU.lbGPuv-3u75qacMVAG1jE0MNmpaw00p61wkwBc"
bot_permissions = [1086567184920227900] 

nt = "HR LUND PE"
aizer = 1086567184920227900
HRLODEPE = 1103347384358031431
os = [aizer,HRLODEPE]



papa = ("https://cdn.discordapp.com/attachments/1146400516033753210/1147842253776236644/Screenshot_20230903-160457.jpg\n")





lund = ("https://media.discordapp.net/attachments/1138154269858611260/1143860405987459173/IMG_20230729_173901.jpg \n https://media.discordapp.net/attachments/1138154269858611260/1143860406343979210/IMG_20230729_173914.jpg \n https://media.discordapp.net/attachments/1138154269858611260/1143860406792749086/IMG_20230729_173852.jpg")
allah = ("https://cdn.discordapp.com/attachments/1142864833075752972/1144664869619118243/1653783598_30-titis-org-p-islam-porn-pics-porno-vkontakte-41.jpg \n https://cdn.discordapp.com/attachments/1142864833075752972/1144664941966667836/unsorted-praying-to-allah-fNihOg.jpg")

command_descriptions = {
  "HR LODE PE": "NT BAP HAI BRO /NTOP"
  }




axzer = "<a:ACS_blackdot:1143914715496587285>"





client = commands.AutoShardedBot(command_prefix="-",intents=discord.Intents.all(),owner_ids=os)
headers = {"Authorization": f"{token}"}

allowed_to_ban = [aizer,1133718023585398804,HRLODEPE]




client.remove_command("help")
  



@client.event
async def on_ready():
  print(client.user)
  print(client.user.id)
  await client.load_extension('jishaku')
  custom_status = discord.Game(name="/HRLODE PE ")
  await client.change_presence(status=discord.Status.dnd, activity=custom_status)



@client.event
async def on_command_error(ctx, error):
    error = getattr(error, 'original', error)
    await ctx.send(embed=discord.Embed(color=0x0052F9, title = "Error!" ,timestamp=ctx.message.created_at, description=f'```{error}```'))










@client.command()
async def help(ctx):
    prefix = "-"  # Replace this with your bot's command prefix
    embed = discord.Embed(title="HR LODE PE", description="List of available commands", color=0x2B2D31)
    
    for command_name, command_description in command_descriptions.items():
        embed.add_field(name=f"{axzer} {command_name}", value=command_description, inline=False)
    
    await ctx.send(embed=embed)


# Command to get member count
@client.command(aliases=['mc'])
async def membercount(ctx):
    mems = ctx.guild.member_count
    embed = discord.Embed(
        color=0x2B2D31,
        title=f"{ctx.guild.name}",
        description=mems
    )
    if ctx.author.id == 1086567184920227900:
        pass
    else:
        await ctx.send(embed=embed)

# KICK M
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="**No reason provided**"):
    if ctx.author.id in bot_permissions:
        await member.kick(reason=reason)
        await ctx.send(f"✅ **{member.name} Has Been Kicked For Reason: `{reason}`")
    else:
        await ctx.send("**You don't have permission to use this command.**")

# BAN M
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="/hackersop"):
    if ctx.author.id in bot_permissions:
        await member.ban(reason=reason)
        await ctx.send(f"✅ **{member.name} Has Been Banned For Reason: `{reason}`**")
    else:
        await ctx.send("**You don't have permission to use this command.**")

# GIVE ROLE
@client.command()
@commands.has_permissions(manage_roles=True)
async def giverole(ctx, member: discord.Member, role: discord.Role):
    if ctx.author.id in bot_permissions:
        await member.add_roles(role)
        await ctx.send(f"✅**{member.name} has been given the `{role.name}` role**")
    else:
        await ctx.send("You don't have permission to use this command.")

# REMOVE ROLE
@client.command()
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, member: discord.Member, role: discord.Role):
    if ctx.author.id in bot_permissions:
        if role in member.roles:
            await member.remove_roles(role)
            await ctx.send(f"✅**`{role.name}` role has been removed from {member.name}**")
        else:
            await ctx.send(f"{member.name} doesn't have the {role.name} role.")
    else:
        await ctx.send("**You don't have permission to use this command.**")

# MUTE OLD MUTE SYSTEM HAI BRO  
time_regex = re.compile(r"(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}

def convert(argument):
    args = argument.lower()
    matches = re.findall(time_regex, args)
    time = 0
    for key, value in matches:
        try:
            time += time_dict[value] * float(key)
        except KeyError:
            raise commands.BadArgument(
                f"{value} is an invalid time key! h|m|s|d are valid arguments")
        except ValueError:
            raise commands.BadArgument(f"{key} is not a number!")
    return round(time)

@client.command(name="vcmute", description="Timeouts someone for a specific time.")
@commands.cooldown(1, 20, commands.BucketType.member)
@commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
@commands.guild_only()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, duration):
    ok = duration[:-1]
    tame = convert(duration)
    till = duration[-1]

    if tame == -1:
        hacker3 = discord.Embed(
            color=0x2f3136,
            description=":error: | You didn't provide a time with correct unit.\nExamples:\n{ctx.prefix}mute {ctx.author} 10m\n{ctx.prefix}mute {ctx.author} 5hr",
            timestamp=ctx.message.created_at)
        await ctx.reply(embed=hacker3, mention_author=False)
    elif tame == -2:
        aizer4 = discord.Embed(
            color=0x2f3136,
            description=":error: | Time must be an integer!",
            timestamp=ctx.message.created_at)
        await ctx.reply(embed=aizer4, mention_author=False)
    else:
        t = None
        if till.lower() == "d":
            t = dt.timedelta(seconds=tame * 86400)
        elif till.lower() == "h":
            t = dt.timedelta(seconds=tame * 3600)
        elif till.lower() == "m":
            t = dt.timedelta(seconds=tame * 60)
        elif till.lower() == "s":
            t = dt.timedelta(seconds=tame)
        
        if t is None:
            await ctx.send("Invalid time unit.")
            return
        
        await member.edit(mute=True, reason=f"Muted for {duration} by {ctx.author}")
        await ctx.send(f"{member.mention} has been muted for {duration}.")
        
        await asyncio.sleep(t.total_seconds())
        
        await member.edit(mute=False, reason="Mute duration expired")
        await ctx.send(f"{member.mention} has been unmuted after {duration}.")



# Command to unmute a member
@client.command(name="vcunmute", description="**Unmutes a member in a voice channel.**")
@commands.guild_only()
@commands.has_permissions(manage_roles=True)
async def unmutevc(ctx, member: discord.Member):
    voice_state = member.voice
    if voice_state is not None and voice_state.channel:
        await member.edit(mute=False)
        await ctx.send(f"**{member.mention} has been unmuted in the voice channel.**")
    else:
        await ctx.send(f"**{member.mention} is not in a voice channel.**")

#===================================#

time_regex = re.compile(r"(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}


def convert(argument):
    args = argument.lower()
    matches = re.findall(time_regex, args)
    time = 0
    for key, value in matches:
        try:
            time += time_dict[value] * float(key)
        except KeyError:
            raise commands.BadArgument(
                f"{value} is an invalid time key! h|m|s|d are valid arguments")
        except ValueError:
            raise commands.BadArgument(f"{key} is not a number!")
    return round(time)

    @client.command(name="mute",
                             description="Timeouts someone for specific time.",
                             usage="mute <member> <time>",
                             aliases=["timeout", "stfu"])
    @commands.cooldown(1, 20, commands.BucketType.member)
    @commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
    @commands.guild_only()  @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, duration):
        ok = duration[:-1]
        tame = self.convert(duration)
        till = duration[-1]
        if tame == -1:
            hacker3 = discord.Embed(
                color=0x2f3136,
                description=
                f":error: | You didnt didnt gave time with correct unit\nExamples:\n{ctx.prefix}mute{ctx.author} 10m\n{ctx.prefix}mute {ctx.author} 5hr",
                timestamp=ctx.message.created_at)
            await ctx.reply(embed=hacker3, mention_author=False)
        elif tame == -2:
            hacker4 = discord.Embed(
                color=0x2f3136,
                description=
                f":error: | Time must be an integer!",
                timestamp=ctx.message.created_at)
            await ctx.reply(embed=hacker4, mention_author=False)
        else:
            if till.lower() == "d":
                t = datetime.timedelta(seconds=tame)
                hacker = discord.Embed(
                    color=0x2f3136,
                    description=
                    ":GreenTick: | Successfully Muted {0.mention} For {1} Day(s)"
                    .format(member, ok),
                    timestamp=ctx.message.created_at)
            elif till.lower() == "m":
                t = datetime.timedelta(seconds=tame)
                hacker = discord.Embed(
                    color=0x2f3136,
                    description=
                    ":GreenTick: | Successfully Muted {0.mention} For {1} Minute(s)"
                    .format(member, ok),
                    timestamp=ctx.message.created_at)
            elif till.lower() == "s":
                t = datetime.timedelta(seconds=tame)
                hacker = discord.Embed(
                    color=0x2f3136,
                    description=
                    ":GreenTick: | Successfully Muted {0.mention} For {1} Second(s)"
                    .format(member, ok),
                    timestamp=ctx.message.created_at)
            elif till.lower() == "h":
                t = datetime.timedelta(seconds=tame)
                hacker = discord.Embed(
                    color=0x2f3136,
                    description=
                    ":GreenTick: | Successfully Muted {0.mention} For {1} Hour(s)"
                    .format(member, ok),
                    timestamp=ctx.message.created_at)
        try:
            if member.guild_permissions.administrator:
                hacker1 = discord.Embed(
                    color=0x2f3136,
                    description=
                    ":error: | I can\'t mute administrators",
                    timestamp=ctx.message.created_at)
                await ctx.reply(embed=hacker1)
            else:
                await member.timeout(discord.utils.utcnow() + t,
                                     reason="Command Used By: {0}".format(
                                         ctx.author))
                await ctx.send(embed=hacker)
        except:
            print("an error occured")
# Dictionary to store user warnings
user_warnings = {}

# Command to warn a member
@client.command()
@commands.has_permissions(manage_roles=True)
async def warn(ctx, member: discord.Member, *, reason="No reason provided"):
    if member.id not in user_warnings:
        user_warnings[member.id] = 1
    else:
        user_warnings[member.id] += 1

    await ctx.send(f"**{member.name} Has Been Warned For: {reason}.\n Total Warnings: {user_warnings.get(member.id, 0)}**")

    # Check if the user has 5+ warnings and apply mute
    if user_warnings.get(member.id, 0) >= 5:
        overwrite = discord.PermissionOverwrite(send_messages=False)

        for channel in ctx.guild.text_channels:
            await channel.set_permissions(member, overwrite=overwrite)

        await ctx.send(f" ✅ `{member.name} ` has been server muted due to 5+ warnings.")

#==============================#

# ... Aizer xd 

#===============================#

# Command to change a user's nickname
@client.command()
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx, member: discord.Member, *, new_nick=None):
    if new_nick is None:
        await ctx.send("Please provide a new nickname.")
        return

    try:
        await member.edit(nick=new_nick)
        await ctx.send(f"**{member.mention}'s Nickname Has Been Changed to `{new_nick}`.**")
    except discord.Forbidden:
        await ctx.send("I don't have permission to change that user's nickname.")

#===============================#


# Command to lock a channel
@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f"✅ **This channel has been locked.**")

# Command to unlock a channel
@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send("✅ **This channel has been unlocked.**")

# Command to hide a channel
@client.command()
@commands.has_permissions(manage_channels=True)
async def hide(ctx):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = False
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send(f"✅ **This channel has been hidden.**")

# Command To unhide channel
@client.command()
@commands.has_permissions(manage_channels=True)
async def unhide(ctx):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.view_channel = True
    await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send("✅ **This channel has been unhidden.**")


#===============================#

#===============================#



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Check if the message contains "vanity" or "Vanity" and reply with the link
    if "vanity" in message.content.lower():
        await message.channel.send("https://discord.gg/hackersop")

    # Aizer Papa
    await client.process_commands(message)


#======================================#
@client.command()
async def join(ctx, channel_id: int):
    voice_channel = client.get_channel(channel_id)
    
    if voice_channel and isinstance(voice_channel, discord.VoiceChannel):
        voice_client = await voice_channel.connect()
        await ctx.send(f"**Joined voice channel: `{voice_channel.name}`**")

        while voice_client.is_connected():
            await asyncio.sleep(1)
    else:
        await ctx.send("**Invalid voice channel ID**")

# Add a command to give the "Randi" role to a mentioned user
@client.command()
@commands.has_permissions(administrator=True)
async def randi(ctx, member: discord.Member):
    randi_role_id = 1119689123188457562  # Replace with the actual "Randi" role ID
    randi_role = ctx.guild.get_role(randi_role_id)
    
    if randi_role:
        if member.id != 1086567184920227900:  # Replace with the actual bot's ID
            await member.add_roles(randi_role)
            await ctx.send(f"**✅ Successfully Added `{randi_role.name}` To {member.mention} **")
        else:
            await ctx.send(f"{ctx.author.mention} ** Aukat Se Bahar**")
    else:
      await ctx.send(f"{ctx.author.mention}** Majdoori krke Perms Le Phle **")


# =====================================#
# Command to give staff role to a mentioned user
@client.command()
@commands.has_permissions(manage_roles=True)
async def staff(ctx, member: discord.Member):
    staff_role_id = 1119689115579973872  # Replace with the actual staff role ID
    
    staff_role = ctx.guild.get_role(staff_role_id)
    
    if staff_role:
        await member.add_roles(staff_role)
        await ctx.send(f"✅ ** Successfully Given `{staff_role.name}` Role To {member.mention} **")
    else:
        await ctx.send("** Lode Staff Role Id Sahi Dall **")

# =====================================#

@client.command()
@commands.has_permissions(administrator=True)
async def srandi(ctx):
#@commands.has_permissions(administrator=True)
    role_id = 1119689123188457562
    role = ctx.guild.get_role(role_id)

    if role:
      for _ in range (5):
        await ctx.send(f"{role.mention} ** Hi Majdooro Jldi Majdoori kro **")
    else:
      await ctx.send(f"{ctx.author.mention}** Majdoori krke Perms Le Phle **")

@client.command()
async def scj(ctx):
    for _ in range (1):
        await ctx.send(f" <@&1119689123188457562> {lund} CJ LODE PE !! \n CJ HR KE LODE PE !! CJ NEW GEN CLAN HR SE PANGA LEGA \n CJ AIZER KE LODE PE \n CJ SAURAV KE LODE PE \n CJ HR KE LODE PE \n CJ VALO FAME LENA BAND KRO \n P4P AA JAO HAI DUM ?\n CJ LODE PE !! \n CJ HR KE LODE PE !! CJ NEW GEN CLAN HR SE PANGA LEGA \n CJ AIZER KE LODE PE \n CJ SAURAV KE LODE PE \n CJ HR KE LODE PE \n CJ VALO FAME LENA BAND KRO \n P4P AA JAO HAI DUM ? \n CJ LODE PE !! \n CJ HR KE LODE PE !! CJ NEW GEN CLAN HR SE PANGA LEGA \n CJ AIZER KE LODE PE \n CJ SAURAV KE LODE PE \n CJ HR KE LODE PE \n CJ VALO FAME LENA BAND KRO \n P4P AA JAO HAI DUM ?\ ")
    #else:
    #  await ctx.send(f"{ctx.author.mention}** Majdoori krke Perms Le Phle **")
#@client.command()
#async def anuj(ctx):
#    for _ in range (100):
#        await ctx.send(f" {papa} <@1108673791984410654>**Anuj Randi Ab bool Aizer Tera papa** ")

        
@client.command()
async def a(ctx):
    aizer = [1086567184920227900]  # Replace with the allowed user IDs
    
    if ctx.author.id in aizer:
        for _ in range(250):
          await ctx.send(f" <@&1143232919066906705> {allah} MULLE LODE PE \n ALLAH BNANE VALE KI MAKI CHOOT ME AIZER KA LUND \n CONDOM PACKETS 👇👇👇\n 🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋 \n CONDOMS PACKETS 👆👆👆👆👆\n MULLE LODE PE \n ALLAH BNANE VALE KI MAKI CHOOT ME AIZER KA LUND \n CONDOM PACKETS 👇👇👇\n 🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋 \n CONDOMS PACKETS 👆👆👆👆👆\n MULLE LODE PE \n ALLAH BNANE VALE KI MAKI CHOOT ME AIZER KA LUND \n CONDOM PACKETS 👇👇👇\n 🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋🕋 \n CONDOMS PACKETS 👆👆👆👆👆")

#===========================#
@client.command()
#async def l(ctx):
   # aizer = [1086567184920227900, 1103347384358031431]  # Replace with the allowed user IDs
    
  #  if ctx.author.id in aizer:
       # for _ in range(250):
         # await ctx.send(" <a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060>@client.command()
async def l(ctx):
    global send_l_messages
    aizer = [1086567184920227900, 1103347384358031431]  # Replace with the allowed user IDs
    
    if ctx.author.id in aizer:
        if not send_l_messages:
            return  # Don't send messages if sending is disabled
        
        for _ in range(250):
            await ctx.send(" <a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060> <a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060><a:zzZ_lmao_blast:1133676936787415060>")
    else:
      await ctx.send(f"{ctx.author.mention}** Lode Aizer Papa Se Perms Ki bheek Mang **")


# Command to start sending messages
send_l_messages = True

@client.command()
@commands.has_permissions(administrator=True)
async def s(ctx):
    global send_l_messages
    send_l_messages = True
    await ctx.send("✅ **Bot started sending 'l' messages.**")

# Command to stop sending messages
@client.command()
@commands.has_permissions(administrator=True)
async def stop(ctx):
    global send_l_messages
    send_l_messages = False
    await ctx.send("✅ **Bot stopped sending 'l' messages.**")

@client.command()
async def restart(ctx):
    if ctx.author.id == 1131561143597547551:  # Aizer's ID
        await ctx.send("Restarting...")
        os.system("python3 main.py")  # Aizer
    else:
        await ctx.send(f"{ctx.author.mention} ** Lode Bot Perms Hai tere pas ? **")

@client.command()
@commands.has_permissions(administrator=True)
async def dm(ctx, user_id_or_mention, *, message):
    # Check if the user ID is valid
    try:
        user_id = int(user_id_or_mention.strip("<@!>"))
        user = await client.fetch_user(user_id)
    except ValueError:
        user = ctx.message.mentions[0] if ctx.message.mentions else None

    if user is not None:
        if user.id == 1086567184920227900:
            await ctx.send("❌ You cannot DM your father.")
        else:
            try:
                await user.send(message)
                await ctx.send(f"✅ Message sent to {user.mention}")
            except discord.Forbidden:
                await ctx.send("❌ Unable to send a message to this user.")
    else:
        await ctx.send("❌ User not found. Make sure you provide a valid user ID or mention.")


# Command to purge messages
@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    if amount <= 0:
        await ctx.send("Please provide a valid amount of messages to purge.")
        return

    if amount > 1000:  # Limit to avoid excessive purging
        await ctx.send("You can't purge more than 1000 messages at a time.")
        return

    await ctx.channel.purge(limit=amount + 1)  # +1 to include the command itself
    await ctx.send(f"Purged {amount} messages.", delete_after=10)  # Automatically delete the confirmation message
@client.command()
@commands.has_permissions(administrator=True)
async def rstaff(ctx, member: discord.Member):
    staff_role_id = 1119689115579973872  # Replace with the actual staff role ID
    
    staff_role = ctx.guild.get_role(staff_role_id)
    
    if staff_role:
        if staff_role in member.roles:
            await member.remove_roles(staff_role)
            await ctx.send(f"✅ **Successfully Removed `{staff_role.name}` Role From {member.mention}**")
        else:
            await ctx.send(f"{member.mention} doesn't have the `{staff_role.name}` role.")
    else:
        await ctx.send("**Invalid Staff Role ID. Please configure it properly.**")

# Command to get client ping
@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000)  # Convert to milliseconds
    await ctx.send(f"Pong! Latency: {latency}ms")


#    await client.load_extension("jishaku")

# Run the client
#os.system('clear')
keep_alive.keep_alive()
client.run(token)
  