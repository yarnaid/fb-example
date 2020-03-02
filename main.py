from flask import Flask, redirect, url_for, render_template, flash
from fb import OAuthSignIn


app = Flask(__name__)
app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': '269045408249',
        'secret': '408d2b6e4560d14c205db123125edd'
    },
}

@app.route("/authorize")
def oauth_authorize():
    oauth = OAuthSignIn.get_provider("facebook")
    return oauth.authorize()


@app.route("/callback")
def oauth_callback():
    oauth = OAuthSignIn.get_provider("facebook")
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash("Authentication failed.")
        return redirect(url_for("index"))
    return redirect(url_for("index"))


@app.route("/")
def index():
    return "ok"


if __name__ == "__main__":
    app.run(debug=True)
