 Manim

# 1. Manim Installation

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

# 2. Tutorials & Guides

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
 (see:6.02.02 manim_colors)
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
 (see:4.10.03.02 MathTex)
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

# 3. Example Gallery

## 3.1 Basic Concepts

### 3.1.1 ManimCELogo

#### Lecture 051: ManimCELogo
 (see:4.02.01.08 Circle4.02.05.08 Square4.02.05.10 Triangle4.10.03.02 MathTex)
### 3.1.2 BraceAnnotation

#### Lecture 052: BraceAnnotation
 (see:4.08.01.02 Brace)
#### Brace Annotation in LaTeX

\documentclass{article}

\usepackage{amsmath}

\begin{document}

  \[

  \overset{\text{foo}}{\overbrace{a\rightarrow \underset{\text{bar}}{\underbrace{(b \rightarrow c)}}}}

  \]

\end{document}


### 3.1.3 VectorArrow

#### Lecture 053: VectorArrow
 (see:4.02.01.12 Dot4.04.01.04 NumberPlane4.10.04.03 Text)
### 3.1.4 GradientImageFromArray

#### Lecture 054: GradientImageFromArray
 (see:4.12.01.02 ImageMobject)
#### About np.uint8

##### NumPy's Built-in scalar types: Unsigned integer types

#### For loop with underscore(_)

### 3.1.5 BooleanOperations

#### Lecture 055: BooleanOperations
 (see:4.02.02.01 Difference4.02.02.02 Exclusion4.02.02.03 Intersection4.02.03.04 Union)
#### Ref: Boolean Operations in wikipedia

## 3.2 Animations

### 3.2.1 PointMovingOnShapes

#### Lecture 056: PointMovingOnShapes
 (see:1.06.02 GrowFromCenter1.08.03 MoveAlongPath1.10.02 Rotating1.13.19 Transform4.02.01.08 Circle4.02.01.12 Dot4.02.04.06 Line)
### 3.2.2 MovingAround

#### Lecture 057: MovingAround
 (see:4.07.02 Mobject4.12.03.05 VMobject)
### 3.2.3 MovingAngle

#### Lecture 058: MovingAngle
 (see:4.02.04.01 Angle4.07.02 Mobject)
### 3.2.4 MovingDots

#### Lecture 059: MovingDots

### 3.2.5 MovingGroupToDestination

#### Lecture 060: MovingGroupToDestination

### 3.2.6 MovingFrameBox

#### Lecture 061: MovingFrameBox
 (see:4.02.06.03 SurrandingRectangle4.10.03.02 MathTex)
### 3.2.7 RotationUpdater

#### Lecture 062: RotationUpdater
 (see:4.07.02 Mobject)
### 3.2.8 PointWithTrace

#### Lecture 063: PointWithTrace
 (see:1.10.02 Rotating4.12.03.05 VMobject)
## 3.3 Plotting with Manim

### SinAndCosFunctionPlot

#### Lecture 064: SinAndCosFunctionPlot
 (see:4.04.01.01 Axes4.10.03.02 MathTex)
### ArgMinExample

#### Lecture 065: ArgMinExample

### GraphAreaPlot

#### Lecture 066: GraphAreaPlot

### PloygonOnAxes

#### Lecture 067: PolygonOnAxes

### HeatDiagramPlot

#### Lecture 068: HeatDiagramPlot

## 3.4 Special Camera Settings

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

## 3.5 Advanced Projects

### OpeningManim

#### Lecture 076: OpeningManim

### SineCurveUnitCircle

#### Lecture 077: SinCurveUnitCircle

# 4. Reference Manual

## 1. Animations

### 1.01 animation

#### Lecture 078: OverrideAnimationExample

#### 1.01.01 Animation

##### Parameters

###### mobject

###### lag_ratio

###### run_time

###### rate_func

##### Return Type

###### self

##### Lecture 079: LagRatios

#### 1.01.02 Wait

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

#### 1.06.01 GrowArrow

