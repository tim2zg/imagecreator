from PIL import ImageFont, ImageDraw, Image
import requests
import random
import githubstreaker

colors = ["blue", "red", "green", "yellow", "orange", "purple", "pink", "white"]

fontpath = r'C:\Users\Tim\Downloads\Arial-Rounded-MT-Bold-Font\ARLRDBD.ttf'


def straktest():
    image = Image.open("mini.png")
    data = githubstreaker.getthedata()["currentstreak"]
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontpath, 38)
    font2 = ImageFont.truetype(fontpath, 33)
    font3 = ImageFont.truetype(fontpath, 10)

    draw.text((165, 100), "Streak: ", font=font, align="center", fill=(255, 255, 255))

    #draw.text((220, 150), "1", font=font2, align="center", fill=(255, 255, 255))
    draw.text((209.25, 150), str(data["lenth"]), font=font2, align="center", fill=(255, 255, 255))

    draw.text((177.5, 200), "Days!", font=font, align="center", fill=(255, 255, 255))

    if data["lenth"] == 0:
        draw.text((155, 270), "From: " + "Today" + " To: " + "Today", font=font3, align="center", fill=(255, 255, 255))
    else:
        draw.text((155, 270), "From: " + data["start"] + " To: " + data["end"], font=font3, align="center", fill=(255, 255, 255))


    for i in range(data["lenth"]):
        if i >= 6 and i <= 11:
            i = i - 6
            draw.ellipse((60 + 40, 60 + i * 40, 90 + 40, 90 + i * 40), fill='white', outline='white')
        if i >= 12 and i <= 17:
            i = i - 12
            draw.ellipse((340, 60 + i * 40, 370, 90 + i * 40), fill='white', outline='white')
        if i >= 18 and i <= 23:
            i = i - 18
            draw.ellipse((380, 60 + i * 40, 410, 90 + i * 40), fill='white', outline='white')
        if i >= 0 and i <= 5:
            draw.ellipse((60, 60 + i * 40, 90, 90 + i * 40), fill='white', outline='white')

    image.save("current-streak.png")


def straktestlongest():
    image = Image.open("mini.png")
    data = githubstreaker.getthedata()["longeststreak"]
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontpath, 30)
    font2 = ImageFont.truetype(fontpath, 33)
    font3 = ImageFont.truetype(fontpath, 10)

    draw.text((145, 100), "Streak MAX:", font=font, align="center", fill=(255, 255, 255))

    #draw.text((220, 150), "1", font=font2, align="center", fill=(255, 255, 255))
    draw.text((209.25, 150), str(data["lenth"]), font=font2, align="center", fill=(255, 255, 255))

    draw.text((187.5, 200), "Days!", font=font, align="center", fill=(255, 255, 255))

    draw.text((155, 270), "From: " + data["start"] + " To: " + data["end"], font=font3, align="center", fill=(255, 255, 255))


    for i in range(data["lenth"]):
        if i >= 6 and i <= 11:
            i = i - 6
            draw.ellipse((60 + 40, 60 + i * 40, 90 + 40, 90 + i * 40), fill='white', outline='white')
        if i >= 12 and i <= 17:
            i = i - 12
            draw.ellipse((340, 60 + i * 40, 370, 90 + i * 40), fill='white', outline='white')
        if i >= 18 and i <= 23:
            i = i - 18
            draw.ellipse((380, 60 + i * 40, 410, 90 + i * 40), fill='white', outline='white')
        if i >= 0 and i <= 5:
            draw.ellipse((60, 60 + i * 40, 90, 90 + i * 40), fill='white', outline='white')

    image.save("streaklong.png")


def allcontributes():
    image = Image.open("mini.png")
    data = githubstreaker.getthedata()["totalcontributes"]
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontpath, 35)
    font2 = ImageFont.truetype(fontpath, 38)

    draw.text((145, 120), "All commits:", font=font, align="center", fill=(255, 255, 255))
    draw.text((209.25, 170), str(data), font=font2, align="center", fill=(255, 255, 255))

    image.save("contributes.png")


def userrepos():
    data = requests.get("https://api.github.com/users/tim2zg")
    data = data.json()
    image = Image.open("mini.png")

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontpath, 38)
    font2 = ImageFont.truetype(fontpath, 33)

    draw.text((55, 100), "You can access my", font=font, align="center", fill=(255, 255, 255))
    draw.text((209.25, 150), str(data["public_repos"]), font=font2, align="center", fill=(255, 255, 255))
    draw.text((177.5, 200), "Repos!", font=font, align="center", fill=(255, 255, 255))

    image.save("userrepos.png")


