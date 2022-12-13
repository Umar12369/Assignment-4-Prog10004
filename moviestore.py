
import csv

class MovieStore:
    def __init__(self):
        # Initialize an empty list of movies
        self.movies = []

    def add_movie(self, movie):
        # Add the given movie to the list of movies
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