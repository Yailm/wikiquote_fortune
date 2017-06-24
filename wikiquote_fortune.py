#!/usr/bin/env python3
# -*- python -*-

import os
import sys
import json
import urllib
import aiohttp
import asyncio
import lxml.html

_site = 'https://en.wikiquote.org/wiki/'
_api = 'https://en.wikiquote.org/w/api.php?action=opensearch&format=json' \
        '&formatversion=2&search={}&namespace=0&limit=10&suggest=true'


def print_help():
    print("Usage: {} SHOW".format(sys.argv[0]))
    print("     -- program to generate fortune-mod cookie from wikiquote")


def bake_cookie(elements):
    cookies = []
    pretag = ''
    baking = 0
    for e in elements:
        if e.tag == 'h2':
            baking = 1
        elif baking:
            if e.tag == 'dl' and pretag == 'p':
                cookies[-1] += "\n"+e.text_content().strip()
            elif e.tag == 'li' and pretag == 'dl':
                break
            else:
                cookies.append(e.text_content().strip())
            pretag = e.tag
    return cookies


def generate_fortune(source):

    tree = lxml.html.fromstring(source)
    show_name = tree.get_element_by_id('firstHeading').text_content()
    file_name = '{}'.format(show_name.lower())

    ele_content = tree.xpath('//div[@class="mw-parser-output"]')[0]
    elements = ele_content.xpath('ul/li|h2|dl|p')

    with open(file_name, 'w') as fo:
        fo.write("\n%\n".join(bake_cookie(elements))+"\n%")
    os.execvp('strfile', ('strfile', file_name))


async def search(session, show):
    url = _api.format(urllib.parse.quote(show))
    async with session.get(url) as resp:
        suggestions = json.loads(await resp.text())
        if len(suggestions[1]) > 1:
            for index in range(len(suggestions[1])):
                print("\033[33;1m[%d:%s]\033[0m"
                      % (index+1, suggestions[1][index]))
                print("    "+suggestions[2][index])
                if suggestions[2][index]:
                    print()

            option = input("option (1..{}, or abort): ".format(index+1))
            if option in [str(x) for x in range(1, index+2)]:
                return suggestions[3][int(option)-1]
        else:
            print('\033[31mThere\'re no results matching "{}".\033[0m'
                  .format(show))

async def main(loop, show):
    async with aiohttp.ClientSession(loop=loop) as session:
        page_url = await search(session, show)
        if not page_url:
            return
        async with session.get(page_url) as resp:
            if resp.status == 200:
                generate_fortune(await resp.text())
            else:
                print("Error: url is not available, program is now exiting.")


def cli():
    if len(sys.argv) < 2:
        print_help()
        sys.exit(0)
    show = sys.argv[1]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop, show))
    loop.close()

if __name__ == '__main__':
    cli()
