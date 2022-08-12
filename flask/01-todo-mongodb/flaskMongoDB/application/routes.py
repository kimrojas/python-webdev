from application import app
from application import db
from flask import render_template, redirect, flash, request
from .forms  import TodoForm
from datetime import datetime
import pytz

@app.route("/")
def get_todos():
    todos = []
    for todo in db.todo_flask.find().sort("date_created", -1):
        todo["_id"] = str(todo["_id"])
        todo["date_created"] = todo["date_created"].strftime("%b %d %Y %H:%M:%S")
        todos.append(todo)
    return render_template("view_todos.html", title="Layout Page", todos=todos)

@app.route("/add_todo", methods=["POST", "GET"])
def add_todo():
    if request.method == "POST":
        form = TodoForm(request.form)
        todo_name = form.name.data
        todo_description = form.description.data
        completed = form.completed.data
        
        db.todo_flask.insert_one({
            "name": todo_name,
            "description": todo_description,
            "completed": completed,
            "date_created": datetime.now()
        })
        
        flash("Todo successfully added", "success")
        return redirect("/")
        
    else:
        form = TodoForm()
    return render_template("add_todo.html", form=form)