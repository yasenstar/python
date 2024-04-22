from guizero import App, Drawing, TextBox, Combo, Slider

def draw_meme():
    meme.clear()
    meme.image(30,0,"woodpecker.png")
    meme.text(
        50,10, top_text.value,
        color=color.value,
        size=20,
        font="courier"
    )
    meme.text(
        250,220, bottom_text.value,
        color="blue",
        size=size.value,
        font=font.value
    )

app = App("meme")

top_text = TextBox(app, text="top text", width=50, command=draw_meme)
bottom_text = TextBox(app, text="bottom text", width=50, command=draw_meme)

color = Combo(
    app,
    options=["black", "white", "red", "green", "blue", "orange", "pink"],
    command=draw_meme,
    selected="blue"
)

font = Combo(
    app,
    options=["times new roman", "verdana", "courier", "impact"],
    command=draw_meme,
    selected="impact"
)

size = Slider(app, start=20, end=40, command=draw_meme)

meme = Drawing(app, width="fill", height="fill")

draw_meme()

app.display()