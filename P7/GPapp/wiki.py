#! /usr/bin/env python3
# coding: utf-8

import wikipedia


class Wiki:

    # Get the question as an attribute
    def __init__(self, place):
        wikipedia.set_lang("fr")
        self.place = " " + place

    # Return the first 2 sentence of wiki
    def wiki_quote(self):
        search = wikipedia.search(self.place)
        if search == []:
            result = "Je ne me rappelle de rien à propos de ce lieu."
        else:
            title_page = search[0]
            text = wikipedia.summary(title_page, sentences=2)
            result = ("Le saviez-vous : " + text)
        return result

    # Return the link of the page
    def wiki_link(self):
        link = wikipedia.page(self.place)
        result = link.url
        return result
