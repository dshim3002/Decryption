from mcmc import mcmc

d = "abcdefghijklmnopqrstuvwxyz"


def test_mcmc():
    assert d != mcmc(d, 0.5)