##### Lecture 096: GrowArrowExample

#### 1.06.02 GrowFromCenter

##### Lecture 097: GrowFromCenterExample

#### 1.06.03 GrowFromEdge

##### Lecture 098: GrowFromEdgeExample

#### 1.06.04 GrowFromPoint

##### Lexture 099: GrowFromPointExample

#### 1.06.05 SpinInFromNothing

##### Lecture 100: SpinInFromNothingExample

### 1.07 indication

### 1.08 movement

#### 1.08.01 ComplexHomotopy

#### 1.08.02 Homotopy

#### 1.08.03 MoveAlongPath

#### 1.08.04 PhaseFlow

#### 1.08.05 SmoothedVectorizedHomotopy

### 1.09 numbers

#### 1.09.01 ChangeDecimalToValue

#### 1.09.02 ChangingDecimal

### 1.10 rotation

#### 1.10.01 Rotate

#### 1.10.02 Rotating

### 1.11 specialized

### 1.12 speedmodifier

### 1.13 transform

#### 1.13.01 ApplyCompleFunction

#### 1.13.02 ApplyFunction

#### 1.13.03 ApplyMatrix

#### 1.13.04 ApplyMethod

#### 1.13.05 ApplyPointwiseFunction

#### 1.13.06 ApplyPointwiseFunctionToCenter

#### 1.13.07 ClockwiseTransform

#### 1.13.08 CounterclockwiseTransform

#### 1.13.09 CyclicReplace

#### 1.13.10 FadeToColor

#### 1.13.11 FadeTransform

#### 1.13.12 FadeTransformPieces

#### 1.13.13 MoveToTarget

#### 1.13.14 ReplacementTransform

#### 1.13.15 Restore

#### 1.13.16 ScaleInPlace

#### 1.13.17 ShrinkToCenter

#### 1.13.18 Swap

#### 1.13.19 Transform

#### 1.13.20 TransformAnimations

#### 1.13.21 TransformFromCopy

### 1.14 transform_matching_parts

#### 1.14.1 TransformMatchingAbstractBase

#### 1.14.2 TransformMatchingShapes

#### 1.14.3 TransformMatchingTex

### 1.15 updaters

## 2. Cameras

## 3. Configurations

## 4. Mobjects

### 4.01 frame

#### 4.01.01 FullScreenRectangle

#### 4.01.02 ScreenRectangle

### 4.02 geometry

#### 4.02.01 arc

##### 4.02.01.01 AnnotationDot

##### 4.02.01.02 AnnularSector

##### 4.02.01.03 Annulus

##### 4.02.01.04 Arc

##### 4.02.01.05 ArcBetweenPoints

##### 4.02.01.06 ArcPolygon

##### 4.02.01.07 ArcPolygonFromArcs

##### 4.02.01.08 Circle

##### 4.02.01.09 CubicBezier

##### 4.02.01.10 CurveArrow

##### 4.02.01.11 CurvedDoubleArrow

##### 4.02.01.12 Dot

##### 4.02.01.13 Ellipse

##### 4.02.01.14 LabeledDot

##### 4.02.01.15 Sector

##### 4.02.01.16 TipableVMobject

#### 4.02.02 boolean_ops

##### 4.02.02.01 Difference

##### 4.02.02.02 Exclusion

##### 4.02.02.03 Intersection

##### 4.02.03.04 Union

#### 4.02.03 labeled

##### 4.02.03.01 LabeledArrow

##### 4.02.03.02 LabeledLine

#### 4.02.04 line

##### 4.02.04.01 Angle

##### 4.02.04.02 Arrow

##### 4.02.04.03 DashedLine

##### 4.02.04.04 DoubleArrow

##### 4.02.04.05 Elbow

##### 4.02.04.06 Line

##### 4.02.04.07 RightAngle

##### 4.02.04.08 TangentLine

##### 4.02.04.09 Vector

#### 4.02.05 polygram

##### 4.02.05.01 Cutout

##### 4.02.05.02 Polygon

