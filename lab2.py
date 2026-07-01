import curses

text = """Hello world!
This is a tiny text editor.
Edit me!"""

cursor = 0


def draw(screen):
    screen.clear()

    # DRAW DISPLAY

    display = text[:cursor] + "|" + text[cursor:]

    # ----------------------------------------

    for row, line in enumerate(display.split("\n")):
        screen.addstr(row, 0, line)

    screen.addstr(
        len(display.split("\n")) + 1,
        0,
        "← → Move   Type Insert   Backspace Delete   Enter New Line   Esc Quit"
    )

    screen.refresh()


def main(screen):
    global text, cursor

    while True:
        draw(screen)

        key = screen.getch()

        if key == 27:
            break

        # LEFT ARROW

        elif key == curses.KEY_LEFT:

            if cursor > 0:
                cursor -= 1

        # ----------------------------------------

        # RIGHT ARROW

        elif key == curses.KEY_RIGHT:

            if cursor < len(text):
                cursor += 1

        # ----------------------------------------

        # BACK SPACE

        elif key in (8, 127, curses.KEY_BACKSPACE):

            if cursor > 0:
                text = text[:cursor-1] + text[cursor:]
                cursor -= 1

        # ----------------------------------------

        # NEW LINE

        elif key == 10:

            text = text[:cursor] + "\n" + text[cursor:]
            cursor += 1

        # INSERT CHARACTER

        elif 32 <= key <= 126:

            text = text[:cursor] + chr(key) + text[cursor:]
            cursor += 1

        # ----------------------------------------

        #BONUS: Can you figure out how to select one line up/down by yourself? 

        elif key == curses.KEY_UP:
            current_line_start = text.rfind("\n", 0, cursor) + 1
            column = cursor - current_line_start
            if current_line_start > 0:
                previous_line_end = current_line_start - 1
                previous_line_start = text.rfind("\n", 0, previous_line_end) + 1

                previous_line_length = previous_line_end - previous_line_start

                cursor = previous_line_start + min(column, previous_line_length)
               

        elif key == curses.KEY_DOWN:
            current_line_start = text.rfind("\n", 0, cursor) + 1
            column = cursor - current_line_start

            current_line_end = text.find("\n", cursor)

            if current_line_end != -1:
                next_line_start = current_line_end + 1
                next_line_end = text.find("\n", next_line_start)

                next_line_length = next_line_end - next_line_start

                cursor = next_line_start + min(column, next_line_length)
            else:
                    next_line_end = len(text)
                    cursor = next_line_end


curses.wrapper(main)