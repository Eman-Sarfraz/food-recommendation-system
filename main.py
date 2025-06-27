from owlready2 import *
import gradio as gr
import uuid

# Create Ontology (unchanged)
onto = get_ontology(r"C:\Users\HP\Desktop\KRR proj\food_ontology.owl")

with onto:
    # Classes
    class Cuisine(Thing): pass
    class Diet(Thing): pass
    class Allergen(Thing): pass
    class Dish(Thing): pass
    class Ingredient(Thing): pass
    class Nutrition(Thing): pass

    # Properties
    class hasCuisine(Dish >> Cuisine): pass
    class suitableFor(Dish >> Diet): pass
    class containsAllergen(Dish >> Allergen): pass
    class hasIngredient(Dish >> Ingredient): pass
    class preparationTime(Dish >> int, FunctionalProperty): pass
    class isSpicy(Dish >> bool, FunctionalProperty): pass
    class hasNutrition(Dish >> Nutrition): pass
    class calories(Nutrition >> int, FunctionalProperty): pass
    class protein(Nutrition >> int, FunctionalProperty): pass
    class carbs(Nutrition >> int, FunctionalProperty): pass

    # Cuisines
    italian = Cuisine("Italian")
    indian = Cuisine("Indian")
    chinese = Cuisine("Chinese")
    mexican = Cuisine("Mexican")
    japanese = Cuisine("Japanese")
    french = Cuisine("French")
    pakistani = Cuisine("Pakistani")
    american = Cuisine("American")
    thai = Cuisine("Thai")
    mediterranean = Cuisine("Mediterranean")

    # Diets
    vegan = Diet("Vegan")
    vegetarian = Diet("Vegetarian")
    keto = Diet("Keto")
    gluten_free = Diet("GlutenFree")
    paleo = Diet("Paleo")
    low_carb = Diet("LowCarb")

    # Allergens
    gluten = Allergen("Gluten")
    nuts = Allergen("Nuts")
    dairy = Allergen("Dairy")
    shellfish = Allergen("Shellfish")
    soy = Allergen("Soy")
    eggs = Allergen("Eggs")

    # Ingredients
    tomato = Ingredient("Tomato")
    cheese = Ingredient("Cheese")
    spinach = Ingredient("Spinach")
    paneer = Ingredient("Paneer")
    chicken = Ingredient("Chicken")
    peanuts = Ingredient("Peanuts")
    avocado = Ingredient("Avocado")
    rice = Ingredient("Rice")
    shrimp = Ingredient("Shrimp")
    tofu = Ingredient("Tofu")
    beef = Ingredient("Beef")
    eggplant = Ingredient("Eggplant")
    noodles = Ingredient("Noodles")
    chickpeas = Ingredient("Chickpeas")

    # Nutrition instances
    pizza_nutrition = Nutrition("PizzaNutrition", calories=800, protein=30, carbs=90)
    palak_paneer_nutrition = Nutrition("PalakPaneerNutrition", calories=600, protein=20, carbs=30)
    kung_pao_nutrition = Nutrition("KungPaoChickenNutrition", calories=700, protein=35, carbs=40)
    tacos_nutrition = Nutrition("TacosNutrition", calories=500, protein=25, carbs=50)
    sushi_nutrition = Nutrition("SushiNutrition", calories=400, protein=20, carbs=60)
    ratatouille_nutrition = Nutrition("RatatouilleNutrition", calories=200, protein=5, carbs=25)
    biryani_nutrition = Nutrition("BiryaniNutrition", calories=900, protein=40, carbs=100)
    nihari_nutrition = Nutrition("NihariNutrition", calories=800, protein=45, carbs=20)
    burger_nutrition = Nutrition("BurgerNutrition", calories=700, protein=30, carbs=50)
    hot_dog_nutrition = Nutrition("HotDogNutrition", calories=600, protein=15, carbs=45)
    chow_mein_nutrition = Nutrition("ChowMeinNutrition", calories=650, protein=20, carbs=80)
    pad_thai_nutrition = Nutrition("PadThaiNutrition", calories=700, protein=25, carbs=90)
    hummus_nutrition = Nutrition("HummusNutrition", calories=300, protein=10, carbs=20)

    # Dishes
    pizza = Dish("Pizza")
    pizza.hasCuisine = [italian]
    pizza.suitableFor = []
    pizza.containsAllergen = [gluten, dairy]
    pizza.hasIngredient = [tomato, cheese]
    pizza.preparationTime = 30
    pizza.isSpicy = False
    pizza.hasNutrition = [pizza_nutrition]

    palak_paneer = Dish("PalakPaneer")
    palak_paneer.hasCuisine = [indian]
    palak_paneer.suitableFor = [vegetarian]
    palak_paneer.containsAllergen = [dairy]
    palak_paneer.hasIngredient = [spinach, paneer]
    palak_paneer.preparationTime = 45
    palak_paneer.isSpicy = True
    palak_paneer.hasNutrition = [palak_paneer_nutrition]

    kung_pao = Dish("KungPaoChicken")
    kung_pao.hasCuisine = [chinese]
    kung_pao.suitableFor = []
    kung_pao.containsAllergen = [nuts, soy]
    kung_pao.hasIngredient = [chicken, peanuts]
    kung_pao.preparationTime = 25
    kung_pao.isSpicy = True
    kung_pao.hasNutrition = [kung_pao_nutrition]

    tacos = Dish("Tacos")
    tacos.hasCuisine = [mexican]
    tacos.suitableFor = []
    tacos.containsAllergen = [gluten]
    tacos.hasIngredient = [avocado, beef]
    tacos.preparationTime = 20
    tacos.isSpicy = True
    tacos.hasNutrition = [tacos_nutrition]

    sushi = Dish("Sushi")
    sushi.hasCuisine = [japanese]
    sushi.suitableFor = [keto]
    sushi.containsAllergen = [shellfish]
    sushi.hasIngredient = [rice, shrimp]
    sushi.preparationTime = 40
    sushi.isSpicy = False
    sushi.hasNutrition = [sushi_nutrition]

    ratatouille = Dish("Ratatouille")
    ratatouille.hasCuisine = [french]
    ratatouille.suitableFor = [vegan, vegetarian]
    ratatouille.containsAllergen = []
    ratatouille.hasIngredient = [tomato, eggplant]
    ratatouille.preparationTime = 60
    ratatouille.isSpicy = False
    ratatouille.hasNutrition = [ratatouille_nutrition]

    biryani = Dish("Biryani")
    biryani.hasCuisine = [pakistani]
    biryani.suitableFor = []
    biryani.containsAllergen = [gluten]
    biryani.hasIngredient = [rice, chicken]
    biryani.preparationTime = 90
    biryani.isSpicy = True
    biryani.hasNutrition = [biryani_nutrition]

    nihari = Dish("Nihari")
    nihari.hasCuisine = [pakistani]
    nihari.suitableFor = []
    nihari.containsAllergen = [gluten]
    nihari.hasIngredient = [beef]
    nihari.preparationTime = 120
    nihari.isSpicy = True
    nihari.hasNutrition = [nihari_nutrition]

    burger = Dish("Burger")
    burger.hasCuisine = [american]
    burger.suitableFor = []
    burger.containsAllergen = [gluten, dairy]
    burger.hasIngredient = [beef, cheese]
    burger.preparationTime = 15
    burger.isSpicy = False
    burger.hasNutrition = [burger_nutrition]

    hot_dog = Dish("HotDog")
    hot_dog.hasCuisine = [american]
    hot_dog.suitableFor = []
    hot_dog.containsAllergen = [gluten]
    hot_dog.hasIngredient = [beef]
    hot_dog.preparationTime = 10
    hot_dog.isSpicy = False
    hot_dog.hasNutrition = [hot_dog_nutrition]

    chow_mein = Dish("ChowMein")
    chow_mein.hasCuisine = [chinese]
    chow_mein.suitableFor = []
    chow_mein.containsAllergen = [gluten, soy]
    chow_mein.hasIngredient = [noodles, chicken]
    chow_mein.preparationTime = 20
    chow_mein.isSpicy = False
    chow_mein.hasNutrition = [chow_mein_nutrition]

    pad_thai = Dish("PadThai")
    pad_thai.hasCuisine = [thai]
    pad_thai.suitableFor = []
    pad_thai.containsAllergen = [nuts, shellfish]
    pad_thai.hasIngredient = [noodles, shrimp, peanuts]
    pad_thai.preparationTime = 30
    pad_thai.isSpicy = True
    pad_thai.hasNutrition = [pad_thai_nutrition]

    hummus = Dish("Hummus")
    hummus.hasCuisine = [mediterranean]
    hummus.suitableFor = [vegan, vegetarian, gluten_free]
    hummus.containsAllergen = []
    hummus.hasIngredient = [chickpeas]
    hummus.preparationTime = 15
    hummus.isSpicy = False
    hummus.hasNutrition = [hummus_nutrition]

    # Reasoning Rules
    class isVegetarian(Dish >> bool, FunctionalProperty): pass
    class isVegan(Dish >> bool, FunctionalProperty): pass
    class isGlutenFree(Dish >> bool, FunctionalProperty): pass

    for d in Dish.instances():
        if not d.containsAllergen or not any(a.name in ['Meat', 'Shellfish'] for a in d.containsAllergen):
            if vegetarian not in d.suitableFor:
                d.suitableFor.append(vegetarian)
                d.isVegetarian = True

        if not d.containsAllergen or not any(a.name in ['Dairy', 'Meat', 'Shellfish', 'Eggs'] for a in d.containsAllergen):
            if vegan not in d.suitableFor:
                d.suitableFor.append(vegan)
                d.isVegan = True

        if not d.containsAllergen or 'Gluten' not in [a.name for a in d.containsAllergen]:
            if gluten_free not in d.suitableFor:
                d.suitableFor.append(gluten_free)
                d.isGlutenFree = True

