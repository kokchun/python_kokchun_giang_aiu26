from pathlib import Path

DATA_PATH = Path(__file__).parent / "data"

print(DATA_PATH)

print("Reading a file")

# open up quotes.txt and print it 
with open("data/quotes.txt") as file:
    print(file.read())