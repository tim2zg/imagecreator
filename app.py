from flask import Flask, send_file
import datetime
import main

app = Flask(__name__)

strakdate = datetime.datetime(1969, 6, 9)
strakdatelong = datetime.datetime(1969, 6, 9)
contributionsdate = datetime.datetime(1969, 6, 9)
userreposdate = datetime.datetime(1969, 6, 9)
followersdate = datetime.datetime(1969, 6, 9)
maindate = datetime.datetime(1969, 6, 9)
isntadate = datetime.datetime(1969, 6, 9)
githubdate = datetime.datetime(1969, 6, 9)
redditdate = datetime.datetime(1969, 6, 9)
twitterdate = datetime.datetime(1969, 6, 9)
unsplashdate = datetime.datetime(1969, 6, 9)
discorddate = datetime.datetime(1969, 6, 9)


@app.route('/streak', methods=['GET'])
def streak():
    global strakdate
    now = datetime.datetime.now()
    if (now - strakdate) > datetime.timedelta(hours=1):
        main.straktest()
        strakdate = now

    return send_file("current-streak.png", mimetype='image/png')


@app.route('/streaklong', methods=['GET'])
def streaklong():
    global strakdatelong
    now = datetime.datetime.now()
    if (now - strakdatelong) > datetime.timedelta(hours=1):
        main.straktestlongest()
        strakdatelong = now
    return send_file("streaklong.png", mimetype='image/png')


@app.route('/contributes', methods=['GET'])
def contributes():
    global contributionsdate
    now = datetime.datetime.now()
    if (now - contributionsdate) > datetime.timedelta(hours=1):
        main.allcontributes()
        contributionsdate = now
    return send_file("contributes.png", mimetype='image/png')


@app.route('/userrepos', methods=['GET'])
def userrepos():
    global userreposdate
    now = datetime.datetime.now()
    if (now - userreposdate) > datetime.timedelta(hours=1):
        main.userrepos()
        userreposdate = now
    return send_file("userrepos.png", mimetype='image/png')


@app.route('/followers', methods=['GET'])
def followers():
    global followersdate
    now = datetime.datetime.now()
    if (now - followersdate) > datetime.timedelta(hours=1):
        main.myfollowers()
        followersdate = now
    return send_file("followers.png", mimetype='image/png')


@app.route('/main', methods=['GET'])
def mainasdf():
    global maindate
    now = datetime.datetime.now()
    if (now - maindate) > datetime.timedelta(hours=1):
        main.getmainpage()
        maindate = now
    return send_file("main.png", mimetype='image/png')


@app.route('/insta', methods=['GET'])
def isnta():
    global isntadate
    now = datetime.datetime.now()
    if (now - isntadate) > datetime.timedelta(hours=1):
        main.insta()
        isntadate = now
    return send_file("insta_mini.png", mimetype='image/png')


@app.route('/github', methods=['GET'])
def github():
    global githubdate
    now = datetime.datetime.now()
    if (now - githubdate) > datetime.timedelta(hours=1):
        main.github()
        githubdate = now
    return send_file("github_mini.png", mimetype='image/png')


@app.route('/reddit', methods=['GET'])
def reddit():
    global redditdate
    now = datetime.datetime.now()
    if (now - redditdate) > datetime.timedelta(hours=1):
        main.reedit()
        redditdate = now
    return send_file("reedit_mini.png", mimetype='image/png')


@app.route('/twitter', methods=['GET'])
def twitter():
    global twitterdate
    now = datetime.datetime.now()
    if (now - twitterdate) > datetime.timedelta(hours=1):
        main.twitter()
        twitterdate = now
    return send_file("twitter_mini.png", mimetype='image/png')


@app.route('/unsplash', methods=['GET'])
def unsplash():
    global unsplashdate
    now = datetime.datetime.now()
    if (now - unsplashdate) > datetime.timedelta(hours=1):
        main.unsplash()
        unsplashdate = now
    return send_file("unsplash_mini.png", mimetype='image/png')


@app.route('/discord', methods=['GET'])
def discord():
    global discorddate
    now = datetime.datetime.now()
    if (now - discorddate) > datetime.timedelta(hours=1):
        main.discord()
        discorddate = now
    return send_file("discord_mini.png", mimetype='image/png')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)