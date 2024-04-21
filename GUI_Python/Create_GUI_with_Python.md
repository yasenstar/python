 Create GUI with Python
(guizero library)

Get free PDF: https://magpi.raspberrypi.com/books/create-guis/pdf/download


# CH01 Introduction to GUIs

## Installing guizero

### pip3 install guizero

### from guizero import App

## Run "Hello World" in GUI

### app = App("Hello World")

## Adding widgets

### from guizero import App, Text

### Text(app, text="string")

# CH02 Wanted Poster

## Add text in different fonts, sizes and colors

### Text.text_size = size_in_integer

### Text.font="font_name"

## Change background color

### app.bg="color-name or color-code"

#### app.bg="yellow"

#### app.bg="#FBFBD0"

#### app.bg=(251,251,208)

### htmlcolorcodes.com

## Add pictures

### from guizero import App, Text, Picture

### Picture(app, image="pic_name")

### Get free pictures from PIXABAY

# CH03 Spy Name Chooser

# CH04 Meme Generator

# CH05 World's Worst GUI

# CH06 Tic-Tac-Toe

# CH07 Destroy the Dots

# CH08 Flood It

# CH09 Emoji Match

# CH10 Paint

# CH11 Stop-Frame Animation

# Appendix A: Setting Up

# Appendix B: Getting Started with Python

# Appendix C: Widgets in guizero