##### 4.02.05.03 Polygram

##### 4.02.05.04 Rectangle

##### 4.02.05.05 RegularPolygon

##### 4.02.05.06 RegularPolygram

##### 4.02.05.07 RoundedRectangle

##### 4.02.05.08 Square

##### 4.02.05.09 Star

##### 4.02.05.10 Triangle

#### 4.02.06 shape_matchers

##### 4.02.06.01 BackgroundRectangle

##### 4.02.06.02 Cross

##### 4.02.06.03 SurrandingRectangle

##### 4.02.06.04 Underline

#### 4.02.07 tips

##### 4.02.07.01 ArrowCircleFilledTip

##### 4.02.07.02 ArrowCircleTip

##### 4.02.07.03 ArrowSquareFilledTip

##### 4.02.07.04 ArrowSquareTip

##### 4.02.07.05 ArrowTip

##### 4.02.07.06 ArrowTriangleFilledTip

##### 4.02.07.07 StealthTip

### 4.03 graph

#### 4.03.01 DiGraph

#### 4.03.02 GenericGraph

#### 4.03.03 Graph

#### 4.03.04 LayoutFunction

### 4.04 graphing

#### 4.04.01 coordinate_systems

##### 4.04.01.01 Axes

##### 4.04.01.02 ComplexPlane

##### 4.04.01.03 CoordinateSystem

##### 4.04.01.04 NumberPlane

##### 4.04.01.05 PolarPlane

##### 4.04.01.06 ThreeDAxes

#### 4.04.02 functions

##### 4.04.02.01 FunctionGraph

##### 4.04.02.02 ImplicitFunction

##### 4.04.02.03 ParametricFunction

#### 4.04.03 number_line

##### 4.04.03.01 NumberLine

##### 4.04.03.02 UnitInterval

#### 4.04.04 probability

##### 4.04.04.01 BarChart

##### 4.04.04.02 SampleSpace

#### 4.04.05 scale

##### 4.04.05.01 LinearBase

##### 4.04.05.02 LogBase

### 4.05 logo

#### 4.05.01 ManimBanner

### 4.06 matrix

#### 4.06.01 DecimalMatrix

#### 4.06.02 IntegerMatrix

#### 4.06.03 Matrix

#### 4.06.04 MobjectMatrix

### 4.07 mojbject

#### 4.07.01 group

#### 4.07.02 Mobject

##### animate()

### 4.08 svg

#### 4.08.01 brace

##### 4.08.01.01 ArcBrace

##### 4.08.01.02 Brace

##### 4.08.01.03 BraceBetweenPoints

##### 4.08.01.04 BraceLabel

##### 4.08.01.05 BraceText

#### 4.08.02 svg_mobject

##### 4.08.02.01 SVGMobject

##### 4.08.02.02 VMobjectFromSVGPath

### 4.09 table

#### 4.09.01 DecimalTable

#### 4.09.02 IntegerTable

#### 4.09.03 MathTable

#### 4.09.04 MobjectTable

#### 4.09.05 Table

### 4.10 text

#### 4.10.01 code_mobject

##### 4.10.01.01 Code

#### 4.10.02 numbers

##### 4.10.02.01 DecimalNumber

##### 4.10.02.02 Integer

##### 4.10.02.03 Variable

#### 4.10.03 tex_mobject

##### 4.10.03.01 BulletedList

##### 4.10.03.02 MathTex

##### 4.10.03.03 SingleStringMathTex

##### 4.10.03.04 Tex

##### 4.10.03.05 Title

#### 4.10.04 text_mobject

##### 4.10.04.01 MarkupText

##### 4.10.04.02 Paragraph

##### 4.10.04.03 Text

### 4.11 three_d

#### 4.11.01 polyhedra

##### 4.11.01.01 Dodecahedron

##### 4.11.01.02 Icosahedron

##### 4.11.01.03 Octahedron

##### 4.11.01.04 Polyhedron

##### 4.11.01.05 Tetrahedron

