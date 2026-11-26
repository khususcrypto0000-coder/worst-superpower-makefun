import os

ENTRY = "I can instantly count every grain of rice in a bowl \u2014 but only after you've finished eating it."


def main():
    assert 1 <= len(ENTRY) <= 140, len(ENTRY)
    assert ENTRY.strip() == ENTRY
    assert "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
