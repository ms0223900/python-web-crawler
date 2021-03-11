import os
from test_web_crawler import crawlWeb

URI = os.getenv('WEB_URI', 'http://yahoo.com')
# print(URI)

def get_web_titles(quriedHTML):
  if not URI:
    print('no uri :(')
    return None
  else:
    titles = quriedHTML.find_all(['h1', 'h2'])
    res = list(titles)
    print(res)
    return res

def main():
  queriedHTML = crawlWeb(URI)
  return get_web_titles(queriedHTML)

if __name__ == "__main__":
    main()