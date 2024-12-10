 Manim

# Manim Installation

## Windows OS

### Chocolatey

#### choco install manimce

##### get choco via powershell

#### choco install manim-latex

##### Error Message

Failures

 - manim-latex (exited 1) - manim-latex not installed. An error occurred during installation:

 Unable to obtain lock file access on 'C:\ProgramData\chocolatey\lib\882c7ec97e70db2a7b0eb9aa773bfab65350d8a6' for operations on 'C:\ProgramData\chocolatey\lib\manim-latex'. This may mean that a different user or administrator is holding this lock and that this process does not have permission to access it. If no other process is currently performing an operation on this file it may mean that an earlier NuGet process crashed and left an inaccessible lock file, in this case removing the file 'C:\ProgramData\chocolatey\lib\882c7ec97e70db2a7b0eb9aa773bfab65350d8a6' will allow NuGet to continue. 


##### https://github.com/rstudio/tinytex-releases/releases/download/v2024.11/TinyTeX-1-v2024.11.zip

#### Use scoop for installing tinytex

##### install scoop: powershell in Windows

###### Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

##### scoop bucket add r-bucket https://github.com/cderv/r-bucket.git

##### scoop install tinytex

error:

Installing 'tinytex' (2024.11) [64bit] from 'r-bucket' bucket

TinyTeX-1-v2024.11.zip (109.7 MB) [=======================================================>                   ]  75%

The operation has timed out.

URL https://github.com/yihui/tinytex-releases/releases/download/v2024.11/TinyTeX-1-v2024.11.zip is not valid


#### Use choco to install miktex

##### In Windows, open CMD with administrative permission

##### run: choco install miktex.install

PS C:\Users\v0cn037> choco install miktex.install

Chocolatey v2.4.0

Installing the following packages:

miktex.install

By installing, you accept licenses for the packages.

Downloading package from source 'https://community.chocolatey.org/api/v2/'



miktex.install v24.4.0 [Approved]

miktex.install package files install completed. Performing other installation steps.

The package miktex.install wants to run 'chocolateyinstall.ps1'.

Note: If you don't run this script, the installation will fail.

Note: To confirm automatically next time, use '-y' or consider:

choco feature enable -n allowGlobalConfirmation

Do you want to run the script?([Y]es/[A]ll - yes to all/[N]o/[P]rint): Y



Extracting 64-bit C:\ProgramData\chocolatey\lib\miktex.install\tools\miktexsetup-5.5.0+1763023-x64.zip to C:\ProgramData\chocolatey\lib\miktex.install\tools...

Downloading a "Basic" package set to install.

WARNING: No registry key found based on  'miktex*'

Creating a temporary repository at 'C:\Users\v0cn037\AppData\Local\Temp\chocolatey\MiKTeX-repository'.

Installing from temporary MiKTeX repository for all users.

  miktex.install may be able to be automatically uninstalled.

Environment Vars (like PATH) have changed. Close/reopen your shell to

 see the changes (or in powershell/cmd.exe just type `refreshenv`).

 The install of miktex.install was successful.

  Deployed to 'C:\Program Files\MiKTeX'



Chocolatey installed 1/1 packages.

 See the log for details (C:\ProgramData\chocolatey\logs\chocolatey.log).


## lecture 001

# Tutorials & Guides

## 1. Tutorials

### 1. Quickstart

#### New Project, Animating a Circle

##### lecture 002

##### manim -pql .\scene.py CreateCircle

##### If the PATH is not effective

###### You can use full path of manim.exe to execute

###### You can restart VS Code then the PATH will be working

#### Transforming a Square into a Circle

##### lecture 003

#### Positioning MobjectS

##### lecture 004

#### Using .animate syntax to animate methods

##### lecture 005

#### Transform vs. ReplacementTransform

##### Transform(mob1, mob2)

###### transforms the points (as well as other attributes like color) of mob1 into the points/attributes of mob2

###### In some cases it's more beneficial to use Transform, like when you are transforming several mobjects one after the other.

##### ReplacementTransform(mob1, mob2)

###### on the other hand literally replaces mob1 on the scene with mob2

##### lecture 006

### 2. Homepage's Examples

#### Example: ContinousMotion

##### lecture 007

#### Example: OpeningManim

##### lecture 008

#### Example: SquareToCircle

##### lecture 009

#### Example: UnionExample

##### lecture 010

#### Example: WarpSquare

##### lecture 011

### 3. Manim's Output Settings

#### lecture 012

#### 3.1 Manim Output Folders

##### command: manim -pql scene.py SquareToCircle