# Save ontology
onto.save(file=r"C:\Users\HP\Desktop\KRR proj\food_ontology.owl")

# Interface Functions (unchanged)
def query_dish_info(dish_name, show_cuisine, show_diet, show_allergen, show_ingredients, show_nutrition, show_preptime, show_spicy, show_all_dishes):
    if show_all_dishes:
        all_info = "## 🍴 All Dishes\n\n"
        for dish in Dish.instances():
            all_info += f"### {dish.name}\n"
            if show_cuisine:
                cuisine = ", ".join(c.name for c in dish.hasCuisine) or "None"
                all_info += f"- 🌍 **Cuisine**: {cuisine}\n"
            if show_diet:
                diets = ", ".join(d.name for d in dish.suitableFor) or "None"
                all_info += f"- 🥗 **Suitable For**: {diets}\n"
            if show_allergen:
                allergens = ", ".join(a.name for a in dish.containsAllergen) or "None"
                all_info += f"- ⚠️ **Allergens**: {allergens}\n"
            if show_ingredients:
                ingredients = ", ".join(i.name for i in dish.hasIngredient) or "None"
                all_info += f"- 🥕 **Ingredients**: {ingredients}\n"
            if show_nutrition and dish.hasNutrition:
                nutrition = dish.hasNutrition[0]
                all_info += f"- 📊 **Nutrition**: {nutrition.calories} kcal, {nutrition.protein}g protein, {nutrition.carbs}g carbs\n"
            if show_preptime:
                all_info += f"- ⏰ **Prep Time**: {dish.preparationTime} minutes\n"
            if show_spicy:
                all_info += f"- 🌶️ **Spicy**: {'Yes' if dish.isSpicy else 'No'}\n"
            all_info += "\n"
        return all_info

    dish = onto.search_one(iri="*" + dish_name.replace(" ", ""))
    if not dish:
        return f"❌ Dish not found. Try one from: {', '.join(dish_names)}."

    output = f"## 🍽️ {dish.name}\n\n"
    if show_cuisine:
        cuisine = ", ".join(c.name for c in dish.hasCuisine) or "None"
        output += f"- 🌍 **Cuisine**: {cuisine}\n"
    if show_diet:
        diets = ", ".join(d.name for d in dish.suitableFor) or "None"
        output += f"- 🥗 **Suitable For**: {diets}\n"
    if show_allergen:
        allergens = ", ".join(a.name for a in dish.containsAllergen) or "None"
        output += f"- ⚠️ **Allergens**: {allergens}\n"
    if show_ingredients:
        ingredients = ", ".join(i.name for i in dish.hasIngredient) or "None"
        output += f"- 🥕 **Ingredients**: {ingredients}\n"
    if show_nutrition and dish.hasNutrition:
        nutrition = dish.hasNutrition[0]
        output += f"- 📊 **Nutrition**: {nutrition.calories} kcal, {nutrition.protein}g protein, {nutrition.carbs}g carbs\n"
    if show_preptime:
        output += f"- ⏰ **Prep Time**: {dish.preparationTime} minutes\n"
    if show_spicy:
        output += f"- 🌶️ **Spicy**: {'Yes' if dish.isSpicy else 'No'}\n"
    return output

