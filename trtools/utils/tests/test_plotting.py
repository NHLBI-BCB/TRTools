import numpy as np
import numpy.random as rand
import trtools.utils.plotting as plotting

# These methods produce plots, so can only confirm that the
# tests don't crash. Run these locally to manually check the output

def test_nocrash_PlotHistogram(tmpdir):
    rng = rand.default_rng(2001)
    data = rng.standard_normal(100)
    plotting.PlotHistogram(data, "foo", "bar", (tmpdir / "histo.png"))

def test_nocrash_same_PlotHistogram(tmpdir):
    rng = rand.default_rng(2001)
    data = np.ones((100))
    plotting.PlotHistogram(data, "foo", "bar", (tmpdir / "histo.png"))

def test_nocrash_PlotKDE(tmpdir):
    rng = rand.default_rng(2001)
    data = rng.standard_normal(100)
    plotting.PlotKDE(data, "foo", "bar", (tmpdir / "histo.png"))

def test_nocrash_same_PlotKDE(tmpdir):
    rng = rand.default_rng(2001)
    data = np.ones((100))
    plotting.PlotKDE(data, "foo", "bar", (tmpdir / "histo.png"))

