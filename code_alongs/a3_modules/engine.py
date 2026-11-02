
print("hej från engine")

class Engine:
    print("engine here")

# __name__ -> filename when imported
# __name__ -> __main__ when run directly
print(f"{__name__ = }")

# only run as standalone script
if __name__ == "__main__":
    print(f"engines inside of {__name__}")
