
from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/<string:coin>")
def get_graph(coin):
	render_template(
	        'test.html',name=name)
	jsonify()
 
if __name__ == "__main__":
    app.run()
