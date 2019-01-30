#! /usr/bin/env python3
# coding: utf-8

from flask import Flask, render_template, request, jsonify

from GPapp.parser import Parser
from GPapp.map import GoogleMap
from GPapp.wiki import Wiki

app = Flask(__name__)

app.config.from_object('config')


@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def get_data():

    # get and parse the data
    parse = Parser()
    data = request.data.decode('utf-8')
    new_question = parse.sentence_parser(data)
    print(new_question)

    # get the wiki quote
    wiki_data = Wiki(new_question)
    wquote = wiki_data.wiki_quote()
    if wquote != "Je ne me rappelle de rien à propos de ce lieu.":
        wlink = wiki_data.wiki_link()
    else:
        wlink = ""

    # get the gps coord and the address
    gmap = GoogleMap(new_question)
    gps_coord = gmap.get_gps_coord()
    print(gps_coord)
    address = gmap.get_adress()

    dic = [gps_coord, wquote, address, wlink]

    return jsonify(dic)
