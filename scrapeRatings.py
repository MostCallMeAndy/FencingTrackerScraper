import requests, csv
from bs4 import BeautifulSoup

path = "C:\\Users\\andyn\\Documents\\FencingTrackerScraper\\Fencers_Unformatted.csv"

with open(path) as csv_file:
    fencers = csv.reader(csv_file)
    for count, row in enumerate(fencers):
        if count % 4 == 0:
            userName = row[0]
            print(userName)
        if count % 4 == 1:
            userRating = row[0]
            userRating = userRating[:-9]
            print(userRating)
        if count % 4 == 2:
            userClub = row[0].strip()
            print(userClub)
            userNum = row[1]
            print(userNum)
        

#user = input("Input fencer USAF number, first name, and last name separated by spaces\n\n")
user = "100124844 andy nichols"


userData = user.split()

USAFNum = userData[0]
firstName = userData[1]
lastName = userData[2]

URL = "https://fencingtracker.com/p/" + USAFNum + "/" + firstName.capitalize() + '-' + lastName.capitalize() + "/strength"
#print(URL + '\n')
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all(class_="table-group-divider")
for result in results:
    try:
        if (result.select_one('td:nth-child(1)').get_text() == 'Foil') & (result.select_one('td:nth-child(2)').get_text() == 'DE'):
            rating = result.select_one('td:nth-child(3)').get_text()
            print('\n' + rating + '\n')
    except:
        print('\nSomething went wrong\n')