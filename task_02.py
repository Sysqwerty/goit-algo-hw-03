import turtle


DEFAULT_ORDER = 3


def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 130)
    t.pendown()

    size = 300

    koch_snowflake(t, order, size)

    window.mainloop()


if __name__ == "__main__":
    try:
        order = int(input("Введіть рівень рекурсії (ціле число): "))
    except:
        order = DEFAULT_ORDER
    draw_koch_snowflake(order)
