import csv

class Movie:
    def __init__(self, title, director, release_year):
        self.title = title
        self.director = director
        self.release_year = release_year

    def __str__(self):
        return f"{self.title} ({self.release_year}) - directed by {self.director}" 
        #return method for the each of the class self attributes or data