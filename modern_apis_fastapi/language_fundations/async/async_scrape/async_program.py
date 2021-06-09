from asyncio.events import AbstractEventLoop
import datetime
import asyncio
from typing import Optional

import bs4
import httpx
from colorama import Fore

loop: Optional[AbstractEventLoop] = None


async def get_html(episode_number: int) -> str:
    print(Fore.YELLOW + f"Getting HTML for episode {episode_number}", flush=True)
    
    url = f"https://talkpython.fm/{episode_number}"

    async with httpx.AsyncClient() as client:        
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.text


def get_title(html: str, episode_number: int) -> str:
    print(Fore.CYAN + f"Getting TITLE for episode {episode_number}", flush=True)
    soup = bs4.BeautifulSoup(html, "html.parser")
    header: bs4.element.Tag = soup.select_one("h1")
    if not header:
        return "MISSING"
    return header.get_text(strip=True)


def main():
    t0 = datetime.datetime.now()

    global loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_title_range())

    dt = datetime.datetime.now() - t0
    print(f"Done in {dt.total_seconds():.2f} sec.")


async def get_title_range() -> None:

    tasks = [(n, loop.create_task(get_html(n))) for n in range(270, 280)]

    for n, task in tasks:
        html = await task # await for task to finish and retreive
        title = get_title(html, n)
        print(Fore.WHITE + f"Title found: {title}", flush=True)


if __name__ == "__main__":
    main()
