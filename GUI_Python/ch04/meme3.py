from guizero import App, Drawing, TextBox

def draw_meme():
    meme.clear()
    meme.image(30,0,"woodpecker.png")
    meme.text(
        50,10, top_text.value,
        color="orange",
        size=20,
        font="courier"
    )
    meme.text(
        250,220, bottom_text.value,
        color="blue",
        size=28,
        font="times new roman"
    )

app = App("meme")

top_text = TextBox(app, text="top text", command=draw_meme)
bottom_text = TextBox(app, text="bottom text", command=draw_meme)

meme = Drawing(app, width="fill", height="fill")

draw_meme()

app.display()