from guizero import App, Text, Picture

# Create GUI App
app = App("Wanted!")

# Background colours
app.bg = (251,251,208)

# Add some text
wanted_text = Text(app, "WANTED")

# Change text size, colour and font
wanted_text.text_size = 50
wanted_text.text_color = "blue"
wanted_text.font="Comic Sans MS"

# Add picture
cat = Picture(app, image="my_cat.png")

app.display()