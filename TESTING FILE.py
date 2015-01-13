import Image

background = Image.open("teen.jpg")
foreground = Image.open("powercat.png")

background.paste(foreground, (0, 0), foreground)
background.show()