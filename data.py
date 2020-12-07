# Getting the data from the MET dataset

import pandas as pd
import csv

# Met_objects = pd.read_csv("https://media.githubusercontent.com/media/metmuseum/openaccess/master/MetObjects.csv")


artists = ["Max Ernst", "Salvador Dalí", "May Ray", "Giorgio de Chirico", "Pablo Picasso", "Marcel Duchamp", "Francis Picabia", "André Masson", "Joan Miró", "Joan Miró", "René Magritte", "Paul Delvaux", "Yves Tanguy", "Matta", "Frida Kahlo", "Diego Rivera", "Diego Rivera", "Dorothea Tanning", "Leonora Carrington", "Hans Bellmer", "Roland Penrose", "Stella Snead", "Jean Arp", "Luis Buñuel", "Bridget Bate Tichenor", "Toyen", "Leonor Fini", "Dora Maar", "Kay Sage"]



with open("data/MetObjects.csv", "r") as artwork_csv:
    processed_csv = csv.reader(artwork_csv)

    with open("Met_Surrealist_Titles.csv", "w") as csvout:
        writeable_csv = csv.writer(csvout)

        for row in processed_csv:

            found_artist = False
            for a in artists:
                    if a in row[18]:
                            found_artist = True

            if found_artist == True:
                array_title = row[9].split(',')
                writeable_csv.writerow(array_title)
                 #writeable_csv.writerow(array_artist)