def myfollowers():
    data = requests.get("https://api.github.com/users/tim2zg")
    data = data.json()
    image = Image.open("mini.png")

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontpath, 38)
    font2 = ImageFont.truetype(fontpath, 33)

    draw.text((160, 100), "I have", font=font, align="center", fill=(255, 255, 255))
    draw.text((209.25, 150), str(data["followers"]), font=font2, align="center", fill=(255, 255, 255))
    draw.text((140, 200), "followers!", font=font, align="center", fill=(255, 255, 255))

    image.save("followers.png")


def getmainpage():
    image = Image.open("a.png")

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontpath, 50)

    draw.text((337, 358), "I am Tim, 15 year old junior Dev from Switzerland! ", font=font, align="center", fill=(255, 255, 255))
    draw.text((335.5, 418), "I am excited to learn a lot of new things about", font=font, align="center", fill=(255, 255, 255))
    draw.text((335.5, 478), "IT technologies and happy to exchange my ", font=font, align="center", fill=(255, 255, 255))
    draw.text((335.5, 538), "learnings with other nerds!", font=font, align="center", fill=(255, 255, 255))
    draw.text((340.5, 608), "You can DM me if you want to talk about IT", font=font, align="center", fill=(255, 255, 255))
    draw.text((340.5, 668), "and other stuff:), would be a pleasure 4 me!", font=font, align="center", fill=(255, 255, 255))
    draw.text((340.5, 738), "Feel free to use my code and projects", font=font, align="center", fill=(255, 255, 255))
    draw.text((340.5, 788), "if you can use it!", font=font, align="center", fill=(255, 255, 255))
    draw.text((340.5, 848), "Looking forward to exchange tech and", font=font, align="center", fill=(255, 255, 255))
    draw.text((340.5, 908), "it stuff with you ;)", font=font, align="center", fill=(255, 255, 255))

    draw.line((845, 1050, 1045, 1050), fill=random.choice(colors), width=60)

    count = random.randint(1, 5)

    usecolors = {}

    for i in range(count):
        usecolors[i] = random.choice(colors)

    for i in range(count):
        draw.ellipse((765 - 80 * i, 1020, 825 - 80 * i, 1080), fill=usecolors[i], outline='black')

    for i in range(count):
        draw.ellipse((1065 + 80 * i, 1020, 1125 + 80 * i, 1080), fill=usecolors[i], outline='black')

    image.save("main.png")


def insta():
    image = Image.open("insta.png")

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontpath, 50)

    draw.text((180, 20), "tim2zg", font=font, align="center", fill=(255, 255, 255))

    #draw.text((220, 20), "10", font=font, align="center", fill=(255, 255, 255))

    image.save("insta_mini.png")


def github():
    image = Image.open("github.png")

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontpath, 50)

    draw.text((180, 20), "tim2zg", font=font, align="center", fill=(255, 255, 255))

    #draw.text((220, 20), "10", font=font, align="center", fill=(255, 255, 255))

    image.save("github_mini.png")


def reedit():
    image = Image.open("reedit.png")

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontpath, 50)

    draw.text((180, 20), "tim2zg", font=font, align="center", fill=(255, 255, 255))

    #draw.text((220, 20), "10", font=font, align="center", fill=(255, 255, 255))

    image.save("reedit_mini.png")


def twitter():
    image = Image.open("twitter.png")

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontpath, 50)

    draw.text((180, 20), "tim2zg", font=font, align="center", fill=(255, 255, 255))

    #draw.text((220, 20), "10", font=font, align="center", fill=(255, 255, 255))

    image.save("twitter_mini.png")


def unsplash():
    image = Image.open("unsplash.png")

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontpath, 50)

    draw.text((180, 20), "tim2zg", font=font, align="center", fill=(255, 255, 255))

    #draw.text((220, 20), "10", font=font, align="center", fill=(255, 255, 255))

    image.save("unsplash_mini.png")


def discord():
    image = Image.open("discord.png")

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fontpath, 35)

    draw.text((150, 30), "tim2zg#7743", font=font, align="center", fill=(255, 255, 255))

    #draw.text((220, 20), "10", font=font, align="center", fill=(255, 255, 255))

    image.save("discord_mini.png")


if __name__ == '__main__':
    getmainpage()  # In the future, this will be a flask server
