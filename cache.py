from flask import Flask,request
from flask_caching import Cache
import datetime

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
}

app = Flask(__name__)
# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)

@app.route('/')
@cache.cached(timeout=10)
def index():
    return f'''<html><body>Cached at {str(datetime.datetime.now())}, hello from  {request.headers.get('Referer')}</body></html>'''


if __name__ == '__main__':
    app.run(debug=True)

