from flask import Flask, render_template, send_from_directory, request, redirect, url_for
from backend import *
import json
import os

app = Flask(__name__)
customer_queue = CustomerQueue()
tree_manager = BinaryTreeManager()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/works')
def works():
    data_file = os.path.join(app.root_path, 'data', 'projects.json')
    works = []
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            works = json.load(f)
    except Exception:
        works = []
    return render_template('works.html', works = works)

@app.route('/queue')
@app.route('/queue', methods=["GET", "POST"])
def queue_page():
    if request.method == "POST":
        if "add_customer" in request.form:
            name = request.form["name"]
            state = request.form["state"]
            customer_queue.add_customer(name, state)
        elif "serve_customer" in request.form:
            customer_queue.serve_customer()
        return redirect(url_for("queue_page"))
    
    return render_template("queue.html", line=customer_queue.get_line())

@app.route("/contact")
def contacts_page():
    data_file = os.path.join(app.root_path, 'data', 'team.json')
    contacts = []
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            contacts = json.load(f)
    except Exception as e:
        print(f"Error loading contacts: {e}")
        contacts = []
    return render_template('contact.html', contacts=contacts)

@app.route("/tree", methods=["GET", "POST"])
def tree_page():
    message = None 

    if request.method == "POST":
        parent_value = request.form.get("parent")  # can be empty for root
        side = request.form.get("side")
        new_value = request.form.get("value")
        message = tree_manager.add_node(parent_value, side, new_value)

    tree_dict = tree_manager.get_tree_dict()
    return render_template("tree.html", tree=tree_dict, message=message)

if __name__ == '__main__':
    app.run(debug=True)