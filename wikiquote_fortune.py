#!/usr/bin/env python3
# -*- python -*-

import sys
import json
import urllib
import aiohttp
import asyncio

site = 'https://en.wikiquote.org/wiki/'
show = sys.argv[1]


def print_help():
    print("Usage: {} SHOW" % sys.argv[0])
    print("     -- program to generate fortune-mod cookie from wikiquote")


def soups_turn(source):
    print(source)

async def suggest(session):
    _api = 'https://en.wikiquote.org/w/api.php?action=opensearch&format=json' \
            '&formatversion=2&search={}&namespace=0&limit=10&suggest=true'
    url = _api.format(urllib.parse.quote(show))
    async with session.get(url) as resp:
        suggestions = json.loads(await resp.text())
        print('\033[31mThere were no results matching "{}".\033[0m'.format(show))
        if len(suggestions[1]) > 1:
            print('But some suggesions was provided:\n')

            for index in range(len(suggestions[1])):
                print("\033[33;1m[%d:%s]\033[0m"
                      % (index+1, suggestions[1][index]))
                print("    "+suggestions[2][index])
                if suggestions[2][index]:
                    print()

            option = input("action (1..{}, q for aborted) :".format(index+1))
            if option == 'q':
                return 0
            elif option in [str(x) for x in range(1, index+2)]:
                async with session.get(suggestions[3][int(option)-1]) as resp:
                    soups_turn(await resp.text())

async def main(loop):
    async with aiohttp.ClientSession(loop=loop) as session:
        url = site + urllib.parse.quote(show.replace(' ', '_'))
        async with session.get(url) as resp:
            if resp.status == 200:
                soups_turn(await resp.text())
            else:
                await suggest(session)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print_help()
        sys.exit(0)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
