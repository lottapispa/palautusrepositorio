from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )

    matcher2 = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )

    matcher3 = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )

    for player in stats.matches(matcher):
        print(player)
    print()
    for player in stats.matches(matcher2):
        print(player)
    print()
    for player in stats.matches(matcher3):
        print(player)
    print("Määrä: ")
    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))


if __name__ == "__main__":
    main()
