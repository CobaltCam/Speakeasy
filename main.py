from os import getenv

from discord.ext import commands
from dotenv import load_dotenv

import name_functions

import dice

# NAME GENERATOR!!!
bot = commands.Bot(command_prefix='$')
function = name_functions
load_dotenv()


# TODO clean up code and document in comments

@bot.command()
async def name(ctx, race: str, gender: str):
    race = race.lower()
    gender = gender.lower()
    await ctx.reply(function.fantasy_race_name(race, gender))


@bot.command()
async def human_name(ctx, ethnicity: str, gender: str):
    ethnicity = ethnicity.lower()
    gender = gender.lower()
    await ctx.reply(function.human_ethnicity(ethnicity, gender))


@bot.command()
async def name_options(ctx):
    await ctx.reply('*the following fantasy races are supported:* dragonborn, dwarf, elf, gnome, half-orc, halfling, '
                    'and tiefling\n*For gender choose:* female, male, or neither\n*The following ethnicities are '
                    'supported:* arabic, celtic, chinese, english, egyptian, french, german greek, indian, japanese, '
                    'mesoamerican, niger-congo, norse, polynesian, roman, slavic, and spanish.')


@bot.command()
async def roll(ctx,num_dice: int,  num_sides: int, modifier: int):
    dice.roll_dice(num_dice, num_sides)
    total = sum(dice.rolls) + modifier
    await ctx.reply(f"Rolled {num_dice}d{num_sides}+{modifier}: You rolled a {total} <{dice.rolls} + {modifier}>")

bot.run(getenv('TOKEN'))
