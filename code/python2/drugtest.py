
def pdp(actual=0.05, sensi=0.6, speci=0.99):
    true_pos = actual * sensi
    false_pos = (1-actual) * (1-speci)
    print true_pos + false_pos
    ratio = true_pos / (true_pos + false_pos)
    return ratio

print pdp(actual=0.017, sensi=0.6, speci=0.99)
