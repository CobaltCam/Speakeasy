from discord.ext import commands
from dotenv import load_dotenv
import name_functions
from os import getenv

# NAME GENERATOR!!!
bot = commands.Bot(command_prefix='$')
function = name_functions
load_dotenv()


# TODO clean up code and document in comments

@bot.command()
async def name(ctx, race: str, gender: str):
    await ctx.reply(function.fantasy_race_name(race, gender))


@bot.command()
async def human_name(ctx, ethnicity: str, gender: str):
    await ctx.reply(function.human_ethnicity(ethnicity, gender))


@bot.command()
async def name_options(ctx):
    await ctx.reply('*the following fantasy races are supported:* dragonborn, dwarf, elf, gnome, half-orc, halfling, '
                    'and tiefling\n*For gender choose:* female, male, or neither\n*The following ethnicities are '
                    'supported:* arabic, celtic, chinese, english, egyptian, french, german greek, indian, japanese, '
                    'mesoamerican, niger-congo, norse, polynesian, roman, slavic, and spanish.')


bot.run(getenv('TOKEN'))
