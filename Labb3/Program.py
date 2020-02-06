import requests
import json
import sys
filmerna = []
spara = []
allaSöknignar = []
class huvudMeny():
    def __init__(self):
        self.meny()
    def meny(self):
        while True:
            print("\n1. Sök efter film")
            print("2. Historik")
            print("3. Senast sökta film")
            print("4. Avsluta \n")
            svar = input()
            if svar == '1':
                filmer()     
            elif svar == '2':
                historik()
            elif svar == '3':
                sparat()
            elif svar == '4':
                break
            else:
                print("\nvärdet kan inte hanteras. Försök igen \n")

class filmer():
    def __init__(self):
        self.taFilm()
    def taFilm(self):
        filmNamn = input("Skriv in en film: ")
        svar = requests.get(f'http://www.omdbapi.com/?apikey=7fda03ef&s={filmNamn}')
        data = svar.json()
        try:
            with open('file.json', 'w', encoding="utf=8") as wa:
                json.dump(data, wa, ensure_ascii=False, indent=1)
        except FileNotFoundError as fel:
            print(fel)
        räknare = 0
        i = data['Search']
        for x in i:
            räknare += 1
            print(räknare, x['Title'],x['Year'],x['Type'])
        val = int(input("Skriv in siffran som står inan filmen: "))
        
        with open ('file.json', 'r', encoding='utf-8') as f_list:               
            sasa = json.load(f_list)
            filval = sasa.get('Search')[val-1]
            imdbID = filval['imdbID']
            filmerna.append(filval['Title'])
            newData = requests.get(f'http://www.omdbapi.com/?i={imdbID}&apikey=7fda03ef')
            newfil = newData.json()
            spara.append(newfil)
            print(newfil)
            allaSöknignar.append(newfil)
        try:
            with open('filmer.json', 'w', encoding="utf=8") as aw:
                json.dump(newfil, aw, ensure_ascii=False, indent=1)
        except FileNotFoundError as fel:
            print(fel)


class sparat():
    def __init__(self):
        self.sparadFilm()
    def sparadFilm(self):
        try:
            with open('filmer.json', 'r', encoding="utf=8") as daw:
                sawd = json.load(daw)
                print(sawd)
        except FileNotFoundError as fel:
            print(fel)

class historik():
    def __init__(self):
        self.menyUnder()
    def menyUnder(self):
        räknare = -1
        for x in filmerna:
            räknare += 1
            print(räknare, x)
        valdSökning = input("välj vilken film som du vill se mer om: ")
        valtNummer = int(valdSökning)
        print(allaSöknignar[valtNummer])       
