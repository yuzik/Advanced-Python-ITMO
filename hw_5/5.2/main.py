import asyncio
import aiohttp
from bs4 import BeautifulSoup
import json
import aiofiles
import os
from random import randint
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


async def fetch_page(session, url):
    logging.info(f"Начало скачивания страницы: {url}")
    await asyncio.sleep(randint(3, 6))  # Случайная задержка
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    async with session.get(url, headers=headers) as response:
        if response.status not in [200, 201]:
            logging.error(
                f"Ошибка при скачивании страницы: {url} с статусом: {response.status}")
            return None
        logging.info(f"Страница скачана: {url}")
        return await response.text()


async def parse_page(html):
    logging.info("Начало анализа страницы")
    soup = BeautifulSoup(html, 'html.parser')
    # Измените селектор на актуальный
    ads = soup.find_all('li', class_='OffersSerpItem')
    data = []
    for ad in ads:
        # Измените селектор на актуальный
        title = ad.find('span', class_='OffersSerpItem__title').text
        # Измените селектор на актуальный
        price = ad.find('span', class_='price').text
        data.append({'title': title, 'price': price})
    logging.info("Анализ страницы завершен")
    return data


async def save_data(data, filename):
    logging.info(f"Начало записи данных в файл: {filename}")
    if not os.path.exists('artifacts'):
        os.makedirs('artifacts')
    filepath = os.path.join('artifacts', filename)
    async with aiofiles.open(filepath, 'w', encoding='utf-8') as f:
        await f.write(json.dumps(data, ensure_ascii=False, indent=4))
    logging.info(f"Данные успешно записаны в файл: {filename}")


async def main(base_url, filename='ads.json'):
    async with aiohttp.ClientSession() as session:
        all_data = []  # Собираем данные со всех страниц
        page = 1
        while True:
            url = f"{base_url}?page={page}"
            logging.info(f"Обработка страницы {page}")
            html = await fetch_page(session, url)
            if html is None:
                logging.error("Не удалось получить данные со страницы.")
                break
            data = await parse_page(html)
            if not data:
                logging.info(
                    "Данные на странице отсутствуют, завершение работы.")
                break
            all_data.extend(data)
            page += 1  # Переход к следующей странице
        await save_data(all_data, filename)

if __name__ == '__main__':
    base_url = 'https://realty.ya.ru/sankt-peterburg/kupit/kvartira/vtorichniy-rynok'  # Уточните URL
    asyncio.run(main(base_url))
