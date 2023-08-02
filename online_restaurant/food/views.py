from django.shortcuts import render

# Create your views here.

def index(request):
    meals = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."
        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."
        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."
        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."
        },
        {
            "strMeal": "Pate Chinois",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "idMeal": "This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."
        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."
        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."
        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."
        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "idMeal": "This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer."
        }
    ]
    return render (request, './food/index.html', {'meals': meals})