def filter_dishes(cuisine_filter, diet_filter, allergen_free, max_preptime, max_calories, spicy_preference, sort_by):
    results = []
    for dish in Dish.instances():
        include = True
        if cuisine_filter and cuisine_filter != "Any":
            if not any(c.name == cuisine_filter for c in dish.hasCuisine):
                include = False
        if diet_filter and diet_filter != "Any":
            if not any(d.name == diet_filter for d in dish.suitableFor):
                include = False
        if allergen_free and allergen_free != "Any":
            if any(a.name == allergen_free for a in dish.containsAllergen):
                include = False
        if max_preptime and dish.preparationTime > max_preptime:
            include = False
        if max_calories and dish.hasNutrition and dish.hasNutrition[0].calories > max_calories:
            include = False
        if spicy_preference != "Any":
            is_spicy = dish.isSpicy == (spicy_preference == "Spicy")
            if not is_spicy:
                include = False
        if include:
            results.append(dish)

    if sort_by == "Name":
        results.sort(key=lambda d: d.name)
    elif sort_by == "Preparation Time":
        results.sort(key=lambda d: d.preparationTime)
    elif sort_by == "Calories":
        results.sort(key=lambda d: d.hasNutrition[0].calories if d.hasNutrition else 0)

    if not results:
        return "❌ No dishes match your criteria."
    output = "**🍴 Matching Dishes**:\n\n"
    for dish in results:
        output += f"- **{dish.name}**  \n"
        output += f"  🌍 Cuisine: {', '.join(c.name for c in dish.hasCuisine)}  \n"
        output += f"  🥗 Diets: {', '.join(d.name for d in dish.suitableFor) or 'None'}  \n"
        output += f"  📊 Calories: {dish.hasNutrition[0].calories if dish.hasNutrition else 'N/A'} kcal  \n"
        output += f"  ⏰ Prep Time: {dish.preparationTime} min\n\n"
    return output

