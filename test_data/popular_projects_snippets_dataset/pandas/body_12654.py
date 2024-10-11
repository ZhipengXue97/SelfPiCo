# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_between_time.py
rng = date_range("1/1/2000", "1/5/2000", freq="5min")
ts = DataFrame(np.random.randn(len(rng), 2), index=rng)
ts = tm.get_obj(ts, frame_or_series)

stime = time(0, 0)
etime = time(1, 0)
inclusive = inclusive_endpoints_fixture

filtered = ts.between_time(stime, etime, inclusive=inclusive)
exp_len = 13 * 4 + 1

if inclusive in ["right", "neither"]:
    exp_len -= 5
if inclusive in ["left", "neither"]:
    exp_len -= 4

assert len(filtered) == exp_len
for rs in filtered.index:
    t = rs.time()
    if inclusive in ["left", "both"]:
        assert t >= stime
    else:
        assert t > stime

    if inclusive in ["right", "both"]:
        assert t <= etime
    else:
        assert t < etime

result = ts.between_time("00:00", "01:00")
expected = ts.between_time(stime, etime)
tm.assert_equal(result, expected)

# across midnight
rng = date_range("1/1/2000", "1/5/2000", freq="5min")
ts = DataFrame(np.random.randn(len(rng), 2), index=rng)
ts = tm.get_obj(ts, frame_or_series)
stime = time(22, 0)
etime = time(9, 0)

filtered = ts.between_time(stime, etime, inclusive=inclusive)
exp_len = (12 * 11 + 1) * 4 + 1
if inclusive in ["right", "neither"]:
    exp_len -= 4
if inclusive in ["left", "neither"]:
    exp_len -= 4

assert len(filtered) == exp_len
for rs in filtered.index:
    t = rs.time()
    if inclusive in ["left", "both"]:
        assert (t >= stime) or (t <= etime)
    else:
        assert (t > stime) or (t <= etime)

    if inclusive in ["right", "both"]:
        assert (t <= etime) or (t >= stime)
    else:
        assert (t < etime) or (t >= stime)
