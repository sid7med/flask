from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "<h1>Welcome to My Flask App!</h1><p>Explore the API by visiting /api or the interactive page at /about.</p>"

# About page (HTML template rendering)
@app.route('/about')
def about():
    return """
    <html>
        <head>
            <title>About My Flask App</title>
        </head>
        <body>
            <h1>About</h1>
            <p>This is a demo Flask application with multiple routes and interactive APIs.</p>
            <p>Try visiting: <a href="/api/data">/api/data</a> or POST data to <a href="/api/echo">/api/echo</a>.</p>
        </body>
    </html>
    """

# Static JSON data route
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "status": "success",
        "data": {
            "id": 1,
            "name": "Flask Demo",
            "version": "1.0.0"
        }
    }
    return jsonify(data)

# Echo API (POST route)
@app.route('/api/echo', methods=['POST'])
def echo_data():
    input_data = request.json
    if not input_data:
        return jsonify({"error": "No JSON data provided!"}), 400
    return jsonify({"status": "success", "received": input_data})

# Dynamic route with a parameter
@app.route('/api/greet/<name>')
def greet_user(name):
    return jsonify({"message": f"Hello, {name}! Welcome to the Flask App!"})

# Error handling for unknown routes
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Route not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
