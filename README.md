🍽️ ## **Food Explorer**
A Python-powered web app that helps users explore, filter, and discover delicious dishes tailored to their dietary needs, cuisines, allergen concerns, and taste preferences. Built with the power of Owlready2 for semantic reasoning and Gradio for an elegant and interactive interface.

🔍 **Overview**
Food Explorer is a semantic food recommendation system that uses an ontology to reason about:

🍱 Dishes

🍽️ Cuisines

🥗 Diets

⚠️ Allergens

🧂 Ingredients & Nutrition

🌟 **Core Features**
🔎 Search Dishes: View detailed information (cuisine, allergens, nutrition, ingredients) for selected dishes.

🔧 Filter Dishes: Narrow down dishes using filters like cuisine, diet, allergens, preparation time, calories, and spiciness.

🎯 Recommend Dish: Receive a personalized dish suggestion based on your preferences and restrictions.


💡 How to Use
🗂️ Tabs & Features
Search Dishes

Choose a dish from a dropdown

Select which attributes to display (cuisine, allergens, ingredients, etc.)

Filter Dishes

Apply filters:

Cuisine

Diet (e.g., Vegan, Keto)

Allergen-free (e.g., No Gluten)

Max Preparation Time / Calories

Spiciness level

Sort results by name, prep time, or calories

Recommend Dish

Set dietary needs and allergen exclusions

Get a single dish tailored to your preferences

🧠 Ontology Details
Built with Owlready2, the ontology models the food domain with:

🏷️ Classes
Cuisine, Diet, Allergen, Dish, Ingredient, Nutrition

🔗 Properties
hasCuisine, suitableFor, containsAllergen, hasIngredient

preparationTime, isSpicy

Nutrition details: calories, protein, carbs

🧠 Reasoning Rules
Automatically infers:

isVegetarian

isVegan

isGlutenFree

Based on ingredients and allergens

📊 Sample Data
Cuisines: Italian, Indian, etc.

Diets: Vegan, Keto, etc.

Dishes: Pizza, Sushi, Hummus

Allergens: Gluten, Dairy, etc.

🎨 Interface Design
Built with Gradio using:

Dropdowns, checkboxes, sliders, radio buttons

Tabs for intuitive navigation

Custom CSS:

Food-themed visuals 🍝

Orange accent color 🧡

Responsive layout 📱

📁 **Project Structure**
bash
Copy
Edit
📁 food-explorer/
├── food_explorer.py       # Main app script
├── food_ontology.owl      # Ontology file (place it as configured)
└── README.md              # Project documentation
🔧 Notes & Tips
File Path: Update the hardcoded path to your local ontology file.

Extensibility: You can add new dishes, diets, cuisines, or rules by editing the ontology definitions in food_explorer.py.

Dependencies: Check Owlready2 and Gradio version compatibility if issues arise.


🙌 Acknowledgments
🧠 Owlready2 – Ontology reasoning and management

🌐 Gradio – Elegant interactive web interfaces

🍜 Inspired by food lovers & knowledge representation principles





