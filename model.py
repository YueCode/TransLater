from flask import Flask, jsonify, render_template, request, Blueprint
# app=Flask(__name__)
# from flask_markdown import Markdown
# Markdown(app)

from flaskext.markdown import Markdown
import markdown
from utils import transMD,transE2C,download

def markdown2html(text):
    return markdown.markdown(text, ['extra'])
app=Flask(__name__)
Markdown(app)

# main_blueprint = Blueprint('main', __name__, template_folder='templates')
@app.route('/')
@app.route('/hello')
def test_1():
    mkd = '''
    # header
    ## header2
    [picture](http://www.example.com)
    * 1
    * 2
    * 3
    **bold**
    '''
    # mkd=markdown2html(mkd)


    return render_template('test1.html', mkd=mkd)
@app.route('/Transmd')
def trans2MD():
    Weburl=request.args.get('Weburl',0,type=str)
    md=transMD(Weburl)
    cmd=transE2C(md)
    return jsonify(mdstr=cmd)
if __name__ == '__main__':
    app.run()