##### High Res.: manim -pqh scene.py SquareToCircle

#### 3.2 Sections

##### JSON file in sections folder

#### 3.3 Some Command Line Flags
 (see:Command-line arguments)
##### -p: plays the animation onces it's rendered

##### -f: replacing -p, open the file browser at the location of the animation instead of playing it

##### -a: render all "Scene" classes

##### -s: output last frame of a scene as one .png static image

##### -ql: specifies low render quality (854x480 15FPS)

##### -qm: medium render quality (1280x720 30FPS)

##### -qh: high render quality (1920x1080 60FPS)

##### -qp: 2k render quality (2560x1440 60FPS)

##### -qk: 4k render quality (3840x2160 60FPS)

##### --format gif: output animations in .gif format instead of default .mp4

### 4. Manim's Buidling Blocks

#### Mobjects

Mobjects are the basic building blocks for all manim animations.

Each class that derives from Mobject represents an object that can be displayed on the screen.


##### Creating and Displaying mobjects

###### Display a mobject: call add() method on the containing Scene

###### Remove a mobject: call remove() method from the containing Scene

###### lecture 013

##### Placing mobjects

###### shift(): shift one unit in the direction from the origin

###### move_to(): use absolute units (measured relative to the ORIGIN)

###### next_to(): uses relative units (measured from the mobject passes as the first argument)

###### align_to(): use direction not as measuring units but as a way to determine the border to use for alignment

* The coordinates of the borders of a mobject are determined using an imaginary bounding box around it.

###### lecture 014

##### Styling mobjects

###### instances of VMobject

* set_stroke(): change visual style of the mobject's border

* set_fill(): change visual style of the mobject's interior

###### instances of Mobject: set_color()

###### opacity (不透明度) parameter

* By default, most mobjectis have a fully transparent interior

* An opacity of 1.0 means fully opaque, while 0.0 means fully transparent

##### Mobject on-screen order

###### the order of the arguments of add() determines the order that the mobjects are displayed on the screen, with the left-most arguments being put in the back

##### lecture 015
 (see:Styling mobjectsMobject on-screen order)
#### Animations

##### Aminations Basic

###### lecture 016

###### lecture 017

###### FadeIn() and FadeOut()
 (see:1.05 fading)
##### Animating methods
 (see:animate())
###### lecture:018
 
Any property of a mobject that can be changedcan be animated.


###### animate() is a property of all mobjects that animates the methods that come afterward

##### Animating run time

###### lecture 019
 
By default, any animation passed to play() lasts for exactlyone second.


###### Use run_time argument to control the duration
 (see:run_time)
##### Creating a custom animation

###### lecture 020: missing LaTex

###### You start by extending the Animation class and overriding its interpolate_mobject()

###### lecture 021

##### Using coordinates of a mobject

###### lecture 022

###### The color name used bases manim_colors
 (see:manim_colors)
##### Transforming mobjects into other mobjects

###### lecture 023

#### Scenes

## 2. Thematic Guides

### 2.1 Configuration

#### Command-line arguments

##### Advanced examples

##### A list of all CLI flags

#### The ManimConfig class

##### Lecture 024: Show Screen Resolution

#### The config files

##### The user config file

##### Cascading config files

#### Order of operations

#### A list of all config options

#### Accessing CLI command options

### 2.2 A deep dive into Manim's internals

#### Introduction

##### Lecture 025

##### 2024/12/04: Got "OSError: [WinErro -2146959355] Server execution failed" error, raise ticket to project

#### Overview

##### Preliminaries

###### Importing the library

* Python Guide 6.4.1 for "from xxx import *"

* __Init__.py in manim

###### Scene instantiation and rendering

* tempconfig() to replace same feature as Manim CLI execution

* scene.render()

  + Scene.setup()

  + Scene.construct()

  + Scene.tear_down()

  + CairoRenderer.scene_finished()

###### Lecture 026: use tempconfig in file

##### Mobject Initialization

###### What even is a Mobject?
 
Mobject stands formathematical object  orManim object.


* The Python class "Mobject" is the base class for all objects that should be displayed on screen

  + Cairo renderer: Cairo Graphics

  + /renderer/cairo_renderer.py

    - ImageMObject

    - PMobject

    - VMObject
 (see:...and what are VMobjects)
###### ...and what are VMobjects

* Bezier Curve

  + A Primer on Bezier civers

* Lecture 027: VMobjectDemo

###### Squares and Circles: back to our Toy Example

* polygram.py

* arc.py

###### Adding Mobjects to the Scene

