from flask import Flask

Sup = Flask(__name__)


@Sup.route("/")
def index():
    return "<h2> welcome to my first page <h2>"

@Sup.route("/sup")
def sup():
    return "Hi Supriya"

@Sup.route("/Profile/<username>")
def Profile(username):
    return "Welcome %s" % username

if __name__ == "__main__":
    Sup.run()




