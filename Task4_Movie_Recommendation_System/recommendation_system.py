import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from rapidfuzz import process

console = Console()

movies = pd.read_csv("movies.csv")

vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(movies["genre"])

similarity = cosine_similarity(genre_matrix)


def show_banner():
    console.print(
        Panel.fit(
            "[bold cyan]🎬 AI MOVIE RECOMMENDATION SYSTEM[/bold cyan]\n"
            "[green]Developed by Shraddha Chauhan[/green]"
        )
    )


def recommend_movie():
    movie_name = input("\nEnter movie name: ")

    match = movies[
        movies["title"].str.lower() == movie_name.lower()
    ]

    if match.empty:
        suggestion = process.extractOne(
            movie_name,
            movies["title"].tolist()
        )

        console.print("\n[yellow]Movie not found![/yellow]")

        if suggestion:
            console.print(
                f"[cyan]Did you mean: {suggestion[0]} ?[/cyan]"
            )

        return

    index = match.index[0]

    scores = list(enumerate(similarity[index]))
    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    table = Table(title="🎯 Recommended Movies")

    table.add_column("No")
    table.add_column("Movie")
    table.add_column("Rating")

    for count, movie in enumerate(scores[1:6], start=1):
        idx = movie[0]

        table.add_row(
            str(count),
            movies.iloc[idx]["title"],
            str(movies.iloc[idx]["rating"])
        )

    console.print(table)


def recommend_genre():
    genre = input("\nEnter Genre: ")

    result = movies[
        movies["genre"]
        .str.lower()
        .str.contains(genre.lower())
    ]

    if result.empty:
        console.print("\n[red]No movies found![/red]")
        return

    result = result.sort_values(
        by="rating",
        ascending=False
    )

    table = Table(title=f"🎥 {genre.upper()} MOVIES")

    table.add_column("Movie")
    table.add_column("Rating")

    for _, row in result.head(5).iterrows():
        table.add_row(
            row["title"],
            str(row["rating"])
        )

    console.print(table)


def top_movies():
    top = movies.sort_values(
        by="rating",
        ascending=False
    )

    table = Table(title="🏆 TOP RATED MOVIES")

    table.add_column("Rank")
    table.add_column("Movie")
    table.add_column("Rating")

    for rank, row in enumerate(
            top.head(10).itertuples(),
            start=1):

        table.add_row(
            str(rank),
            row.title,
            str(row.rating)
        )

    console.print(table)


def available_movies():
    table = Table(title="📚 Available Movies")

    table.add_column("No")
    table.add_column("Movie")

    for i, movie in enumerate(
            movies["title"],
            start=1):

        table.add_row(
            str(i),
            movie
        )

    console.print(table)


def statistics():
    console.print(
        f"\n📊 Total Movies: {len(movies)}"
    )

    console.print(
        f"⭐ Average Rating: {movies['rating'].mean():.2f}"
    )

    console.print(
        f"🏆 Highest Rated Movie: "
        f"{movies.loc[movies['rating'].idxmax(),'title']}"
    )


def main():

    show_banner()

    while True:

        console.print("\n[bold yellow]MENU[/bold yellow]")
        console.print("1. Recommend by Movie")
        console.print("2. Recommend by Genre")
        console.print("3. Top Rated Movies")
        console.print("4. Available Movies")
        console.print("5. Statistics")
        console.print("6. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            recommend_movie()

        elif choice == "2":
            recommend_genre()

        elif choice == "3":
            top_movies()

        elif choice == "4":
            available_movies()

        elif choice == "5":
            statistics()

        elif choice == "6":

            console.print(
                "\n[green]Thank you for using the system![/green]"
            )

            break

        else:

            console.print(
                "\n[red]Invalid Choice![/red]"
            )


if __name__ == "__main__":
    main()