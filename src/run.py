from src.app import app

__author__ = 'sanny'

app.run(debug=app.config['DEBUG'], port=4990)