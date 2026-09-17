"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000

# TODO 1:

def test_negative_rate():
    with pytest.raises(ValueError):
        simulate(1000, -0.4)

# TODO 2:

def test_average():
    N0 = 1000
    lam = 0.4
    dt = 0.01
    steps = 100

    results = []

    for seed in range(100):
        result = simulate(N0, lam, dt, steps, seed)
        results.append(result[-1])

    avg = np.mean(results)
    theoretical = N0 * np.exp(-lam * dt * steps)

    assert avg == pytest.approx(theoretical, rel=0.05)

