import pygame
import datetime
from tools import draw_shape, flood_fill

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1000, 700
FPS = 120

COLORS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
}

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Extended Paint App - TSIS 2")

canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(COLORS["white"])

font = pygame.font.SysFont("Arial", 24)
ui_font = pygame.font.SysFont("Arial", 16)


def draw_ui(current_tool, current_color, current_size):
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, WIDTH, 30))
    pygame.draw.line(screen, (100, 100, 100), (0, 30), (WIDTH, 30), 2)

    text1 = f"Tool: {current_tool.upper()} | Color: {current_color} | Size: {current_size}px"
    text2 = "P Pencil | L Line | R Rect | C Circle | Q Square | T Text | F Fill | E Eraser"

    screen.blit(ui_font.render(text1, True, COLORS["black"]), (10, 5))
    screen.blit(ui_font.render(text2, True, COLORS["black"]), (10, 15))


def main():
    clock = pygame.time.Clock()

    current_tool = "pencil"
    current_color = "black"
    current_color_rgb = COLORS[current_color]

    sizes = {
        pygame.K_1: 2,
        pygame.K_2: 5,
        pygame.K_3: 10,
    }
    current_size = 5

    drawing = False
    last_pos = None
    start_pos = None

    typing_mode = False
    text_input = ""
    text_pos = (0, 0)

    running = True

    while running:
        screen.blit(canvas, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if typing_mode:
                    if event.key == pygame.K_RETURN:
                        text_surface = font.render(text_input, True, current_color_rgb)
                        canvas.blit(text_surface, text_pos)
                        typing_mode = False
                        text_input = ""

                    elif event.key == pygame.K_ESCAPE:
                        typing_mode = False
                        text_input = ""

                    elif event.key == pygame.K_BACKSPACE:
                        text_input = text_input[:-1]

                    else:
                        text_input += event.unicode

                    continue

                if event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    filename = f"canvas_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                    pygame.image.save(canvas, filename)
                    print("Saved:", filename)

                if event.key in sizes:
                    current_size = sizes[event.key]

                if event.key == pygame.K_p:
                    current_tool = "pencil"
                elif event.key == pygame.K_l:
                    current_tool = "line"
                elif event.key == pygame.K_r:
                    current_tool = "rect"
                elif event.key == pygame.K_c:
                    current_tool = "circle"
                elif event.key == pygame.K_q:
                    current_tool = "square"
                elif event.key == pygame.K_t:
                    current_tool = "text"
                elif event.key == pygame.K_f:
                    current_tool = "fill"
                elif event.key == pygame.K_e:
                    current_tool = "eraser"
                elif event.key == pygame.K_7:
                    current_tool = "right_tri"
                elif event.key == pygame.K_8:
                    current_tool = "eq_tri"
                elif event.key == pygame.K_9:
                    current_tool = "rhombus"

                if event.key == pygame.K_z:
                    current_color = "black"
                elif event.key == pygame.K_x:
                    current_color = "red"
                elif event.key == pygame.K_v:
                    current_color = "green"
                elif event.key == pygame.K_b:
                    current_color = "blue"

                current_color_rgb = COLORS[current_color]

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if event.pos[1] < 30:
                        continue

                    if current_tool == "text":
                        typing_mode = True
                        text_pos = event.pos
                        text_input = ""

                    elif current_tool == "fill":
                        flood_fill(canvas, event.pos, current_color_rgb)

                    else:
                        drawing = True
                        start_pos = event.pos
                        last_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and drawing:
                    drawing = False

                    if current_tool == "line":
                        pygame.draw.line(
                            canvas,
                            current_color_rgb,
                            start_pos,
                            event.pos,
                            current_size
                        )

                    elif current_tool in [
                        "rect",
                        "circle",
                        "square",
                        "right_tri",
                        "eq_tri",
                        "rhombus",
                    ]:
                        draw_shape(
                            canvas,
                            current_color_rgb,
                            start_pos,
                            event.pos,
                            current_tool,
                            current_size
                        )

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if current_tool == "pencil":
                        pygame.draw.line(
                            canvas,
                            current_color_rgb,
                            last_pos,
                            event.pos,
                            current_size
                        )
                        last_pos = event.pos

                    elif current_tool == "eraser":
                        pygame.draw.line(
                            canvas,
                            COLORS["white"],
                            last_pos,
                            event.pos,
                            current_size
                        )
                        last_pos = event.pos

        if drawing and current_tool not in ["pencil", "eraser", "fill", "text"]:
            mouse_pos = pygame.mouse.get_pos()

            if current_tool == "line":
                pygame.draw.line(
                    screen,
                    current_color_rgb,
                    start_pos,
                    mouse_pos,
                    current_size
                )
            else:
                draw_shape(
                    screen,
                    current_color_rgb,
                    start_pos,
                    mouse_pos,
                    current_tool,
                    current_size
                )

        if typing_mode:
            text_surface = font.render(text_input + "|", True, current_color_rgb)
            screen.blit(text_surface, text_pos)

        draw_ui(current_tool, current_color, current_size)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()