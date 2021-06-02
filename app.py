from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route('/')
def hi():
    print('hi')

@app.route('/jadwal-sholat', methods=['GET'])
def getJadwalSholat():
    res = requests.get('https://api.pray.zone/v2/times/day.json?city=mecca&date=2021-06-02')
    