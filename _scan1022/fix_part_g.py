# -*- coding: utf-8 -*-
"""Part G: residual wording fixes in findings the scan does not otherwise change."""
from fixlib import REP


# P-19 used the model's 3.96 m room width; the sheets print 3900 overall / 3200 inner.
REP(
    "In a 3.96 m wide room with the beams running transversely at roughly 1.8-4.2 m centres",
    "In a 3.90 m wide room (3200 clear between the party walls) with the beams running "
    "transversely at roughly 1.8-4.2 m centres",
    "p19-roomwidth",
)

# P-26: the floor count is unchanged, but say why tầng 5 does not add a sixth floor.
REP(
    "So this house is **five occupied floors**.",
    "So this house is **five occupied floors** - tret, lung, tầng 2, tầng 3 and tầng 4. "
    "Tầng 5 adds none, because it holds no rooms at all: only the stair/lift lobby, the "
    "glazed light well and the two sân thượng terraces (IMG_9977).",
    "p26-floorcount",
)
