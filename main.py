"""One-line office placard: an ordinary office object, labelled as an
ancient artifact for a dry-witted museum curator."""

import os


PLACARD = (
    "Paper Jam, c. 1997. Ritual device for summoning the IT priesthood: "
    "it blinks red, accepts no offering, and demands a virgin ream. "
    "Donated by Accounting."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLACARD)
    print(PLACARD)


if __name__ == "__main__":
    main()