* Lecture 028

##### Animations and the Render Loop

###### Initializing animations
 (see:1.01 animation)
* Animation.begin()

* Animation.finish()
 (see:Animation.finish())
* Animation.interpolate()

###### The play call: preparing to enter Mainm's render loop

* Scene.play()

###### The render loop (for real this time)

* CairoRenderer.save_static_frame_data()

* Scene.play_internal()

###### Completing the render loop

* Animation.finish()

* Animation.clean_up_from_scene()

###### Lecture 029

### 2.3 Rendering Text and Formulas

#### Text Without LaTeX

##### Lecture 030

###### Text

* Gnome pango library

###### MarkupText

* PangoMarkup

##### Working with Text

###### Using Fonts

* Lecture 031

* Question raised to project discussion board: font is not existed

###### Setting Slant and Weight

* Lecture 032

* Slant

  + NORMAL (default)

  + ITALIC: Roman Style

  + OBLIQUE: Italic Style

* Weight

  + manimpango.Weight

  + NORMAL

  + BOLD

###### Using Colors

* Lecture 033

* color = ColorName

* t2c for iterating text

###### Using Gradients

* Lecture 034

* gradient = (color1, color2, color3)

* t2g for gradients with specific characters

* No gradient effect (strange) when font_size = 70 #4049

###### Setting Line Spacing

* Lecture 035

* line_spacing=value

###### Disabling Ligatures (连字)

* Lecture 036

* disable_ligatures to Text

* "disable_ligatures" doesn't have effect in local environment #4050

###### Iterating

* Lecture 037

* Text objects behave like VGroups

##### Working with MarkupText

###### Lecture 038

###### MarkupText("content with markup", color=, font_size=)

#### Text With LaTex

##### Lecture 039

###### Online LaTex Editor

##### Working with MathTex

###### Lecture 040

##### LaTex commands and keyword arguments

###### Lecture 041

##### Extra LaTeX Packages

###### Lecture 042

###### usepackage{mathrsfs}

##### Substrings and parts

###### Lecture 043: LaTeXSubstrings

###### Lecture 044: IncorrectLaTeXSubstringColoring

###### Lecture 045: CorrectLaTeXSubstringColoring

###### TransformMatchingTex
 (see:1.14.3 TransformMatchingTex)
##### Using index_labels to work with complicated strings
 (see:4.10.3.2 MathTex)
###### Lecture 046: IndexLabelsMathTex

###### index_labels()
 (see:function: index_labels())
##### LaTeX Maths Fonts - The Template Library

###### Lecture 047: LaTeXMathFonts

* TexFontTemplates

###### Lecture 048: LaTeXTemplateLibrary

* error for display Chinese chars: Xelatex error converting to xdv

* Unicode decoder error

* Submit issue: #4052

##### Aligning formulae

###### Lecture 049: LaTeXAlignEnvironment

### 2.4 Adding Voiceovers to Videos
 (see:Voiceover)
#### Basic Usage

##### Lecture 050

##### pip install "manim-voiceover[azure,gtts]"

##### pip install "manim-voiceover[recorder]"

##### pip install "manim-voiceover[transcribe]"

#### Quickstart: voiceover

# Example Gallery

## Basic Concepts

### ManimCELogo

#### Lecture 051: ManimCELogo

### BraceAnnotation

#### Lecture 052: BraceAnnotation

### VectorArrow

#### Lecture 053: VectorArrow

### GradientImageFromArray

#### Lecture 054: GradientImageFromArray

### BooleanOperations

#### Lecture 055: BooleanOperations

## Animations

### PointMovingOnShapes

#### Lecture 056: PointMovingOnShapes

### MovingAround

#### Lecture 057: MovingAround

### MovingAngle

#### Lecture 058: MovingAngle

### MovingDots

#### Lecture 059: MovingDots

### MovingGroupToDestination

#### Lecture 060: MovingGroupToDestination

### MovingFrameBox

#### Lecture 061: MovingFrameBox

### RotationUpdater

#### Lecture 062: RotationUpdater

### PointWithTrace

#### Lecture 063: PointWithTrace

## Plotting with Manim

### SinAndCosFunctionPlot

#### Lecture 064: SinAndCosFunctionPlot

### ArgMinExample

#### Lecture 065: ArgMinExample

### GraphAreaPlot

#### Lecture 066: GraphAreaPlot

### PloygonOnAxes

#### Lecture 067: PolygonOnAxes

### HeatDiagramPlot

#### Lecture 068: HeatDiagramPlot

## Special Camera Settings

