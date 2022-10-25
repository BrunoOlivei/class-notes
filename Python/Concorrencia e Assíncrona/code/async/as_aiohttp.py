import asyncio

import aiohttp
import aiofiles
import bs4


async def pegar_links():
    links = []
    async with aiofiles.open("links.txt") as arquivo:
        async for linha in arquivo:
            links.append(linha.strip())
    return links


async def pegar_html(link):
    print(f"Pegando o HTML do curso {link}")

    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resp:
            print(resp.status)
            print(resp.raise_for_status())
            html = await resp.text()
            return html


def pegar_titulo(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    return soup.title.string.split("|")[0].strip()


async def imprimir_titulos():
    links = await pegar_links()
    tasks = []

    for link in links:
        tasks.append(asyncio.create_task(pegar_html(link)))

    for task in tasks:
        html = await task
        titulo = pegar_titulo(html)
        print(f"Curso: {titulo}")


def main():
    eventloop = asyncio.get_event_loop()
    eventloop.run_until_complete(imprimir_titulos())
    eventloop.close()


if __name__ == "__main__":
    main()