# Reading a Remote Teammate's Body: Heart Rate and Variability Cues for Coordination and Understanding in Multiplayer Cooperative Play

LaTeX source for a paper prepared for ACM ISS 2026 / PACM HCI, submitted in the
`acmart` `manuscript,review,anonymous` format.

The paper reports two studies on an ambient avatar display that renders a
teammate's heart rate and heart rate variability as an animated halo, without
naming an emotion:

- **Study 1** tests the icon's legibility online with a chance-referenced
  forced-choice design.
- **Study 2** implements the acquisition, classification, and rendering
  architecture proposed in Study 1 and evaluates it during live cooperative
  multiplayer play, comparing the ambient icon against a no-cue baseline and
  an explicit numeric HR/HRV display.

## Building

The main document is `Main text.tex`, compiled with the bundled `acmart`
class and `ACM-Reference-Format.bst` bibliography style against
`sample-base.bib`.

## Repository contents

- `Main text.tex` — paper source
- `sample-base.bib` — bibliography
- Figures referenced by the paper (`Figure_*.png`, `Icon.jpg`, etc.)
- `research/` — corpus analysis notes used during revision
