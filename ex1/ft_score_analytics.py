import sys


def get_valid_inputs(args: list[str]) -> list[int]:
    valid_inputs: list[int] = []
    for arg in args:
        try:
            valid_inputs.append(int(arg))
        except Exception:
            print(f"Invalid parameter: '{arg}'")
    return valid_inputs


if __name__ == "__main__":
    valid_inputs: list[int] = []
    print("=== Player Score Analytics ===")
    valid_inputs = get_valid_inputs(sys.argv[1:])
    if not valid_inputs:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        exit(1)
    msg = ", ".join(str(i) for i in valid_inputs)
    print(f"Scores processed: [{msg}]")
    total_players = len(valid_inputs)
    total_score = sum(valid_inputs)
    high_score = max(valid_inputs)
    low_score = min(valid_inputs)

    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {total_score / total_players}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {high_score - low_score}")
