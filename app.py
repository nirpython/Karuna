from flask import Flask, request

task = Flask(__name__)


@task.route('/')
def home():
    return "<b> Numel Solutions </b>"


if __name__ == "__name__":
    task.run()

task = Flask(__name__)


@task.route('/')
def add():
    return "<h2> Flask Framework</h2>"


if __name__ == "__name__":
    task.run()

task = Flask(__name__)


def fruits():
    return "<h1>Apple</h1>"

if __name__ == "__name__":
    task.run()
