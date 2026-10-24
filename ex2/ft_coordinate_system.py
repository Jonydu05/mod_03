from math import sqrt


def get_player_pos() -> tuple[float, float, float]:
    user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
    split_input = user_input.split(",")
    if len(split_input) != 3:
        raise Exception("Invalid Syntax")
    try:
        x = float(split_input[0].strip())
        y = float(split_input[1].strip())
        z = float(split_input[2].strip())
    except ValueError:
        raise Exception("Invalid Syntax")
    coord = (x, y, z)
    center_at = sqrt(
        coord[0] ** 2 + coord[1] ** 2 + coord[2] ** 2
    )
    print(f"Got first tuple: {coord}")
    print(f"It includes: X={x}, Y={y}, Z={z}")
    print(f"Distance to center: {round(center_at, 4)}")
    return coord


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("\nGet first set of coordinates")
    try:
        first_coord = get_player_pos()
    except Exception as e:
        print(e)
    print("\nGet second set of coordinates")
    try:
        second_coord = get_player_pos()
    except Exception as e:
        print(e)
    distance_coords = sqrt(
        (second_coord[0] - first_coord[0]) ** 2
        + (second_coord[1] - first_coord[1]) ** 2
        + (second_coord[2] - first_coord[2]) ** 2
    )
    print(f"Distance between the 2 sets of coordinates: {distance_coords}")
