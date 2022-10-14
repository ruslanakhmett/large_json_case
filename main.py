import asyncio
import aiohttp


async def fetch(sem, session, url, filename):
    async with sem, session.get(url) as response:
        with open(filename, "wb") as out:
            async for chunk in response.content.iter_chunked(4096):
                out.write(chunk)

async def fetch_all(urls_and_filenames, loop):
    sem = asyncio.Semaphore(12)
    async with aiohttp.ClientSession(loop=loop, connector=aiohttp.TCPConnector(ssl=False)) as session:
        results = await asyncio.gather(
            *[fetch(sem, session, url, filename) for url, filename in urls_and_filenames]
        )
        return results

if __name__ == '__main__':

    urls_and_filenames = [
        ('https://rdb.altlinux.org/api/export/branch_binary_packages/sisyphus', 'sisyphus.json'),
        ('https://rdb.altlinux.org/api/export/branch_binary_packages/p10', 'p10.json'),
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_all(urls_and_filenames, loop))