### FollowingGraphCamera

#### Lecture 069: FollowingGraphCamera

### MovingZoomedSceneAround

#### Lecture 070: MovingZoomedSceneAround

### FixedInFrameMObjectTest

#### Lecture 071: FixedInFrameMObjectTest

### ThreeDLightSourcePosition

#### Lecture 072: ThreeDLightSourcePosition

### ThreeDCameraRotation

#### Lecture 073: ThreeDCameraRotation

### ThreeDCameraIllusionRotation

#### Lecture 074: ThreeDCameraIllusionRotation

### ThreeDSurfacePlot

#### Lecture 075: ThreeDSurfacePlot

## Advanced Projects

### OpeningManim

#### Lecture 076: OpeningManim

### SineCurveUnitCircle

#### Lecture 077: SinCurveUnitCircle

# Reference Manual

## 1. Animations

### 1.01 animation

#### Lecture 078: OverrideAnimationExample

#### Animation

##### Parameters

###### mobject

###### lag_ratio

###### run_time

###### rate_func

##### Return Type

###### self

##### Lecture 079: LagRatios

#### Wait

### 1.02 changing

#### AnamatedBoundary

##### Lecture 079: AnimatedboundaryExample

#### TracedPath

##### Lecture 080: TracedPathExample

##### Lecture 081: DissipatingPathExample

### 1.03 composition

#### AnimationGroup

#### LaggedStart

##### Lecture 082: LaggedStartExample

#### LaggedStartMap

##### Lecture 083: LaggedStartMapExample

#### Succession

##### Lecture 084: SuccessionExample

### 1.04 creation

#### AddTextLetterByLetter

#### AddTextWordByWord

#### Create

##### Lecture 085: CreateScene

#### DrawBorderThenFill

##### Lecture 086: ShowDrawBorderThenFill

#### RemoveTextLetterByLetter

#### ShowIncreasingSubsets

##### Lecture 087: ShowIncreasingSubsetsScene

#### ShowPartial

#### ShowSubmobjectsOneByOne

#### Spiralln

##### Lecture 088: SpiralInExample

#### Uncreate

##### Lecture 089: ShowUncreate

#### Unwrite

##### Lecture 090: UnwriteReverseTrue & UnwriteReverseFalse

#### Write

##### Lecture 091: ShowWrite & ShowWriteReversed

### 1.05 fading

#### Lecture 092: Fading

#### FadeIn

##### Lecture 093: FadeInExample

#### FadeOut

##### Lecture 094: FadeOutExample

### 1.06 growing

#### Lecture 095: Growing

#### GrowArrow

##### Lecture 096: GrowArrowExample

#### GrowFromCenter

##### Lecture 097: GrowFromCenterExample

#### GrowFromEdge

##### Lecture 098: GrowFromEdgeExample

#### GrowFromPoint

##### Lexture 099: GrowFromPointExample

#### SpinInFromNothing

##### Lecture 100: SpinInFromNothingExample

### 1.07 indication

### 1.08 movement

### 1.09 numbers

### 1.10 rotation

### 1.11 specialized

### 1.12 speedmodifier

### 1.13 transform

### 1.14 transform_matching_parts

#### 1.14.1 TransformMatchingAbstractBase

#### 1.14.2 TransformMatchingShapes

#### 1.14.3 TransformMatchingTex

### 1.15 updaters

## 2. Cameras

## 3. Configurations

## 4. Mobjects

### 4.01 frame

### 4.02 geometry

### 4.03 graph

### 4.04 graphing

### 4.05 logo

### 4.06 matrix

### 4.07 mojbject

#### group

#### Mobject

##### animate()

### 4.08 svg

### 4.09 table

### 4.10 text

#### 4.10.1 code_mobject

#### 4.10.2 numbers

#### 4.10.3 tex_mobject

##### 4.10.3.1 BulletedList

##### 4.10.3.2 MathTex

##### 4.10.3.3 SingleStringMathTex

##### 4.10.3.4 Tex

##### 4.10.3.5 Title

#### 4.10.4 text_mobject

### 4.11 three_d

### 4.12 types

### 4.13 utils

### 4.14 value_tracker

### 4.15 vector_field

## 5. Scenes

## 6. Utilities and other modules

### 6.01 bezier

### 6.02 color

#### core

#### manim_colors

#### AS2700

#### BS381

#### XKCD

#### X11

### 6.03 commands

### 6.04 config_ops

### 6.05 constants

### 6.06 debug

#### function: index_labels()

#### function: print_family

# Add-on

## Voiceover
