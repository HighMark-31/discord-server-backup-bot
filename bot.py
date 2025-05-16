import os
import asyncio
from pathlib import Path
from datetime import datetime
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

def generate_progress_bar(current, total, length=20):
    progress = int(length * current / total)
    bar = '█' * progress + '-' * (length - progress)
    percent = int(100 * current / total)
    return f"[{bar}] {current}/{total} channels ({percent}%)"

@bot.command()
@commands.has_permissions(administrator=True)
async def backup(ctx):
    guild = ctx.guild
    timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    backup_dir = Path(f'backup_{guild.name}_{timestamp}')
    backup_dir.mkdir(exist_ok=True)

    progress_msg = await ctx.send(f"📦 Starting backup of **{guild.name}**...")

    info_path = backup_dir / "server_info.txt"
    with open(info_path, 'w', encoding='utf-8') as f:
        f.write(f"Server Name: {guild.name}\n")
        f.write(f"Server ID: {guild.id}\n")
        f.write(f"Owner: {guild.owner}\n")
        f.write(f"Member Count: {guild.member_count}\n")
        f.write(f"Created At: {guild.created_at.isoformat()}\n")
    await progress_msg.edit(content="📁 Backup: server information saved...")

    roles_path = backup_dir / "roles.txt"
    with open(roles_path, 'w', encoding='utf-8') as f:
        for role in guild.roles:
            f.write(f"{role.name} (ID: {role.id})\n")
    await progress_msg.edit(content="📁 Backup: roles saved...")

    emoji_dir = backup_dir / "emoji"
    emoji_dir.mkdir(exist_ok=True)
    for emoji in guild.emojis:
        try:
            emoji_bytes = await emoji.read()
            ext = emoji.url.split('.')[-1]
            with open(emoji_dir / f"{emoji.name}.{ext}", 'wb') as f:
                f.write(emoji_bytes)
        except Exception as e:
            print(f"Error saving emoji {emoji.name}: {e}")
    await progress_msg.edit(content="📁 Backup: emojis saved...")

    members_path = backup_dir / "member_list.txt"
    with open(members_path, 'w', encoding='utf-8') as f:
        for member in guild.members:
            roles = ', '.join(role.name for role in member.roles if role != guild.default_role)
            f.write(
                f"Username: {member} | ID: {member.id} | Bot: {member.bot}\n"
                f"Roles: {roles or 'None'}\n"
                f"Created at: {member.created_at.isoformat()} | Joined at: {member.joined_at.isoformat() if member.joined_at else 'N/A'}\n"
                f"---\n"
            )
    await progress_msg.edit(content="👥 Backup: member list saved...")

    text_channels = guild.text_channels
    total_channels = len(text_channels)
    completed_channels = 0

    media_dir = backup_dir / "media"
    logs_dir = backup_dir / "logs"
    media_dir.mkdir(exist_ok=True)
    logs_dir.mkdir(exist_ok=True)

    async def progress_updater():
        while completed_channels < total_channels:
            bar = generate_progress_bar(completed_channels, total_channels)
            await progress_msg.edit(content=f"📨 Backing up messages: {bar}")
            await asyncio.sleep(2)

    updater_task = asyncio.create_task(progress_updater())

    for channel in text_channels:
        log_path = logs_dir / f"{channel.name}.txt"
        channel_media_dir = media_dir / channel.name
        channel_media_dir.mkdir(exist_ok=True)

        try:
            with open(log_path, 'w', encoding='utf-8') as f:
                async for msg in channel.history(limit=None, oldest_first=True):
                    timestamp = msg.created_at.isoformat()
                    author = msg.author
                    content = msg.clean_content
                    f.write(f"[{timestamp}] {author}: {content}\n")
                    for att in msg.attachments:
                        try:
                            await att.save(channel_media_dir / att.filename)
                        except Exception as e:
                            f.write(f"[ATTACHMENT ERROR] {att.filename} - {e}\n")
        except Exception as e:
            print(f"Error saving messages in {channel.name}: {e}")

        completed_channels += 1

    updater_task.cancel()

    from discord import Embed

    final_bar = generate_progress_bar(completed_channels, total_channels)
    embed = Embed(
        title="✅ Backup completed successfully!",
        description="The server backup was performed correctly.",
        color=discord.Color.green()
    )
    embed.add_field(name="📊 Progress", value=final_bar, inline=False)
    embed.add_field(
        name="💬 Feedback",
        value="If this bot was helpful, please leave a **[review on Trustpilot](https://www.trustpilot.com/review/highmark.it)** "
              "and give a ⭐ to the [GitHub repo](https://github.com/highmark-31/backup-server-discord-bot)!",
        inline=False
    )
    embed.set_footer(text="Made with ❤️ by Highmark.it", icon_url="https://highmark.it/favicon.ico")

    await progress_msg.edit(content=None, embed=embed)

# --- replace "TOKEN" with your bot token ---
bot.run('TOKEN')
