import sys
import os

print("Minecraft Community Edition")
print("Start set")

print("Set you language:")
print("English(United States of America):en_US")
print("简体中文(中华人民共和国):zh_CN")

lang = input("Set:")

print('You game language is:' + lang)
os.system("python launcher.py " + lang)