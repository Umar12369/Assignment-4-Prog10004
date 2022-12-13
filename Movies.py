import csv

class Movie:
    def __init__(self, title, director, release_year):
        self.title = title
        self.director = director
        self.release_year = release_year

    def __str__(self):
        return f"{self.title} ({self.release_year}) - directed by {self.director}" 
        #return method for the each of the class self attributes or data

class MovieStore:
    def __init__(self):
        #list of movies
        self.movies = []

    def add_movie(self, movie):
        # create movie to the list of movies
        self.movies.append(movie)

    def write_to_csv(self, filename):
        # Create a new file with the given filename
        with open(filename, "w", newline="") as csvfile:
            # Use the csv.writer() method to create a writer object
            writer = csv.writer(csvfile)
            # Write the column headers
            writer.writerow(["Title", "Director", "Release Year"])
            # Iterate over the movies in the store and write each one to the file
            for movie in self.movies:
                writer.writerow([movie.title, movie.director, movie.release_year])