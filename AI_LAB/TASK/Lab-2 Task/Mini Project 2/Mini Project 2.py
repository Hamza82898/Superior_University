class Movie:
    def __init__(self, movie):
        self.movie = movie

    def cal_avg_budget(self):
        total_budget = sum(budget for _, budget in self.movie)
        avg_budget = total_budget / len(self.movie)
        return avg_budget

    def add_movie(self):
        movies = int(input("How many Movies you're Added!?"))
        for _ in range(movies):
            name = input("Enter the Movie Name :")
            budget = int(input("Enter the Movie Budget$ :"))
            self.movie.append((name,budget))

    def high_budget_movie(self, avg_budget):
        high_budget_film = []
        for movie, budget in self.movie:
            if budget > avg_budget:
                high_budget_film.append((movie, budget, budget - avg_budget))
        return high_budget_film

    def main(self):
        self.add_movie()
        avg_budget = self.cal_avg_budget()
        print(f"\nThe Average Budget of the Movies is {avg_budget:.2f}")

        high_budget_movie = self.high_budget_movie(avg_budget)
        print(f"\nHigher Budget Movies :")
        for name, budget, diff in high_budget_movie:
            print(f"{name} : {budget} (Higher)")

        print(f"\nTotal High Budget Movies : {len(high_budget_movie)}")

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers : Age of Ultron", 365000000),
    ("Avengers : End Game", 356000000),
    ("Incredibles 2", 200000000)
]

moive_analyzer = Movie(movies)
moive_analyzer.main()