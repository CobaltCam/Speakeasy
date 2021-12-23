import random
import name_lists


def human_ethnicity(ethnicity: str, user_gender: str):
    """ When human is chosen presents list of human ethnicities and then generates a human name randomly """

    if ethnicity == "arabic" and user_gender == "female":
        return random.choice(name_lists.arabic_female) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "arabic" and user_gender == "male":
        return random.choice(name_lists.arabic_male) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "arabic" and user_gender == "neither":
        return random.choice(name_lists.arabic_female or name_lists.arabic_male) + ' ' + random.choice(
            name_lists.human_surnames)

    if ethnicity == "celtic" and user_gender == "female":
        return random.choice(name_lists.celtic_female) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "celtic" and user_gender == "male":
        return random.choice(name_lists.celtic_male) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "celtic" and user_gender == "neither":
        return random.choice(name_lists.celtic_female or name_lists.celtic_male) + ' ' + random.choice(
            name_lists.human_surnames)

    if ethnicity == "chinese" and user_gender == "female":
        return random.choice(name_lists.chinese_female) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "chinese" and user_gender == "male":
        return random.choice(name_lists.chinese_male) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "chinese" and user_gender == "neither":
        return random.choice(name_lists.chinese_female or name_lists.chinese_male) + ' ' + random.choice(
            name_lists.human_surnames)

    if ethnicity == "english" and user_gender == "female":
        return random.choice(name_lists.english_female) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "english" and user_gender == "male":
        return random.choice(name_lists.english_male) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "english" and user_gender == "neither":
        return random.choice(name_lists.english_female or name_lists.english_male) + ' ' + random.choice(
            name_lists.human_surnames)

    if ethnicity == "egyptian" and user_gender == "female":
        return random.choice(name_lists.egyptian_female) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "egyptian" and user_gender == "male":
        return random.choice(name_lists.egyptian_male) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "egyptian" and user_gender == "neither":
        return random.choice(name_lists.egyptian_female or name_lists.egyptian_male) + ' ' + random.choice(
            name_lists.human_surnames)

    if ethnicity == "french" and user_gender == "female":
        return random.choice(name_lists.french_female) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "french" and user_gender == "male":
        return random.choice(name_lists.french_male) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "french" and user_gender == "neither":
        return random.choice(name_lists.french_female or name_lists.french_male) + ' ' + random.choice(
            name_lists.human_surnames)

    if ethnicity == "german" and user_gender == "female":
        return random.choice(name_lists.german_female) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "german" and user_gender == "male":
        return random.choice(name_lists.german_male) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "german" and user_gender == "neither":
        return random.choice(name_lists.german_female or name_lists.german_male) + ' ' + random.choice(
            name_lists.human_surnames)

    if ethnicity == "greek" and user_gender == "female":
        return random.choice(name_lists.greek_female) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "greek" and user_gender == "male":
        return random.choice(name_lists.greek_male) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "greek" and user_gender == "neither":
        return random.choice(name_lists.greek_female or name_lists.greek_male) + ' ' + random.choice(
            name_lists.human_surnames)

    if ethnicity == "indian" and user_gender == "female":
        return random.choice(name_lists.indian_female) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "indian" and user_gender == "male":
        return random.choice(name_lists.indian_male) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "indian" and user_gender == "neither":
        return random.choice(name_lists.indian_female or name_lists.indian_male) + ' ' + random.choice(
            name_lists.human_surnames)

    if ethnicity == "japanese" and user_gender == "female":
        return random.choice(name_lists.japanese_female) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "japanese" and user_gender == "male":
        return random.choice(name_lists.japanese_male) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "japanese" and user_gender == "neither":
        return random.choice(name_lists.japanese_female or name_lists.japanese_male) + ' ' + random.choice(
            name_lists.human_surnames)

    if ethnicity == "mesoamerican" and user_gender == "female":
        return random.choice(name_lists.mesoamerican_female) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "mesoamerican" and user_gender == "male":
        return random.choice(name_lists.mesoamerican_male) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "mesoamerican" and user_gender == "neither":
        return random.choice(name_lists.mesoamerican_female or name_lists.mesoamerican_male) + ' ' + random.choice(
            name_lists.human_surnames)

    if ethnicity == "niger-congo" and user_gender == "female":
        return random.choice(name_lists.nigercongo_female) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "niger-congo" and user_gender == "male":
        return random.choice(name_lists.nigercongo_male) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "niger-congo" and user_gender == "neither":
        return random.choice(name_lists.nigercongo_female or name_lists.nigercongo_male) + ' ' + random.choice(
            name_lists.human_surnames)

    if ethnicity == "norse" and user_gender == "female":
        return random.choice(name_lists.norse_female) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "norse" and user_gender == "male":
        return random.choice(name_lists.norse_male) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "norse" and user_gender == "neither":
        return random.choice(name_lists.norse_female or name_lists.norse_male) + ' ' + random.choice(
            name_lists.human_surnames)

    if ethnicity == "polynesian" and user_gender == "female":
        return random.choice(name_lists.polynesian_female) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "polynesian" and user_gender == "male":
        return random.choice(name_lists.polynesian_male) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "polynesian" and user_gender == "neither":
        return random.choice(name_lists.polynesian_female or name_lists.polynesian_male) + ' ' + random.choice(
            name_lists.human_surnames)

    if ethnicity == "roman" and user_gender == "female":
        return random.choice(name_lists.roman_female) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "roman" and user_gender == "male":
        return random.choice(name_lists.roman_male) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "roman" and user_gender == "neither":
        return random.choice(name_lists.roman_female or name_lists.roman_male) + ' ' + random.choice(
            name_lists.human_surnames)

    if ethnicity == "slavic" and user_gender == "female":
        return random.choice(name_lists.slavic_female) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "slavic" and user_gender == "male":
        return random.choice(name_lists.slavic_male) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "slavic" and user_gender == "neither":
        return random.choice(name_lists.slavic_female or name_lists.slavic_male) + ' ' + random.choice(
            name_lists.human_surnames)

    if ethnicity == "spanish" and user_gender == "female":
        return random.choice(name_lists.spanish_female) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "spanish" and user_gender == "male":
        return random.choice(name_lists.spanish_male) + ' ' + random.choice(name_lists.human_surnames)
    elif ethnicity == "spanish" and user_gender == "neither":
        return random.choice(name_lists.spanish_female or name_lists.spanish_male) + ' ' + random.choice(
            name_lists.human_surnames)


