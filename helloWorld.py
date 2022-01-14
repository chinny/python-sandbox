import os

""" import shutil

print("Hello, World!")

du = shutil.disk_usage("/")
print(du)

print(du.free/du.total)

user = "Jeffrey Chin"

print("Welcome, {}".format(user))

file = open("test.txt")
print(file.read())
file.close() """

with open("test.txt") as file:
    lines = file.readlines().strip()

print(lines)