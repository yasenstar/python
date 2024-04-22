from guizero import App, Drawing, TextBox

app = App("meme")

top_text = TextBox(app, text="top text")
bottom_text = TextBox(app, text="bottom text")

app.display()