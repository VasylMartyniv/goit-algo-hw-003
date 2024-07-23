import math

from PIL import Image, ImageDraw


def draw_koch_segment(draw, order, p1, p2):
    if order == 0:
        draw.line([p1, p2], fill="blue", width=1)
    else:
        (x1, y1), (x5, y5) = p1, p2
        dx = (x5 - x1) / 3
        dy = (y5 - y1) / 3
        x2, y2 = x1 + dx, y1 + dy
        x4, y4 = x5 - dx, y5 - dy
        x3 = (x2 + x4 + math.sqrt(3) * (y2 - y4)) / 2
        y3 = (y2 + y4 + math.sqrt(3) * (x4 - x2)) / 2

        draw_koch_segment(draw, order - 1, (x1, y1), (x2, y2))
        draw_koch_segment(draw, order - 1, (x2, y2), (x3, y3))
        draw_koch_segment(draw, order - 1, (x3, y3), (x4, y4))
        draw_koch_segment(draw, order - 1, (x4, y4), (x5, y5))


def draw_koch_snowflake(order, size):
    image = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(image)
    p1 = (size / 4, size / 2)
    p2 = (3 * size / 4, size / 2)
    p3 = ((p1[0] + p2[0]) / 2, p1[1] - (math.sqrt(3) / 2) * (p2[0] - p1[0]))

    draw_koch_segment(draw, order, p1, p2)
    draw_koch_segment(draw, order, p2, p3)
    draw_koch_segment(draw, order, p3, p1)

    return image


def main():
    level = int(input("Enter recursion: "))
    size = 800

    image = draw_koch_snowflake(level, size)
    image.save(f"koch_snowflake_level_{level}.png")
    image.show()


if __name__ == "__main__":
    main()
