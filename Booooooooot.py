import time
import telebot
import xmltodict
import random
import json
import requests

bot = telebot.TeleBot("7097102560:AAFmw9QKpzbE2cNUYjiHRyxiBm9s6_hRqpk", parse_mode=None)

def create_record(data, leviy_file):
    with open(leviy_file, 'w') as file:
        json.dump(data, file)

def read_record(filee):
    with open(filee, 'r') as file:
        data = json.load(file)
        return data

def update_record(filename, new_value):
    data = read_record(filename)
    data.append(new_value)
    create_record(data, filename)