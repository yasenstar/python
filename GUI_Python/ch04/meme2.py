from guizero import App, Drawing, TextBox

def draw_meme():
    meme.clear()
    meme.image(30,0,"woodpecker.png")
    meme.text(50,20, top_text.value)
    meme.text(50,220, bottom_text.value)

app = App("meme")

top_text = TextBox(app, text="top text")
bottom_text = TextBox(app, text="bottom text")

meme = Drawing(app, width="fill", height="fill")

draw_meme()

app.display()