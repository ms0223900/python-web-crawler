import json
import os
import flask
from flask import jsonify
from test_web_crawler import crawlWeb

app = flask.Flask(__name__)
app.config['DEBUG'] = True

URI = os.getenv('WEB_URI', 'http://yahoo.com')
# print(URI)

def get_web_titles(quriedHTML):
  if not URI:
    print('no uri :(')
    return None
  else:
    res = []
    titles = quriedHTML.find_all(['h1', 'h2', 'h3', 'article'])
    for title in titles:
      res.append(title.text)
    print(list(titles))
    return json.dumps(res)

@app.route('/', methods=['GET'])
def main():
  queriedHTML = crawlWeb(URI)
  return get_web_titles(queriedHTML)

if __name__ == "__main__":
    # main()
    app.run(
      host='0.0.0.0'
    )