def recommend_dish(diet_preference, avoid_allergen, prefer_spicy):
    scores = []
    for dish in Dish.instances():
        score = 0
        if diet_preference and diet_preference != "Any":
            if any(d.name == diet_preference for d in dish.suitableFor):
                score += 2
        if avoid_allergen and avoid_allergen != "Any":
            if not any(a.name == avoid_allergen for a in dish.containsAllergen):
                score += 2
        if prefer_spicy != "Any":
            if dish.isSpicy == (prefer_spicy == "Spicy"):
                score += 1
        scores.append((dish, score))

    scores.sort(key=lambda x: x[1], reverse=True)
    if not scores or scores[0][1] == 0:
        return "❌ No suitable dishes found."
    top_dish = scores[0][0]
    return f"## 🍽️ Recommended: {top_dish.name}\n\n" \
           f"- 🌍 **Cuisine**: {', '.join(c.name for c in top_dish.hasCuisine)}\n" \
           f"- 🥗 **Suitable For**: {', '.join(d.name for d in top_dish.suitableFor) or 'None'}\n" \
           f"- ⚠️ **Allergens**: {', '.join(a.name for a in top_dish.containsAllergen) or 'None'}\n" \
           f"- 🥕 **Ingredients**: {', '.join(i.name for i in top_dish.hasIngredient) or 'None'}\n" \
           f"- 📊 **Nutrition**: {top_dish.hasNutrition[0].calories if top_dish.hasNutrition else 'N/A'} kcal\n" \
           f"- ⏰ **Prep Time**: {top_dish.preparationTime} minutes\n" \
           f"- 🌶️ **Spicy**: {'Yes' if top_dish.isSpicy else 'No'}\n"

# Dish dropdown options
dish_names = sorted([d.name for d in Dish.instances()])

# Enhanced Custom CSS with Food Pattern Background
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* General styling */
body, .gradio-container {
    font-family: 'Inter', Arial, sans-serif !important;
    background: url('https://www.transparenttextures.com/patterns/food.png') repeat, linear-gradient(135deg, #fef3e2 0%, #fff7ed 100%) !important;
    background-size: auto, cover !important;
    color: #333333 !important;
}

/* Header styling */
h1, h2, h3 {
    color: #e65100 !important; /* Deep orange for headers */
    font-weight: 700 !important;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1) !important;
}

/* Tabs styling */
.tab-nav {
    background: #ffffff !important;
    border: 1px solid #fed7aa !important; /* Soft peach border */
    border-radius: 8px !important;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1) !important;
}

.tab-nav button {
    font-weight: 600 !important;
    color: #7c2d12 !important; /* Dark orange text */
    background: #fff7ed !important;
    border-radius: 6px !important;
    padding: 10px 20px !important;
    margin: 4px !important;
    transition: all 0.3s ease !important;
}

