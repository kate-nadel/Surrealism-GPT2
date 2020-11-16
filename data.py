import pandas as pd
import csv

# Met_objects = pd.read_csv("https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv")


# artists = []



with open("data/MetObjects.csv", "r") as artwork_csv:
    processed_csv = csv.reader(artwork_csv)

    with open("Met_Surrealist_Artists6.csv", "w") as csvout:
        writeable_csv = csv.writer(csvout)

        for row in processed_csv:

            if "Salvador Dalí" in row[18]:

                # print(row[9], row[18]) #this seems  to work
                array_title = row[9].split(',')
                array_artist = row[18].split(',')
                writeable_csv.writerow(array_title), writeable_csv.writerow(array_artist)
                # writeable_csv.writerow(row[9][18])    ##this writes the whole document to new CSV
                # writeable_csv.writerow(row["Title"], row["Artist Display Name"])  ##this doesn't work at all

# title row = index 9
# Artist Display Name = index 18
#or "Salvador Dalí" or "May Ray" or "Giorgio de Chirico" or "Pablo Picasso" or "Marcel Duchamp" or "Francis Picabia" or "André Masson" or "Joan Miró" or "Joan Miró" or "René Magritte" or "Paul Delvaux" or "Yves Tanguy" or "Matta" or "Frida Kahlo" or "Diego Rivera" or "Diego Rivera" or "Dorothea Tanning" or "Leonora Carrington" or "Hans Bellmer" or "Roland Penrose" or "Stella Snead" or "Jean Arp" or "Luis Buñuel" or "Bridget Bate Tichenor" or "Toyen" or "Leonor Fini" or "Dora Maar" or "Kay Sage"
