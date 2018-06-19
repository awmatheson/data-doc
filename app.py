from flask import Flask

app = Flask(__name__)


# homepage
@app.route('/')
def index():
    # serve up the home page
    return render_template("index.html",para1=meter1, para2=meter2)

# DAG page
@app.route('/dag/<dag_id>', methods=['GET'])
def dag_page(dag_id):

		# parse code and print out the important parts
    return render_template("dag_template.html",para1=meter1, para2=meter2)

if __name__ == "__main__":
    app.run()