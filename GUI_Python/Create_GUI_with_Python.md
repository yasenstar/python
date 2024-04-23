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

## Add a button

### button=PushButton()

## Create a function

### def functionName():

### Transfer argument to function: use "command=lambda:function(arg1,arg2...)"

## Add some names

### random, choice

## Put the name in the GUI

# CH04 Meme Generator

## Create a meme as Drawing

### Drawing

### TextBox

## Customize your meme generator

### Combo

### Slider

# CH05 World's Worst GUI

## It's Hard to Read

## The Wrong Widget

## Pop-ups

# CH06 Tic-Tac-Toe

## 1. Create the board

### tictactoe1.py

### Using Box for Board container

### Using PushButton inside the Board

### FOR loop to create 3x3 board

## 2. Underlying data structure

### tictactoe2.py

## 3. Make the buttons work

### tictactoe3.py

### Using Text for Message about Turn

## 4. Alternating between players

### tictactoe4.py

## 5. Do we have a winner?

### tictactoe5.py

## 6. Reset the game

## 7. Draw game

### tictactoe6.py

# CH07 Destroy the Dots

# CH08 Flood It

# CH09 Emoji Match

# CH10 Paint

# CH11 Stop-Frame Animation

# Appendix A: Setting Up

# Appendix B: Getting Started with Python

# Appendix C: Widgets in guizero

# guizero core

## Commands (Function)
 (see:Create a function)
## Multiple windows

## Layouts

## Pop-ups

## Sizes

## Colors
 (see:Change background color)
## Images

## Loops and sleeping
 (see:FOR loop to create 3x3 board)
## Events

## Using tkinter

# guizero Widgets

## App
 (see:app = App("Hello World")Pop-ups)
## Box
 (see:Using Box for Board container)
## ButtonGroup
 (see:Using PushButton inside the Board)
## CheckBox

## Combo
 (see:ComboThe Wrong Widget)
## Drawing
 (see:Create a meme as Drawing)
## ListBox

## Picture
 (see:Add pictures)
## PushButton
 (see:Add a button)
## Slider
 (see:Slider)
## Text
 (see:Text(app, text="string")Add text in different fonts, sizes and colorsIt's Hard to ReadUsing Text for Message about Turn)
## TextBox
 (see:TextBox)
## TitleBox

## Waffle

## Window
