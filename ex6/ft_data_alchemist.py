import random

PLAYERS: list[str] = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory",
                      "john", "kevin", "Liam"]

if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {PLAYERS}")

    capitalized_players: list[str] = [player.capitalize()
                                      for player in PLAYERS]
    capitalized_only: list[str] = [player for player in PLAYERS
                                   if player[0].isupper()]

    scores: dict[str, int] = {player: random.randint(0, 1000)
                              for player in capitalized_players}

    average = round(sum(scores.values()) / len(capitalized_players), 2)

    high_scores: dict[str, int] = {player: score for player,
                                   score in scores.items() if score > average}

    print(f"New list with all names capitalized: {capitalized_players}")
    print(f"New list of capitalized names only: {capitalized_only}\n")
    print(f"Score dict: {scores}")
    print(f"Score average: {average}")
    print(f"High scores: {high_scores}")
