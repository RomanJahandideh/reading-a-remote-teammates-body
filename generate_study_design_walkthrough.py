"""Regenerates Figure_Study_Design_Walkthrough (PNG + PDF): the Study 1 / Study 2
procedure flowchart. Rewritten from scratch (no earlier source script existed)
to fix the cramped gap between each box's bold title and its lighter subtitle.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

NAVY = "#0F2438"
WHITE = "#FFFFFF"
SUBTITLE_COLOR = "#B9C4CE"
BAND_FILL = "#F3F5F7"
BAND_EDGE = "#D9DEE3"
BAND_TEXT = "#334155"
LABEL_COLOR = "#4B5563"
ARROW_COLOR = "#F5573F"

CANVAS_W, CANVAS_H = 1036.8, 499.325414
FIG_W_IN, FIG_H_IN = CANVAS_W / 72.0, CANVAS_H / 72.0

BOX_W = 215.242105
BOX_H = 99.574007
BOX_GAP = 43.560903
ROW1_Y0 = 360.189854
ROW2_Y0 = 87.854946
BAND_H = 52.276353
BAND1_Y0 = 291.98166
BAND2_Y0 = 19.646751
FULL_X0 = 22.574436
FULL_X1 = 1014.225564
CENTER_X = (FULL_X0 + FULL_X1) / 2.0

BOX_XS = [FULL_X0 + i * (BOX_W + BOX_GAP) for i in range(4)]

TITLE_SIZE = 21
SUBTITLE_SIZE = 17
HEADING_SIZE = 17
BAND_TITLE_SIZE = 13
BAND_SUB_SIZE = 13
LABEL_SIZE = 13
LINESPACING = 1.18
TITLE_SUBTITLE_GAP = 11  # points of breathing room between title block and subtitle block


def draw_stack(ax, xc, yc, groups):
    """groups: list of (lines, fontsize, color, weight, gap_after) drawn top to bottom,
    centered as a whole block on yc."""
    heights = []
    for lines, fontsize, color, weight, gap_after in groups:
        heights.append(len(lines) * fontsize * LINESPACING + gap_after)
    total_h = sum(heights)
    cursor = yc + total_h / 2.0
    for (lines, fontsize, color, weight, gap_after) in groups:
        for line in lines:
            line_h = fontsize * LINESPACING
            cursor -= line_h
            ax.text(xc, cursor + line_h / 2.0, line, ha="center", va="center",
                    fontsize=fontsize, color=color, fontweight=weight, family="DejaVu Sans")
        cursor -= gap_after


def add_box(ax, x0, y0, title_lines, subtitle_lines=None):
    xc = x0 + BOX_W / 2.0
    yc = y0 + BOX_H / 2.0
    ax.add_patch(FancyBboxPatch((x0, y0), BOX_W, BOX_H,
                                 boxstyle="round,pad=0,rounding_size=8",
                                 linewidth=0, facecolor=NAVY))
    groups = [(title_lines, TITLE_SIZE, WHITE, "bold",
               TITLE_SUBTITLE_GAP if subtitle_lines else 0)]
    if subtitle_lines:
        groups.append((subtitle_lines, SUBTITLE_SIZE, SUBTITLE_COLOR, "normal", 0))
    draw_stack(ax, xc, yc, groups)


def add_band(ax, y0, title, subtitle):
    ax.add_patch(FancyBboxPatch((FULL_X0, y0), FULL_X1 - FULL_X0, BAND_H,
                                 boxstyle="round,pad=0,rounding_size=6",
                                 linewidth=1.1, edgecolor=BAND_EDGE, facecolor=BAND_FILL))
    xc = CENTER_X
    yc = y0 + BAND_H / 2.0
    groups = [
        ([title], BAND_TITLE_SIZE, BAND_TEXT, "bold", 5),
        ([subtitle], BAND_SUB_SIZE, BAND_TEXT, "normal", 0),
    ]
    draw_stack(ax, xc, yc, groups)


def h_arrow(ax, x_start, x_end, y):
    ax.annotate("", xy=(x_end, y), xytext=(x_start, y),
                arrowprops=dict(arrowstyle="-|>", color=ARROW_COLOR, lw=2.4,
                                 shrinkA=0, shrinkB=0, mutation_scale=16))


def v_arrow(ax, x, y_start, y_end, lw=2.4, mutation_scale=16):
    ax.annotate("", xy=(x, y_end), xytext=(x, y_start),
                arrowprops=dict(arrowstyle="-|>", color=ARROW_COLOR, lw=lw,
                                 shrinkA=0, shrinkB=0, mutation_scale=mutation_scale))


fig, ax = plt.subplots(figsize=(FIG_W_IN, FIG_H_IN))
ax.set_xlim(0, CANVAS_W)
ax.set_ylim(0, CANVAS_H)
ax.axis("off")
# Bottom-left origin, y increases upward -- same convention as the extracted
# PDF coordinates below, so they are used as-is with no flipping.

ax.text(BOX_XS[0], 471.159212, "STUDY 1", ha="left", va="center",
        fontsize=HEADING_SIZE, color=NAVY, fontweight="bold", family="DejaVu Sans")

add_box(ax, BOX_XS[0], ROW1_Y0, ["Consent &", "Demographics"])
add_box(ax, BOX_XS[1], ROW1_Y0, ["Open Phase"], ["free", "interpretation"])
add_box(ax, BOX_XS[2], ROW1_Y0, ["Structured", "Phase"], ["forced-choice", "+ SAM"])
add_box(ax, BOX_XS[3], ROW1_Y0, ["Questionnaire"], ["NASA-TLX"])

row1_mid = ROW1_Y0 + BOX_H / 2.0
for i in range(3):
    h_arrow(ax, BOX_XS[i] + BOX_W, BOX_XS[i + 1], row1_mid)

add_band(ax, BAND1_Y0, "Within-subjects design",
          "Research-through-design methodology (ISO 9186 forced-choice convention)")
v_arrow(ax, CENTER_X, ROW1_Y0, BAND1_Y0 + BAND_H, mutation_scale=13, lw=2.0)

# Big transition arrow + label
big_arrow_top = BAND1_Y0
big_arrow_bottom = ROW2_Y0 + BOX_H
v_arrow(ax, CENTER_X, big_arrow_top, big_arrow_bottom, lw=2.6, mutation_scale=18)
label_yc = (big_arrow_top + big_arrow_bottom) / 2.0
ax.text(CENTER_X + 15, label_yc, "independent sample of\n36 participants", ha="left", va="center",
        fontsize=LABEL_SIZE, color=LABEL_COLOR, fontstyle="italic", family="DejaVu Sans",
        linespacing=1.3)

ax.text(BOX_XS[0], 210.824303, "STUDY 2", ha="left", va="center",
        fontsize=HEADING_SIZE, color=NAVY, fontweight="bold", family="DejaVu Sans")

add_box(ax, BOX_XS[0], ROW2_Y0, ["Wearable Setup"], ["Apple Watch"])
add_box(ax, BOX_XS[1], ROW2_Y0, ["Tutorial"], ["Numeric + Icon", "practice"])
add_box(ax, BOX_XS[2], ROW2_Y0, ["3 Missions"], ["No Cue", "Numeric Cue", "Icon Cue"])
add_box(ax, BOX_XS[3], ROW2_Y0, ["Final", "Questionnaire"], ["condition", "ranking"])

row2_mid = ROW2_Y0 + BOX_H / 2.0
for i in range(3):
    h_arrow(ax, BOX_XS[i] + BOX_W, BOX_XS[i + 1], row2_mid)

add_band(ax, BAND2_Y0, "Within-subjects design",
          "Latin-square counterbalanced across three mission layouts")
v_arrow(ax, CENTER_X, ROW2_Y0, BAND2_Y0 + BAND_H, mutation_scale=13, lw=2.0)

plt.tight_layout(pad=1.0)
fig.savefig("Figure_Study_Design_Walkthrough_600dpi.png", dpi=600)
fig.savefig("Figure_Study_Design_Walkthrough.pdf")
print("done")
