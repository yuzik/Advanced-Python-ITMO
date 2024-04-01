import asyncio
import aiohttp
import aiofiles
import os


async def download_image(session, url, folder, image_number):
    async with session.get(url) as response:
        if response.status == 200:
            image_data = await response.read()
            filepath = os.path.join(folder, f'image_{image_number}.jpg')
            async with aiofiles.open(filepath, 'wb') as f:
                await f.write(image_data)
            print(f'{image_number} сохраннено в {filepath}')


async def main(total_images, folder='artifacts'):
    if not os.path.exists(folder):
        os.makedirs(folder)
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, "https://picsum.photos/200", folder, i)
                 for i in range(total_images)]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    total_images = int(input("Кол-во изображений: "))
    asyncio.run(main(total_images))
