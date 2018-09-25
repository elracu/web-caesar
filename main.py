from flask import Flask, request
from caesar import encrypt 

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form method="post">
        <label> Rotated by:
            <input type="text" name="rot" value="0"/>
        </label>
        <textarea type="text" name="text"/></textarea>
        <input type="submit"/>
      
      </form>
    </body>
</html>


"""


@app.route("/")
def index():

    return form

@app.route("/", methods=['POST'])
def encrypted():
    #values from form
    rotate_by = request.form['rot']
    phrase = request.form['text']
    rotate_by_number = int(rotate_by)

    return '<h1>' + encrypt(phrase, rotate_by_number) + '</h1>'

app.run()