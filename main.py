from random import randint
from time import sleep

import requests
from bs4 import BeautifulSoup
import numpy as np

from database import insertData, openConnection


pages = np.arange(1, 3468, 40)
for page in pages:
    url = (
        "https://www.kijiji.ca/b-apartments-condos/city-of-toronto/"
        + str(page)
        + "/c37l1700273?ad=offering"
    )
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    posts = soup.find_all("div", class_="clearfix")
    sleep(randint(2, 8))

    for value in posts:
        connection = openConnection()
        ads = []
        # Exception for getting images, because some of them are null
        try:
            picture = value.find("picture").find("img").get("data-src")
        except AttributeError:
            picture = ""

        title = getattr(value.find("div", class_="title"), "text", "").strip()
        location = value.find("span", class_="").text.strip()
        date = (
            getattr(value.find("span", class_="date-posted"), "text", "")
            .replace("<", "")
            .strip())
        description = (
            getattr(value.find("div", class_="description"), "text", "")
            .strip()
            .replace("\n", "")
        )
        beds = (
            getattr(value.find("span", class_="bedrooms"), "text", "")
            .replace("Beds:", "")
            .strip()
        )
        price = (
            getattr(value.find("div", class_="price"), "text", "")
            .replace("$", "")
            .strip()
        )
        сurrency = getattr(
            value.find("div", class_="price"), "text", "text"
        ).strip()[0]

        ads.append(title)
        ads.append(location)
        ads.append(date)
        ads.append(description)
        ads.append(beds)
        ads.append(picture)
        ads.append(price)
        ads.append(сurrency)

        insertData(connection, ads, "public.posts")
        print(ads)
