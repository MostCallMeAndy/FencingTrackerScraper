import requests, csv
from bs4 import BeautifulSoup

path = "C:\\Users\\andyn\\Documents\\FencingTrackerScraper\\Fencers.csv"

f = open(path[:-4] + '_Formatted.csv', 'w+')
fencers_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
fencers_writer.writerow(['LastName', 'FirstName', 'USAFNum', 'Club', 'Rating', 'RatingYear', 'Strength'])
f.close() 

with open(path) as csv_file:
    fencers = csv.reader(csv_file)

    for count, row in enumerate(fencers):
        if count % 4 == 0:
            name = row[0].split()
            lastName = name[0]
            lastName = lastName[:-1]
            firstName = name[1]
        if count % 4 == 1:
            rating = row[0]
            rating = rating[:-9]
            if rating == 'U':
                ratingYear = "2023"
            else:
                ratingYear = "20" + rating[-2:]
            rating = rating[0]
        if count % 4 == 2:
            club = row[0].strip()
            usafNum = row[1]
            usafNum = usafNum[1:]

            URL = "https://fencingtracker.com/p/" + usafNum + "/" + firstName+ '-' + lastName + "/strength"

            page = requests.get(URL)

            soup = BeautifulSoup(page.content, "html.parser")

            #results = soup.find_all(class_="table-group-divider")
            rows = soup.find_all('tr')
            strength = 0
            for row in rows:
                try:
                    if (row.select_one('td:nth-child(1)').get_text() == 'Foil') & (row.select_one('td:nth-child(2)').get_text() == 'DE'):
                        strength = row.select_one('td:nth-child(3)').get_text()
                        print('\n' + strength + '\n')
                except:
                    print()
            
            with open(path[:-4] + '_Formatted.csv', mode="a") as csv_writer:
                fencers_writer = csv.writer(csv_writer, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                fencers_writer.writerow([lastName, firstName, usafNum, club, rating, ratingYear, strength])