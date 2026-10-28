import random

ACHIEVEMENTS: list[str] = [
    "Crafting Genius", "Strategist", "World Savior", "Speed Runner",
    "Survivor", "Master Explorer", "Treasure Hunter", "Unstoppable",
    "First Steps", "Collector Supreme", "Untouchable", "Sharp Mind",
    "Boss Slayer", "Hidden Path Finder"
]


def gen_player_achievements() -> set[str]:
    count = random.randint(4, 9)
    picked = random.sample(ACHIEVEMENTS, count)
    return set(picked)


if __name__ == "__main__":
    print("=== Achievements Tracker System ===\n")

    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    players = [
        ("Alice", alice), ("Bob", bob), ("Charlie", charlie), ("Dylan", dylan)
    ]
    for name, achievements in players:
        print(f"Player {name}: {achievements}")
    all_achievements = alice.union(bob, charlie, dylan)
    print(f"\nAll distinct achievements: {all_achievements}")
    common_achievements = alice.intersection(bob, charlie, dylan)
    print(f"\nCommon achievements: {common_achievements}\n")

    alice_achieve = alice.difference(bob.union(charlie, dylan))
    bob_achieve = bob.difference(alice.union(charlie, dylan))
    charlie_achieve = charlie.difference(alice.union(bob, dylan))
    dylan_achieve = dylan.difference(alice.union(bob, charlie))
    print(f"Only Alice has: {alice_achieve}")
    print(f"Only Bob has: {bob_achieve}")
    print(f"Only Charlie has: {charlie_achieve}")
    print(f"Only Dylan has: {dylan_achieve}")

    print(f"\nAlice is missing: {all_achievements.difference(alice)}")
    print(f"Bob is missing: {all_achievements.difference(bob)}")
    print(f"Charlie is missing: {all_achievements.difference(charlie)}")
    print(f"Dylan is missing: {all_achievements.difference(dylan)}")
