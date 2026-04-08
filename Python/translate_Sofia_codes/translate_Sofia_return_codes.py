#!/usr/bin/env python3

import asyncio
from googletrans import Translator

async def translate_description():
    """
    Translate a given code description from Chinese to English using Google translate with an API call
    """
    with open("description", "r") as description:
        original = [x for x in description]
        async with Translator() as translator:
            translations = await translator.translate(original)
            translation = [x.text for x in translations]
        return original, translation

def main():
    description, translation = asyncio.run(translate_description())
    with open("code", "r") as code:
        for x, y, z in zip(code, description, translation):
            x = x.rstrip('\n')
            y = y.rstrip('\n')
            #print(f"{x}: {y} - {z}")
            print(f"|{x}|{z}|")

if __name__ == "__main__":
    main()
