from flask import Flask, render_template, request, redirect
from peewee import *
from models import Countries
import requests

app = Flask(__name__)

@app.route('/')
def lie():
    all_countries = Countries.select()
    return render_template("index.html", Countries=all_countries)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    res = requests.get('https://restcountries.com/v3.1/all')
    a = 0 
    for i in range(20):
        name = res.json()
        name = name[a]["name"]["common"]
        a+=1
        offical_name = res.json()
        offical_name = offical_name[a]["name"]["official"]

        capital = res.json()
        capital = capital[a]["capital"][0]
        
        region = res.json()
        region = region[a]["region"]
        
        subregion = res.json()
        subregion = subregion[a]["subregion"]
         
        population = res.json()
        population = population[a]["population"]
         
        continents = res.json()
        continents = continents[a]["continents"][0]
        
        timezones = res.json()
        timezones = timezones[a]["timezones"][0]
    
        Countries.create(
            name = name,
            official_name = offical_name,
            capital = capital,
            region = region,
            subregion = subregion,
            population = population,
            continents = continents,
            timezones = timezones
            )
        # return redirect('/')
    return render_template('create.html')

if __name__ == "__main__":
    app.run(debug=True)