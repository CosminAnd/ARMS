import requests
from bs4 import BeautifulSoup
import csv

url = 'https://explodingtopics.com/blog/video-game-stats'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

stats_element = soup.find_all('table')
# print(stats_element)
stats = []
for row in stats_element:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    stats.append(cols)
# for stat in stats:
#     print(stat)

# print(stats[0])
with open('market.csv', mode='w', newline="") as file:
    writer = csv.writer(file)

    for i in range(0, len(stats[0]), 4):
        el1 = stats[0][i]
        el2 = stats[0][i + 1]
        el3 = stats[0][i + 2]
        el4 = stats[0][i + 3]
        writer.writerow([el1, el2, el3, el4])

# print(stats[1])
with open('platform.csv', mode='w', newline="") as file:
    writer = csv.writer(file)

    for i in range(0, len(stats[1]), 2):
        el1 = stats[1][i]
        el2 = stats[1][i + 1]
        writer.writerow([el1, el2])

# print(stats[2])
with open('popular.csv', mode='w', newline="") as file:
    writer = csv.writer(file)

    for i in range(0, len(stats[2]), 5):
        el1 = stats[2][i].replace("#", "")
        el2 = stats[2][i + 1]
        el3 = stats[2][i + 2]
        el4 = stats[2][i + 3]
        el5 = stats[2][i + 4]

        writer.writerow([el1, el2, el3, el4, el5])

# print(stats[3])
with open('top_10_best-selling_Nintendo_Switch_titles.csv', mode='w', newline="") as file:
    writer = csv.writer(file)

    for i in range(0, len(stats[3]), 5):
        el1 = stats[3][i]
        el2 = stats[3][i + 1]
        el3 = stats[3][i + 2]
        el4 = stats[3][i + 3]
        el5 = stats[3][i + 4]

        writer.writerow([el1, el2, el3, el4, el5])

url = "https://en.wikipedia.org/wiki/List_of_video_game_publishers"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

stats_element = soup.find_all('table')
# print(stats_element)
stats = []
for row in stats_element:
    cols = row.find_all('tr')
    cols = [col.text.strip() for col in cols]
    stats.append(cols)
stats = stats[1]
# for stat in stats:
#     print(stat)

split = []

for stat in stats:
    temp = stat.split("\n\n")
    split.append(temp)

lg = len(split)

with open("publisher_and_region.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(split[0][0:3])
    for i in range(1, lg):
        # print(split[i][0:3])
        writer.writerow(split[i][0:3])

