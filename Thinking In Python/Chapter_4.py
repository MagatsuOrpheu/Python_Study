"""
This first segment is reserved for the tests. The second part contains the exercises proposed in the book.

1) Turtle
"""

# Import Section
import turtle

# 1) Turtle Tests
bob = turtle.Turtle()
alice = turtle.Turtle()

"""
def bob_t():
    print(bob)  # Create one Turtle
    bob.fd(100)  # Moves bob forward 100 units (based on device screen)
    bob.lt(90)  # Rotates bob 90 degrees


def alice_t():
    print(alice)  # Create another Turtle
    alice.lt(180)  # Rotates alice 180 degrees
    alice.fd(100)  # Moves alice forward 100 units (based on device screen)
    alice.lt(90)
    turtle.mainloop()


bob_t()
alice_t()
"""  # Initial tests

"""
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)
    turtle.mainloop()


polygon(bob, 100, 6)
"""  # Exercises