def fantasy_race_name(user_race: str, user_gender: str) -> object:
    """ Generates a name randomly based on choice of fantasy race. accepts race and gender as strings"""

    # dragonborn
    if user_race == "dragonborn" and user_gender == "female":
        return random.choice(name_lists.dragonborn_female) + " " + random.choice(name_lists.dragonborn_clan)
    elif user_race == "dragonborn" and user_gender == "male":
        return random.choice(name_lists.dragonborn_male) + " " + random.choice(name_lists.dragonborn_clan)
    elif user_race == "dragonborn" and user_gender == "neither":
        return random.choice(name_lists.dragonborn_female or name_lists.dragonborn_male) + " " + random.choice(
            name_lists.dragonborn_clan)

    # dwarves
    if user_race == "dwarf" and user_gender == "female":
        return random.choice(name_lists.dwarven_female) + " " + random.choice(name_lists.dwarven_clan)
    elif user_race == "dwarf" and user_gender == "male":
        return random.choice(name_lists.dwarven_male) + " " + random.choice(name_lists.dwarven_clan)
    elif user_race == "dwarf" and user_gender == "neither":
        return random.choice(name_lists.dwarven_male or name_lists.dwarven_female) + " " + random.choice(
            name_lists.dwarven_clan)

    # elves
    if user_race == "elf" and user_gender == "female":
        return random.choice(name_lists.elven_female) + " " + random.choice(name_lists.elven_family)
    elif user_race == "elf" and user_gender == "male":
        return random.choice(name_lists.elven_male) + " " + random.choice(name_lists.elven_family)
    elif user_race == "elf" and user_gender == "neither":
        return random.choice(name_lists.elven_male or name_lists.elven_female) + " " + random.choice(
            name_lists.elven_family)

    # gnomes
    if user_race == "gnome" and user_gender == "female":
        return random.choice(name_lists.gnome_female) + " " + random.choice(name_lists.gnome_clan)
    elif user_race == "gnome" and user_gender == "male":
        random.choice(name_lists.gnome_male) + " " + random.choice(name_lists.gnome_clan)
    elif user_race == "gnome" and user_gender == "neither":
        return random.choice(name_lists.gnome_female or name_lists.gnome_male) + " " + random.choice(
            name_lists.gnome_clan)

    # halflings
    if user_race == "halfling" and user_gender == "female":
        return random.choice(name_lists.halfling_female) + " " + random.choice(name_lists.halfling_family)
    elif user_race == "halfling" and user_gender == "male":
        return random.choice(name_lists.halfling_male) + " " + random.choice(name_lists.halfling_family)
    elif user_race == "halfling" and user_gender == "neither":
        return random.choice(name_lists.halfling_female or name_lists.halfling_male) + " " + random.choice(
            name_lists.halfling_family)

    # half-orc
    if user_race == "half-orc" and user_gender == "female":
        return random.choice(name_lists.halforc_female)
    elif user_race == "half-orc" and user_gender == "male":
        return random.choice(name_lists.halforc_male)
    elif user_race == "half-orc" and user_gender == "neither":
        return random.choice(name_lists.halforc_male or name_lists.halforc_female)

    # tiefling
    if user_race == "tiefling" and user_gender == "female":
        return random.choice(name_lists.tiefling_female)
    elif user_race == "tiefling" and user_gender == "male":
        return random.choice(name_lists.tielfing_male)
    elif user_race == "tiefling" and user_gender == "neither":
        return random.choice(name_lists.tiefling_female or name_lists.tielfing_male)
