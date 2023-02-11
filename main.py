from icrawler.builtin import GoogleImageCrawler
from pyfiglet import Figlet
import re
from pathlib import Path
from os import  getcwd, mkdir
from shutil import rmtree


"""Программа скачивает изображение с google по ключивому слову (на латинице) """


def google_img_downloader(keyword, filters):
    crawler = GoogleImageCrawler(storage={'root_dir': './img'})
    crawler.crawl(
        keyword=keyword,
        max_num=5,
        min_size=(1000,1000),
        overwrite=True,
        filters=filters,
        file_idx_offset = "auto")



if __name__ == "__main__":

    prew_text = Figlet('slant')
    print('\33[32m' + prew_text.renderText("Downloader") + '\033[0m')

    path = getcwd() + "/img"

    if Path(path).is_dir():
        if input("Would you like to remove previos images y/n:  ") == 'y':
            rmtree(path)
            mkdir(path)
    else:
        mkdir(path)


    keyword = input("Please put here keyword:  ")

    color = input("Please put here color (color, blackandwhite, etc):  ")
    color = color if color in ['color', 'blackandwhite', 'transparent', 'red', 'orange', 'yellow', 'green', 'teal', 'blue', 'purple', 'pink', 'white', 'gray', 'black', 'brown'] else "color"

    date = input("Please put here date (pastday, pastweek or dates  yyyy mm dd):    ")
    if date in ['pastday', 'pastweek']: pass
    elif re.match(r"\d{4} \d{1,2} \d{1,2}", date): date = tuple(date.split())
    else: date = None


    filters = dict(
        type='photo',
        color=color,
        # license="commerial", #noncomercial,
        date="pastweek",
        size='large',

    )
    google_img_downloader(keyword, filters)


