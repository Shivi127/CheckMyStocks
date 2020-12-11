from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def home():
    stock_name = 'oracle'
    icon_url = f"https://icons8.com/icons/set/{stock_name}"
    print(icon_url)
    return render_template('index.html', stock_icon=icon_url)
# app = Flask(__name__)
# api = Api(app)

# students={
#     '1': {'name:':'Shivi','age':23,'spec':'math'},
#     '2': {'name:':'Vishal','age':25,'spec':'cs'},
# }

# parser = reqparse.RequestParser()

# 

if __name__ == "__main__":
    app.run(debug=True)