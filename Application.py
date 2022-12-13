from Movies import Movie
from Movies import MovieStore

def print_menu(MovieStore):
    print("1. Create movie")
    print("2. Read movie")
    print("3. Update movie")
    print("4. Delete movie")
    print("5. Quit")

if __name__ == "__main__":
    movie_store = MovieStore()
    choice = None

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter movie title: ")
            director = input("Enter movie director: ")
            release_year = input("Enter movie release year: ")
            movie = Movie(title, director, release_year)
            movie_store.add_movie(movie)
            print("Movie added!")
            # Write the movies to the CSV file
            movie_store.write_to_csv("movies.csv")


        elif choice == "2":
            title = input("Enter movie title: ")
            movie = movie_store.get_movie(title)
            if movie:
                print(movie)
            else:
                print("Movie not found!")