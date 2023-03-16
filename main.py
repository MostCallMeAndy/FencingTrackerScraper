import requests
from bs4 import BeautifulSoup

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