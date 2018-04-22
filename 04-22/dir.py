#coding=utf-8
import os
os.mkdir("itarvin")
print(os.getcwd())
os.chdir("../")
print(os.getcwd())
print(os.listdir("./"))
os.rmdir("./04-22/itarvin")
