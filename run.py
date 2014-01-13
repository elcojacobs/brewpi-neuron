__author__ = 'Elco'

from eve import Eve
from flask.ext.bootstrap import Bootstrap
from eve_docs import eve_docs

app = Eve()
Bootstrap(app)
app.register_blueprint(eve_docs, url_prefix='/docs')
app.run()