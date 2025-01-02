from flask import Flask, request
import random
import string

app = Flask(__name__)

def generate_password(length, include_uppercase, include_numbers, include_symbols):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def index():
    password = None
    if request.method == "POST":
        length = int(request.form.get("length", 12))  # Default to 12 if not provided
        include_uppercase = "uppercase" in request.form
        include_numbers = "numbers" in request.form
        include_symbols = "symbols" in request.form

        password = generate_password(length, include_uppercase, include_numbers, include_symbols)

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Password Generator</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }}
            form {{
                margin-bottom: 20px;
            }}
            input, label {{
                margin: 5px;
            }}
            .password {{
                font-size: 1.2em;
                color: #007BFF;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <h1>Password Generator</h1>
        <form method="POST">
            <label for="length">Password Length:</label>
            <input type="number" id="length" name="length" value="12" min="4" max="64" required><br>
            <label><input type="checkbox" name="uppercase"> Include Uppercase</label><br>
            <label><input type="checkbox" name="numbers"> Include Numbers</label><br>
            <label><input type="checkbox" name="symbols"> Include Symbols</label><br>
            <button type="submit">Generate Password</button>
        </form>
        {"<div class='password'><strong>Generated Password:</strong> " + password + "</div>" if password else ""}
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)
