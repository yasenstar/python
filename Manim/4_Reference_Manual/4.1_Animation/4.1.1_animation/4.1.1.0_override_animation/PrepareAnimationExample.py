from manim import Square, FadeIn
s = Square()
print(s)
prepare_animation(FadeIn(s))

# Error Message:
# Traceback (most recent call last):
#   File "d:\GitHub\python\Manim\4_Reference_Manual\4.1_Animation\4.1.1_animation\4.1.1.0_override_animation\PrepareAnimationExample.py", line 4, in <module>
#     prepare_animation(FadeIn(s))
#     ^^^^^^^^^^^^^^^^^
# NameError: name 'prepare_animation' is not defined