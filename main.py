from PIL import ImageFont, ImageDraw, Image
import requests
import random

colors = ["blue", "red", "green", "yellow", "orange", "purple", "pink", "white"]


def straktest():
    image = Image.open("mini.png")

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(r'C:\Users\Tim\Downloads\Arial-Rounded-MT-Bold-Font\ARLRDBD.ttf', 38)
    font2 = ImageFont.truetype(r'C:\Users\Tim\Downloads\Arial-Rounded-MT-Bold-Font\ARLRDBD.ttf', 33)

    draw.text((165, 100), "Streak:", font=font, align="center", fill=(255, 255, 255))

    draw.text((220, 150), "1", font=font2, align="center", fill=(255, 255, 255))
    #draw.text((209.25, 150), "10", font=font2, align="center", fill=(255, 255, 255))

    draw.text((177.5, 200), "Days!", font=font, align="center", fill=(255, 255, 255))


    for i in range(18):
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

    image.save("mini_with_text.png")


def userrepos():
    data = requests.get("https://api.github.com/users/tim2zg")
    data = data.json()
    image = Image.open("mini.png")

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(r'C:\Users\Tim\Downloads\Arial-Rounded-MT-Bold-Font\ARLRDBD.ttf', 38)
    font2 = ImageFont.truetype(r'C:\Users\Tim\Downloads\Arial-Rounded-MT-Bold-Font\ARLRDBD.ttf', 33)

    draw.text((55, 100), "You can access my", font=font, align="center", fill=(255, 255, 255))
    draw.text((209.25, 150), str(data["public_repos"]), font=font2, align="center", fill=(255, 255, 255))
    draw.text((177.5, 200), "Repos!", font=font, align="center", fill=(255, 255, 255))

    image.save("mini_with_text_tow.png")


def myfollowers():
    data = requests.get("https://api.github.com/users/tim2zg")
    data = data.json()
    image = Image.open("mini.png")

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(r'C:\Users\Tim\Downloads\Arial-Rounded-MT-Bold-Font\ARLRDBD.ttf', 38)
    font2 = ImageFont.truetype(r'C:\Users\Tim\Downloads\Arial-Rounded-MT-Bold-Font\ARLRDBD.ttf', 33)

    draw.text((160, 100), "I have", font=font, align="center", fill=(255, 255, 255))
    draw.text((209.25, 150), str(data["followers"]), font=font2, align="center", fill=(255, 255, 255))
    draw.text((140, 200), "followers!", font=font, align="center", fill=(255, 255, 255))

    image.save("mini_with_text_three.png")


def getmainpage():
    image = Image.open("a.png")

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(r'C:\Users\Tim\Downloads\Arial-Rounded-MT-Bold-Font\ARLRDBD.ttf', 50)

    draw.text((337, 358), "I'm Tim 15 Year old Hobby Dev from Switzerland! ", font=font, align="center", fill=(255, 255, 255))
    draw.text((335.5, 458.56), "I'm not very experienced, but I love to learn new things!", font=font, align="center", fill=(255, 255, 255))
    draw.text((340.5, 574.47), "You can DM me if you want to talk about IT", font=font, align="center", fill=(255, 255, 255))
    draw.text((340.5, 634.47), "and other Stuff:) would be a pleasure 4 me!", font=font, align="center", fill=(255, 255, 255))
    draw.text((340.5, 754.47), "Feel free to use my code and projects if they work!", font=font, align="center", fill=(255, 255, 255))
    draw.text((340.5, 814.47), "I love tech and the nerd stuff ;)", font=font, align="center", fill=(255, 255, 255))

    draw.line((845, 1050, 1045, 1050), fill=random.choice(colors), width=60)

    count = random.randint(1, 5)

    usecolors = {}

    for i in range(count):
        usecolors[i] = random.choice(colors)

    for i in range(count):
        draw.ellipse((765 - 80 * i, 1020, 825 - 80 * i, 1080), fill=usecolors[i], outline='black')

    for i in range(count):
        draw.ellipse((1065 + 80 * i, 1020, 1125 + 80 * i, 1080), fill=usecolors[i], outline='black')

    image.save("a_mini.png")


def insta():
    image = Image.open("insta.png")

    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(r'C:\Users\Tim\Downloads\Arial-Rounded-MT-Bold-Font\ARLRDBD.ttf', 50)

    #draw.text((180, 20), "tim2zg", font=font, align="center", fill=(255, 255, 255))

    draw.text((220, 20), "10", font=font, align="center", fill=(255, 255, 255))

    image.save("insta_mini.png")


if __name__ == '__main__':
    insta()