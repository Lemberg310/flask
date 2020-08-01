from flask import Flask, render_template,  url_for
from random import randint

import os 

app = Flask(__name__)

site_name = "Minari" # Це імя буде виводитись


@app.route("/") # Adress
def main():
    return render_template('index.html', site = "Minari") # He must be in folder "templates"

@app.route("/about") # Adress
def about():
	return render_template('about.html', site = "About Minari", number = randint(0, 99999)) # Return text

@app.route("/member/<int:userid>") # Member/id/username
def member(userid, profile):
	return render_template('member.html', site = "Member", id = {userid}, name = {profile})

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values): # this help change css files
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@app.errorhandler(404)
def page_not_found(e):
    #snip
    return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True) # Run program whit debug mode (When debug=True)