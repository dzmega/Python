import requests

API_KEY = '10596a5f999e4f358257769727ed680f'
ingredients = ["onion","pork"]
url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={','.join(ingredients)}&apiKey={API_KEY}"
response = requests.get(url)
recipes = response.json()
for recipe in recipes:
    print(recipe['title'])