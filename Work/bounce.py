# bounce.py
# A rubber ball is dropped from a height of 100 meters and each  time it hits the ground, it bounches back up to 3/5 the height it fell.
# Exercise 1.5

height = 100
bounce = 1



while bounce <= 10:
    height = height * (3/5)
    print(bounce, round(height, 4))
    bounce += 1
