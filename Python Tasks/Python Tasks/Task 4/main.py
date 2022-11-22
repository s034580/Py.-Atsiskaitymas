# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 


class Movie:
    def __init__(self, title, director, budget):
        self.title = title
        self.director = director
        self.budget = budget

    def __str__(self):
        return f'{self}'
      
      Titanikas = Movie('Titanikas', 'James Cameron', 20000000)
      Rambo = Movie('Rambo', 'Stalone', 9999999999)
