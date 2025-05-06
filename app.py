from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route("/")
def index():
    # Create a list of 9 food items for sale
    food_items = [
        {"name": "Pizza", "description": "Delicious cheesy pizza", "price": "$10", "image": "https://via.placeholder.com/150?text=Pizza"},
        {"name": "Burger", "description": "Juicy beef burger", "price": "$8", "image": "https://via.placeholder.com/150?text=Burger"},
        {"name": "Ice Cream", "description": "Cool and tasty ice cream", "price": "$5", "image": "https://via.placeholder.com/150?text=Ice+Cream"},
        {"name": "Sandwich", "description": "Healthy and fresh sandwich", "price": "$7", "image": "https://via.placeholder.com/150?text=Sandwich"},
        {"name": "Salad", "description": "Fresh mixed salad", "price": "$6", "image": "https://via.placeholder.com/150?text=Salad"},
        {"name": "Sushi", "description": "Traditional Japanese sushi", "price": "$12", "image": "https://via.placeholder.com/150?text=Sushi"},
        {"name": "Pasta", "description": "Italian pasta with sauce", "price": "$9", "image": "https://via.placeholder.com/150?text=Pasta"},
        {"name": "Donut", "description": "Sweet and yummy donut", "price": "$3", "image": "https://via.placeholder.com/150?text=Donut"},
        {"name": "Taco", "description": "Spicy and flavorful taco", "price": "$4", "image": "https://via.placeholder.com/150?text=Taco"}
    ]
    # Render the 'index.html' template and pass the food items list to it.
    return render_template("index.html", food_items=food_items)

if __name__ == '__main__':
    app.run(debug=True)