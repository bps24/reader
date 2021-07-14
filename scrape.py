import requests
from bs4 import BeautifulSoup
import csv

base = "https://www.basketball-reference.com/leagues/NBA_2021_games-", ".html"
base2 = "https://www.basketball-reference.com/boxscores/pbp/"
months = ['december','january', 'february', 'march', 'april', 'may', 'june', 'july']
months_test = ['december']

for month in months_test:
    #Iterating Through Months
    page = requests.get(base[0] + month + base[1])
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find_all("div", {"id": "div_schedule"})[0].tbody
    games = [item for index, item in enumerate(table) if index %2 == 0 ]
    gamelinks = [base2 + game.findChildren()[10].get('href').split("/")[2] for game in games]

    for gamelink in gamelinks:
        page = requests.get(gamelink)
        soup = BeautifulSoup(page.content, "html.parser")
        table = soup.find_all("div", {"id":"div_pbp"})[0].table
        names = table.find_all("th")
        away, home = names[2].text, names[6].text

        with open(f"data/teams/{away}.csv","w+") as awaycsv:
            with open(f"data/teams/{home}.csv","w+") as homecsv:
                with open(f"data/games/{(gamelink.split('/')[-1]).split('.')[0]}.csv","w+") as glcsv:
                    #homewriter = csv.writer(home, delimiter=" ")
                    #awaywriter = csv.writer(away, delimiter=" ")
                    #writer.writerow("a")
                    pass

print("completed")

        
        
   

    


