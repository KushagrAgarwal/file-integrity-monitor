import hashlib
import os


def get_hash(p):
    h = hashlib.sha256()

    try:
        with open(p, "rb") as f:
            d = f.read()

            while d:
                h.update(d)
                d = f.read()

        return h.hexdigest()

    except OSError:
        print("Error reading file")
        return None


def main():
    p = input("Enter file path: ").strip().strip('"')

    if not os.path.isfile(p):
        print("File does not exist")
        return

    old = get_hash(p)

    if old is None:
        return

    print("Original hash:", old)

    while True:
        print("\n1. Check file")
        print("2. Exit")
        ch = input("Enter choice: ")

        if ch == "1":
            if not os.path.isfile(p):
                print("File is missing")
                continue

            new = get_hash(p)

            if new is None:
                continue

            print("Current hash:", new)

            if old == new:
                print("File is unchanged")
            else:
                print("File has been modified")

        elif ch == "2":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
