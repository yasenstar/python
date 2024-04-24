from guizero import App, PushButton

app = App("test")
button = PushButton(app, text=u'\u1285')

app.display()