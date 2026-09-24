import sys

if __name__ == "__main__":
    index: int = 0
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[index]}")
    index+= 1
    if len(sys.argv) > 1:
        print(f"Arguments received: {len(sys.argv) - 1}")
        for arg in sys.argv[1:]:
            print(f"Argument {index}: {sys.argv[index]}")
            index+= 1
    else:
        print("No arguments provided!")
    print(f"Total arguments: {len(sys.argv)}")
