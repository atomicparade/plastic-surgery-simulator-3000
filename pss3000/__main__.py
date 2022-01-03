"""Connect to Discord and begin bot operation."""
import logging
import os
import sys

import hikari
import tanjun
from dotenv import load_dotenv

load_dotenv()

# Set logging level
LOGLEVELS = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}

loglevel = os.getenv("LOGLEVEL")

if loglevel:
    loglevel = loglevel.strip().upper()

    if loglevel in LOGLEVELS:
        logging.basicConfig(level=LOGLEVELS[loglevel])
    else:
        logging.warning(
            (
                'Invalid LOGLEVEL value "%s" - must be one of '
                "DEBUG, INFO, WARNING, ERROR, or CRITICAL'"
            ),
            loglevel,
        )


# Get guild IDs to push commands to (for development)
guild_id_strs = (os.getenv("GUILD_ID_LIST") or "").split(";")
guild_id_strs = [guild_id_str.strip() for guild_id_str in guild_id_strs]

guild_ids = []

for guild_id_str in guild_id_strs:
    if len(guild_id_str) == 0:
        continue

    if guild_id_str.isdigit():
        guild_ids.append(hikari.Snowflake(int(guild_id_str)))
    else:
        logging.warning('GUILD_ID_LIST: Invalid guild ID "%s"', guild_id_str)

logging.info(
    "Pushing commands to guilds: %s",
    ", ".join([str(guild_id) for guild_id in guild_ids]),
)

discord_bot_token = (os.getenv("DISCORD_BOT_TOKEN") or "").strip()

if not discord_bot_token:
    logging.critical("Missing environment variable DISCORD_BOT_TOKEN")
    sys.exit(1)

bot = hikari.GatewayBot(discord_bot_token)

client = (
    tanjun.Client.from_gateway_bot(
        bot,
        declare_global_commands=guild_ids,
    )
    .load_modules("pss3000.commands.miscellaneous")
    .load_modules("pss3000.commands.meme")
)

bot.run()
