from flask import Flask, request, jsonify
import string,random

#  WHOLE API THING:
app = Flask(__name__)
Running = True
exiting = False
store = {}

# Generate a random code
def generate_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

code = generate_code()
# /generate
@app.route('/generate', methods=['GET'])
def generate():
    global code
    store['code'] = code
    return jsonify({'code': code})


def run():
    
    app.run(debug=False)
