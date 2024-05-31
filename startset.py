import sys
import os

print("Minecraft Community Edition")
print("Start set")

print("Set you language:")
print("English(United States of America):en_US")
print("English(United Kingdom of Great Britain and Northern Ireland):en_UK")
print("简体中文(中华人民共和国、新加坡共和国、马来西亚):zh_CN")
print("繁體中文(中华人民共和国臺灣省、香港特別行政區、澳門特別行政區):zh_TW")
print("Русский язык(Российская Федерация):ru_RU")



lang = input("Set:")

print('You game language is:' + lang)
os.system("python launcher.py " + lang)