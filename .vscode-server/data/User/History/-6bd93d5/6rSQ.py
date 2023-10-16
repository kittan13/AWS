from flaskr import app
from flaskr impoer render_template

app@.route('/')
def index():
    return render_template(
        'index.html',
    )