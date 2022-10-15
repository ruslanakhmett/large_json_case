import asyncio
import json

import aiohttp


async def fetch(sem, session, url, filename):
    async with sem, session.get(url) as response:
        with open(filename, "wb") as out:
            async for chunk in response.content.iter_chunked(4096):
                out.write(chunk)


async def fetch_all(urls_and_filenames, loop):
    sem = asyncio.Semaphore(10)
    async with aiohttp.ClientSession(
        loop=loop, connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        results = await asyncio.gather(
            *[
                fetch(sem, session, url, filename)
                for url, filename in urls_and_filenames
            ]
        )
        return results


def json_processor_runner():
    urls_and_filenames = [
        (
            "https://rdb.altlinux.org/api/export/branch_binary_packages/sisyphus",  # noqa E501
            "sisyphus.json",
        ),
        (
            "https://rdb.altlinux.org/api/export/branch_binary_packages/p10",
            "p10.json",
        ),
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_all(urls_and_filenames, loop))

    with open("./p10.json", "r") as file:
        for line in file:
            p10_data = json.loads(line)

    with open("./sisyphus.json", "r") as file:
        for line in file:
            sis_data = json.loads(line)

    all_in_p10 = [str(item) for item in p10_data["packages"]]
    all_in_sis = [str(item) for item in sis_data["packages"]]

    only_in_p10 = list(set(all_in_p10) - set(all_in_sis))
    only_in_sis = list(set(all_in_sis) - set(all_in_p10))

    with open("case1.json", "w", encoding="utf-8") as f:
        json.dump({"case_1": only_in_p10}, f, ensure_ascii=False, indent=4)
    print("Ok! Results saved as case1.json")

    with open("case2.json", "w", encoding="utf-8") as f:
        json.dump({"case_2": only_in_sis}, f, ensure_ascii=False, indent=4)
    print("Ok! Results saved as case2.json")


if __name__ == "__main__":
    json_processor_runner()
