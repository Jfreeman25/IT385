#!/usr/bin/env python3

def main():
  name = input("Please enter your name: ")
  year = input("Please enter the current year: ")
  yob = input("Please enter your year of birth: ")

  print("Hello {0}, you are {1} years old" .format(name, int(year) - int(yob)))

if __name__ == "__main__":
  main()