#### 4.11.02 three_d_utils

#### 4.11.03 three_dimensions

##### 4.11.03.01 Arrow3D

##### 4.11.03.02 Cone

##### 4.11.03.03 Cube

##### 4.11.03.04 Cylinder

##### 4.11.03.05 Dot3D

##### 4.11.03.06 Line3D

##### 4.11.03.07 Prism

##### 4.11.03.08 Sphere

##### 4.11.03.09 Surface

##### 4.11.03.10 ThreeDVMobject

##### 4.11.03.11 Torus

### 4.12 types

#### 4.12.01 image_mobject

##### 4.12.01.01 AbstractImageMobject

##### 4.12.01.02 ImageMobject

##### 4.12.01.03 ImageMobjectFromCamera

#### 4.12.02 point_cloud_mobject

##### 4.12.02.01 Mobject1D

##### 4.12.02.02 Mobject2D

##### 4.12.02.03 PGroup

##### 4.12.02.04 PMobject

##### 4.12.02.05 Point

##### 4.12.02.06 PointCloudDot

#### 4.12.03 vectorized_mobject

##### 4.12.03.01 CurvesAsSubmobjects

##### 4.12.03.02 DashedVMobject

##### 4.12.03.03 VDict

##### 4.12.03.04 VGroup

##### 4.12.03.05 VMobject

##### 4.12.03.06 VectorizedPoint

### 4.13 utils

### 4.14 value_tracker

#### 4.14.01 ComplexValueTracker

#### 4.14.02 ValueTracker

### 4.15 vector_field

#### 4.15.01 ArrowVectorField

#### 4.15.02 StreamLines

#### 4.15.03 VectorField

## 5. Scenes

### 5.01 moving_camera_scene

#### 5.01.01 MovingCameraScene

### 5.02 section

#### 5.02.01 DefaultSectionType

#### 5.02.02 Section

### 5.03 scene

#### 5.03.01 RerunSceneHandler

#### 5.03.02 Scene

### 5.04 scene_file_writer

#### 5.04.01 SceneFileWriter

### 5.05 three_d_scene

#### 5.05.01 SpecialThreeDScene

#### 5.05.02 ThreeDScene

### 5.06 vector_space_scene

#### 5.05.01 LinearTransformationScene

#### 5.05.02 VectorScene

### 5.07 zoomed_scene

#### 5.07.01 ZoomedScene

## 6. Utilities and other modules

### 6.01 bezier

### 6.02 color

#### 6.02.01 core

##### 6.02.01.01 ManimColor

#### 6.02.02 manim_colors

#### 6.02.03 AS2700

#### 6.02.04 BS381

#### 6.02.05 XKCD

#### 6.02.06 X11

### 6.03 commands

### 6.04 config_ops

#### 6.04.01 DictAsObject

### 6.05 constants

#### 6.05.01 CapStyleType

#### 6.05.02 LineJointType

#### 6.05.03 RendererType

### 6.06 debug

#### function: index_labels()

#### function: print_family

### 6.07 deprecation

### 6.08 docbuild

#### 6.08.01 autoaliasattr_directive

#### 6.08.02 autocolor_directive

#### 6.08.03 manim_directive

#### 6.08.04 module_parsing

### 6.09 hasing

### 6.10 images

### 6.11 ipython_magic

#### 6.11.01 ManimMagic

### 6.12 iterables

### 6.13 paths

### 6.14 rate_functions

### 6.15 simple_functions

### 6.16 sounds

### 6.17 space_ops

### 6.18 testing

#### 6.18.01 _frames_testers

#### 6.18.02 _show_diff

#### 6.18.03 _test_class_makers

##### 6.18.03.01 DummySceneFileWriter

### 6.19 tex

#### 6.19.01 TexTemplate

### 6.20 tex_file_writing

### 6.21 tex_templates

#### 6.21.01 TexFontTemplates

#### 6.21.02 TexTemplateLibrary

### 6.22 typing

# 5. Add-on

## Voiceover
