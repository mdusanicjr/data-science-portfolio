# My first Python project in GitHub
# Orginal code:
# def greet_user():
# name = input("Enter your name: ")
# print(f"Hello, {name}! Welcome to Data Science.")
# if __name__ == "__main__":
# greet_user()

def greet_user():
  name = input("Enter your favorite NFL team")
  if name == "49ers" or "Niners" in name:
    print("Bang Bang Niner Gang")
  elif "Rams" in name:
    print("Same old sorry ass Lambs")
  else:
    print("My favorite team is better than your favorite team")

if __name__ == "__main__":
  greet_user()
