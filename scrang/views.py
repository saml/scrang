from flask import Blueprint, request, render_template, abort

from . import articles

bp = Blueprint('default', __name__)

@bp.route('/')
def homepage():
    url = request.args.get('url')
    if not url:
        return render_template('error.html', msg='Need ?url= parameter'), 400
    a = articles.download(url)
    return render_template('homepage.html', url=url, html=a.article_html)


