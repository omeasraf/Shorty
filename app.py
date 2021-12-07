from flask import Flask, request, render_template, redirect
import string, random, re
from database import Database


db = Database("urls.db")
db.createDB()

app = Flask(__name__)

LETTERS = string.ascii_lowercase + string.digits


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/link/<id>")
def redir(id:str):
    data = db.find(id, id=True)
    if data:
        return redirect(data.url)
    else:
        return redirect("https://omeasraf.com")


@app.route('/api/generate',methods = ['POST'])
def generate_url():
    if request.method == 'POST':
        url = request.form['url']
        if url and checkURL(url):
            check = db.find(url)
            if check:
                return check.toString()
            else:
                id = "".join(random.choice(LETTERS) for i in range(10))
                db.create(url, id)
                return db.find(url).toString()
    return ""

@app.route("/test")
def test():
    return True

def checkURL(url):
    regex = r"^((([A-Za-z]{3,9}:(?:\/\/)?)(?:[-;:&=\+\$,\w]+@)?[A-Za-z0-9.-]+(:[0-9]+)?|(?:www.|[-;:&=\+\$,\w]+@)[A-Za-z0-9.-]+)((?:\/[\+~%\/.\w\-_]*)?\??(?:[-\+=&;%@.\w_]*)#?(?:[\w]*))?)"
    return re.match(regex, url)