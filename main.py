from skyfield.api import load

# Create a timescale and ask the current time.
ts = load.timescale()
t = ts.now()

# Load the JPL ephemeris DE421 (covers 1900-2050).
planets = load('de421.bsp')
earth, mars, mercury = planets['earth'], planets['mars'], planets['mercury']

# What's the position of Mars, viewed from Earth?
astrometric = earth.at(t).observe(mars)
ra, dec, distance = astrometric.radec()

print(ra)
print(dec)
print(distance)

# What's the position of Mercury, viewed from Earth?
astrometric = earth.at(t).observe(mercury)
ra, dec, distance = astrometric.radec()

print(ra)
print(dec)
print(distance)