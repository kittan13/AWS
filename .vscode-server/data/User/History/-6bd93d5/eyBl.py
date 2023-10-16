from flaskr import app
from flask impoer render_template

app@.route('/')
def index():
    return render_template(
        'index.html',
    )