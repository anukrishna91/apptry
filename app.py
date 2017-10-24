# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 12:48:05 2017

@author: Venkata Ramana
"""

from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
	return 'Yo, its working!'
if __name__ == "__main__":
	app.run()