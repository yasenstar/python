from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class RecorderExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService())

        circle = Circle()

        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
        
        with self.voiceover(text="Let's shift it to the left 2 untis.") as tracker:
            self.pay(circle.animate.shift(2*LEFT), run_time=tracker.duration)