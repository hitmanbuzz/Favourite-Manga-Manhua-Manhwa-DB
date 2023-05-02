import json
import jmespath
import os

with open("manhua_database.json", "r+") as db:
    db_r = db.read()
    data = json.loads(db_r)
    title = input("Search Manhua Title: ").replace(" ", "_")
    search_title = jmespath.search(f"manhua[*].{title}", data)
    search_url = jmespath.search(f"manhua[*].{title}.url", data)
    search_chapter = jmespath.search(f"manhua[*].{title}.chapter", data)
    search_option = jmespath.search(f"manhua[*].{title}.option", data)
    os.system("cls")
    print(f'''TITLE: {title}
URL: {search_url}
CHAPTER: {search_chapter}
OPTION: {search_option}
    ''')
