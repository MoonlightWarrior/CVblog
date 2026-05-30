"""
Manim scene: gradient descent morphing into Adam (via momentum).
Rendered twice with different text colors (light/dark mode) against a
transparent background, then embedded as looping <video> elements.

Render (from repo root):
  manim -t -qh --format=webm _manim_build/optimizer_evolution.py OptimizerEvolution
The -t flag = transparent background. COLOR env var picks the text color.
"""

import os
from manim import *

TEXT_COLOR = os.environ.get("MANIM_TEXT_COLOR", "#1565c0")
ACCENT = os.environ.get("MANIM_ACCENT_COLOR", "#e0552b")
BG_COLOR = os.environ.get("MANIM_BG_COLOR", "#ffffff")
M_COLOR = os.environ.get("MANIM_M_COLOR", "#0f9d58")  # first moment (mean)
V_COLOR = os.environ.get("MANIM_V_COLOR", "#9334e6")  # second moment (variance)


class OptimizerEvolution(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR  # matches the site theme

        label_kw = dict(color=TEXT_COLOR, font_size=34)
        eq_kw = dict(color=TEXT_COLOR, font_size=46)

        # Labels always sit at a fixed height above the equation row
        LABEL_Y = 1.1

        # --- Stage 1: plain gradient descent ---
        label = Tex(r"\textbf{gradient descent}", **label_kw).move_to(UP * LABEL_Y)
        gd = MathTex(r"\theta_{t+1} = \theta_t - \eta\, g_t", **eq_kw)

        self.play(Write(gd), run_time=1.2)
        self.play(FadeIn(label, shift=UP * 0.2), run_time=0.6)
        self.wait(1.3)

        # --- Stage 2: introduce momentum (g_t -> m_t) ---
        label2 = Tex(r"\textbf{+ momentum}", color=ACCENT, font_size=34).move_to(UP * LABEL_Y)
        mom = MathTex(r"\theta_{t+1} = \theta_t - \eta\, m_t", **eq_kw)
        mom.move_to(gd)
        # highlight the term that changes
        mom_term = mom[0][-2:]
        mom_term.set_color(ACCENT)

        self.play(
            TransformMatchingTex(gd, mom),
            FadeOut(label, shift=UP * 0.2),
            run_time=1.3,
        )
        self.play(FadeIn(label2, shift=UP * 0.2), run_time=0.5)
        self.wait(1.3)

        # Color map for the first/second moment estimates
        moment_colors = {
            r"\hat{m}_t": M_COLOR,
            r"\hat{v}_t": V_COLOR,
        }

        # --- Stage 3: full Adam update (adaptive, color-coded moments) ---
        label3 = Tex(r"\textbf{Adam}", color=ACCENT, font_size=34).move_to(UP * LABEL_Y)
        adam = MathTex(
            r"\theta_{t+1}", r"=", r"\theta_t", r"-", r"\eta",
            r"\frac{\hat{m}_t}{\sqrt{\hat{v}_t}+\epsilon}",
            tex_to_color_map=moment_colors,
            **eq_kw,
        )
        adam.move_to(mom)

        self.play(
            TransformMatchingTex(mom, adam),
            FadeOut(label2, shift=UP * 0.2),
            run_time=1.4,
        )
        self.play(FadeIn(label3, shift=UP * 0.2), run_time=0.5)
        self.wait(1.8)

        # --- Stage 4: AdamW (decoupled weight decay) ---
        label4 = Tex(r"\textbf{AdamW}", color=ACCENT, font_size=34).move_to(UP * LABEL_Y)
        adamw = MathTex(
            r"\theta_{t+1}", r"=", r"\theta_t", r"-", r"\eta",
            r"\left(\frac{\hat{m}_t}{\sqrt{\hat{v}_t}+\epsilon}", r"+",
            r"\lambda\,\theta_t\right)",
            tex_to_color_map=moment_colors,
            **eq_kw,
        )
        adamw.move_to(adam)
        # highlight the new decoupled weight-decay term
        adamw.set_color_by_tex(r"\lambda\,\theta_t\right)", ACCENT)

        self.play(
            TransformMatchingTex(adam, adamw),
            FadeOut(label3, shift=UP * 0.2),
            run_time=1.4,
        )
        self.play(FadeIn(label4, shift=UP * 0.2), run_time=0.5)
        self.wait(2.2)

        # --- Loop back: fade to GD so the video repeats cleanly ---
        gd_again = MathTex(r"\theta_{t+1} = \theta_t - \eta\, g_t", **eq_kw)
        gd_again.move_to(adamw)
        self.play(
            TransformMatchingTex(adamw, gd_again),
            FadeOut(label4, shift=UP * 0.2),
            run_time=1.2,
        )
        self.play(FadeOut(gd_again), run_time=0.6)
        self.wait(0.4)