.tab-nav button:hover {
    background: #f97316 !important; /* Vibrant orange on hover */
    color: #ffffff !important;
}

.tab-nav button.selected {
    background: #e65100 !important; /* Deep orange for active tab */
    color: #ffffff !important;
}

/* Markdown output styling */
.markdown-output {
    background: #ffffff !important;
    padding: 20px !important;
    border-radius: 12px !important;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1) !important;
    line-height: 1.8 !important;
    font-size: 16px !important;
    border-left: 4px solid #f97316 !important; /* Orange accent */
}

/* Input and button styling */
input, select, .gr-button {
    border: 1px solid #fed7aa !important; /* Soft peach border */
    border-radius: 8px !important;
    padding: 10px !important;
    transition: all 0.3s ease !important;
}

input:focus, select:focus {
    border-color: #f97316 !important;
    box-shadow: 0 0 0 3px rgba(249, 115, 22, 0.2) !important;
}

.gr-button {
    background: #f97316 !important; /* Vibrant orange buttons */
    color: #ffffff !important;
    font-weight: 600 !important;
    padding: 12px 24px !important;
    border-radius: 8px !important;
}

.gr-button:hover {
    background: #e65100 !important; /* Darker orange on hover */
    transform: translateY(-1px) !important;
}

.gr-button:active {
    transform: translateY(0) !important;
}

/* Checkbox and radio styling */
.gr-checkbox, .gr-radio {
    accent-color: #f97316 !important;
}

/* Slider styling */
.gr-slider input[type="range"] {
    accent-color: #f97316 !important;
}

/* Container styling */
.gr-row, .gr-column {
    gap: 16px !important;
}

/* Card-like styling for content blocks */
.gr-block {
    background: rgba(255, 255, 255, 0.95) !important;
    border-radius: 12px !important;
    padding: 20px !important;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important;
}

