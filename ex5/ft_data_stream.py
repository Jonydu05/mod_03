from random import choice
from typing import Generator


PLAYERS: list[str] = ["charlie", "dylan", "alice", "bob"]
ACTIONS: list[str] = ["move", "grab", "use", "swim", "run",
                      "climb", "release", "eat", "sleep"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        player = choice(PLAYERS)
        action = choice(ACTIONS)
        yield (player, action)


def consume_event(arr: list[tuple[str, str]]) -> None:
    event_picked = choice(arr)
    print(f"Got event from list: {event_picked}")
    arr.remove(event_picked)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    list_actions: list[tuple[str, str]] = []

    for i in range(1000):
        player_action = next(gen_event())
        if (i <= 9):
            list_actions.append(player_action)
        print(f"Event {i}: "
              f"Player {player_action[0]} did action {player_action[1]}")

    print(f"Built list of {len(list_actions)} events: {list_actions}")
    for i in range(len(list_actions)):
        consume_event(list_actions)
        print(f"Remains in list: {list_actions}")
