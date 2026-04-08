from flask import Flask, render_template

app = Flask(__name__)

CAKES = [
    {"name": "Classic Vanilla", "price": "$25", "desc": "Light and fluffy vanilla sponge with buttercream frosting"},
    {"name": "Chocolate Truffle", "price": "$30", "desc": "Rich dark chocolate layers with ganache filling"},
    {"name": "Red Velvet", "price": "$28", "desc": "Velvety cocoa cake with cream cheese frosting"},
    {"name": "Strawberry Delight", "price": "$27", "desc": "Fresh strawberry cake with whipped cream layers"},
    {"name": "Lemon Drizzle", "price": "$24", "desc": "Zesty lemon sponge with a sweet citrus glaze"},
    {"name": "Carrot Cake", "price": "$26", "desc": "Spiced carrot cake with walnuts and cream cheese"},
]

@app.route("/")
def home():
    return render_template("index.html", cakes=CAKES)

if __name__ == "__main__":
    app.run(debug=True)