/* Footer or subtle branding */
footer {
    color: #7c2d12 !important;
    font-size: 12px !important;
    text-align: center !important;
    margin-top: 20px !important;
}
"""

# Enhanced Gradio UI
with gr.Blocks(
    theme=gr.themes.Default(
        primary_hue="orange",
        secondary_hue="blue",
        font=["Inter", "Arial", "sans-serif"],
        spacing_size="lg",
        radius_size="lg"
    ),
    css=custom_css
) as demo:
    gr.Markdown(
        """
        <div style='text-align: center; padding: 20px;'>
            <h1 style='font-size: 2.5rem; margin-bottom: 10px;'>🍴 Food Explorer</h1>
            <p style='font-size: 1.2rem; color: #7c2d12;'>Discover delicious dishes from around the world! Filter by preferences, explore cuisines, or get personalized recommendations.</p>
        </div>
        """,
        elem_classes=["markdown-output"]
    )

    with gr.Tabs(elem_classes=["border", "border-orange-200", "rounded-lg", "shadow-md"]):
        with gr.Tab(label="🔍 Search Dishes", elem_classes=["bg-orange-50", "rounded-lg"]):
            with gr.Row():
                with gr.Column(scale=3):
                    inp = gr.Dropdown(
                        choices=dish_names,
                        label="Select a Dish",
                        value=dish_names[0],
                        elem_classes=["border", "border-orange-300", "rounded-md"]
                    )
                with gr.Column(scale=1):
                    btn = gr.Button(
                        "Search",
                        variant="primary",
                        elem_classes=["bg-orange-500", "text-white", "hover:bg-orange-600"]
                    )

            with gr.Row():
                show_cuisine = gr.Checkbox(value=True, label="Cuisine 🌍", elem_classes=["text-gray-700"])
                show_diet = gr.Checkbox(value=True, label="Diet Suitability 🥗", elem_classes=["text-gray-700"])
                show_allergen = gr.Checkbox(value=True, label="Allergens ⚠️", elem_classes=["text-gray-700"])
                show_ingredients = gr.Checkbox(value=True, label="Ingredients 🥕", elem_classes=["text-gray-700"])
                show_nutrition = gr.Checkbox(value=True, label="Nutrition 📊", elem_classes=["text-gray-700"])
                show_preptime = gr.Checkbox(value=True, label="Prep Time ⏰", elem_classes=["text-gray-700"])
                show_spicy = gr.Checkbox(value=True, label="Spicy 🌶️", elem_classes=["text-gray-700"])
                show_all_dishes = gr.Checkbox(value=False, label="Show All Dishes 📋", elem_classes=["text-gray-700"])

            dish_out = gr.Markdown(elem_classes=["bg-white", "p-4", "rounded-lg", "shadow-md", "mt-4", "markdown-output"])

            btn.click(
                fn=query_dish_info,
                inputs=[inp, show_cuisine, show_diet, show_allergen, show_ingredients, show_nutrition, show_preptime, show_spicy, show_all_dishes],
                outputs=dish_out
            )

        with gr.Tab(label="🧂 Filter Dishes", elem_classes=["bg-blue-50", "rounded-lg"]):
            with gr.Row():
                cuisine_filter = gr.Dropdown(
                    choices=["Any"] + [c.name for c in Cuisine.instances()],
                    label="Filter by Cuisine",
                    value="Any",
                    elem_classes=["border", "border-blue-300", "rounded-md"]
                )
                diet_filter = gr.Dropdown(
                    choices=["Any"] + [d.name for d in Diet.instances()],
                    label="Filter by Diet",
                    value="Any",
                    elem_classes=["border", "border-blue-300", "rounded-md"]
                )
                allergen_free = gr.Dropdown(
                    choices=["Any"] + [a.name for a in Allergen.instances()],
                    label="Free of Allergen",
                    value="Any",
                    elem_classes=["border", "border-blue-300", "rounded-md"]
                )

            with gr.Row():
                max_preptime = gr.Slider(
                    minimum=0,
                    maximum=120,
                    value=60,
                    step=5,
                    label="Max Prep Time (min) ⏰",
                    elem_classes=["text-gray-700"]
                )
                max_calories = gr.Slider(
                    minimum=0,
                    maximum=1000,
                    value=800,
                    step=50,
                    label="Max Calories (kcal) 📊",
                    elem_classes=["text-gray-700"]
                )
                spicy_preference = gr.Radio(
                    choices=["Any", "Spicy", "Non-Spicy"],
                    label="Spicy Preference 🌶️",
                    value="Any",
                    elem_classes=["text-gray-700"]
                )

            with gr.Row():
                sort_by = gr.Radio(
                    choices=["Name", "Preparation Time", "Calories"],
                    label="Sort By",
                    value="Name",
                    elem_classes=["text-gray-700"]
                )
                filter_btn = gr.Button(
                    "Filter",
                    variant="primary",
                    elem_classes=["bg-blue-500", "text-white", "hover:bg-blue-600"]
                )

            filter_out = gr.Markdown(elem_classes=["bg-white", "p-4", "rounded-lg", "shadow-md", "mt-4", "markdown-output"])

            filter_btn.click(
                fn=filter_dishes,
                inputs=[cuisine_filter, diet_filter, allergen_free, max_preptime, max_calories, spicy_preference, sort_by],
                outputs=filter_out
            )

        with gr.Tab(label="🎯 Recommend Dish", elem_classes=["bg-green-50", "rounded-lg"]):
            with gr.Row():
                diet_preference = gr.Dropdown(
                    choices=["Any"] + [d.name for d in Diet.instances()],
                    label="Preferred Diet",
                    value="Any",
                    elem_classes=["border", "border-green-300", "rounded-md"]
                )
                avoid_allergen = gr.Dropdown(
                    choices=["Any"] + [a.name for a in Allergen.instances()],
                    label="Avoid Allergen",
                    value="Any",
                    elem_classes=["border", "border-green-300", "rounded-md"]
                )
                prefer_spicy = gr.Radio(
                    choices=["Any", "Spicy", "Non-Spicy"],
                    label="Spicy Preference 🌶️",
                    value="Any",
                    elem_classes=["text-gray-700"]
                )

            recommend_btn = gr.Button(
                "Recommend",
                variant="primary",
                elem_classes=["bg-green-500", "text-white", "hover:bg-green-600"]
            )

            recommend_out = gr.Markdown(elem_classes=["bg-white", "p-4", "rounded-lg", "shadow-md", "mt-4", "markdown-output"])

            recommend_btn.click(
                fn=recommend_dish,
                inputs=[diet_preference, avoid_allergen, prefer_spicy],
                outputs=recommend_out
            )

    gr.Markdown(
        """
        <footer>Built for food lovers by Eman Sarfraz</footer>
        """,
        elem_classes=["text-center", "mt-8"]
    )

# Launch
if __name__ == "__main__":
    demo.launch()