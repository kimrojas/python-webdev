from flask import Flask
from flask_pymongo import PyMongo

import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] 

app = Flask(__name__)
app.config["SECRET_KEY"] = 'e5dff1c481632e45eab9354a6a161c356373f27e'
app.config["MONGO_URI"] = "mongodb+srv://admin:pass1234@cluster0.wbgv4ax.mongodb.net/?retryWrites=true&w=majority"

# Setup MongoDB
mongodb_client = PyMongo(app)
db = mongodb_client.db

from application import routes


