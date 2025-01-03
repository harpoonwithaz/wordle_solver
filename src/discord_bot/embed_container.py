# Discord bot imports
import discord

def tutorial():
    embed = discord.Embed(title="How to play",
                        description="**Guess the Wordle in 6 tries.**\n• Each guess must be a valid 5-letter word.\n• The color of the tiles will change to show how close your guess was to the word.")

    embed.add_field(name="Examples",
                    value=">>><:regional_indicator_w:1324584776778387527><:regional_indicator_w:1324584776778387527>\n🟩⬛⬛⬛⬛",
                    inline=True)
    embed.add_field(name="",
                    value="**W** is in the word and in the correct spot.\n \n>>>   L      I      G      H      T\n⬛🟨⬛⬛⬛",
                    inline=False)
    embed.add_field(name="",
                    value="**I** is in the word but in the wrong spot.\n\n>>>   R      O      G      U      E\n⬛⬛⬛⬜⬛",
                    inline=False)
    embed.add_field(name="",
                    value="**U** is not in the word in any spot.",
                    inline=False)
    
    return embed