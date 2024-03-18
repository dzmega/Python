# importieren der benötigten bibliotheken
from flask import Flask, render_template, request
import requests
from urllib.parse import unquote
from googletrans import Translator

#deklaration der benötigten variablen
app = Flask(__name__)
API_KEY = '1971efa6b4b844ccb7548327d28099e9'
translator = Translator()
global language

#main-fenster in der webanwendung
@app.route('/', methods=['GET', 'POST'])
def index():
    #default sprache auf englisch setzen
    global language
    language = 'en'

    #nach eingabe rezept suchen
    if request.method == 'POST':
        query = request.form.get('search_query', '')

        #nach rezepte suchen und titel übersetzten
        recipes = search_recipes(query)
        for r in recipes:
            r['title'] = translateRecipe(r['title'])

        return render_template('index.html', recipes=recipes, search_query=query)

    #mit get vorhandene gerichte laden
    #rufe wert von url-parameter ab
    search_query = request.args.get('search_query', '')
    decoded_search_query = unquote(search_query)
    recipes = search_recipes(decoded_search_query)

    return render_template('index.html', recipes=recipes, search_query=decoded_search_query)


#fenster für rezeptanzeige
@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    #anfrage für daten des jeweiligen rezept
    search_query = request.args.get('search_query', '')
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information'
    params = {
        'apiKey': API_KEY,
    }
    response = requests.get(url, params=params)
    recipe = response.json()

    #daten in die jeweilige eingegebene sprache übersetzen
    recipe['title'] = translateRecipe(recipe['title'])
    for ingredient in recipe['extendedIngredients']:
        ingredient['original'] = translateRecipe(ingredient['original'])
    for instruction in recipe['analyzedInstructions']:
        for step in instruction['steps']:
            step['step'] = translateRecipe(step['step'])

    return render_template('view_recipe.html', recipe=recipe, search_query=search_query)


#fenster für suche mit zutaten
@app.route('/search', methods=['GET', 'POST'])
def searchByIngredients():
    global language
    translatedIngredients = []

    #default sprache auf englisch setzten
    global language
    language = 'en'

    if request.method == 'POST':
        req = request.form

        #zutaten aus dem request herauslesen und speichern
        ingredients = [value for key, value in req.items() if key.startswith('ingredient_') and value]

        # zutaten werden in das englische für die suche übersetzt
        if ingredients:
            translateValue(ingredients[0])
            for i in ingredients:
                i = translateValue(i)
                translatedIngredients.append(i)

            #zutaten zusammenfassen und nach rezept suchen
            url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={','.join(translatedIngredients)}"
            parameters = {
                'apiKey': API_KEY,
                'number': 20,
                'instructionsRequired': True,
                'addRecipeInformation': True,
                'fillIngredients': True,
            }
            response = requests.get(url, params=parameters)
            data = response.json()

            #titel in gesuchter sprache übersetzen
            for d in data:
                d['title'] = translateRecipe(d['title'])

            return render_template('search.html', recipes=data)
        else:
            return render_template('search.html')
    return render_template('search.html')


def search_recipes(query):
    #werte für rezeptsuche festlegen
    query = translateValue(query)
    url = f'https://api.spoonacular.com/recipes/complexSearch'
    params = {
        'apiKey': API_KEY,
        'query': query,
        'number': 20,
        'instructionsRequired': True,
        'addRecipeInformation': True,
        'fillIngredients': True,
    }

    #rezepte suchen und als json zurücksenden
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    return []

def translateRecipe(value):
    #rezept in die jeweils eingegebene sprache übersetzen
    translation = translator.translate(value, src='en', dest=language)
    return translation.text


def translateValue(value):
    global language
    #eingegebene sprache für suche ins englische mit übersetzen
    translation = translator.translate(value, src='auto', dest='en')
    if translation.src != 'en':
        language = translation.src
    return translation.text


#starten der webanwendung
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)