import pygame
import sys
from pygame.locals import *

# Initialize pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Trackpad Drawing with Finger")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
COLOR_OPTIONS = [BLACK, RED, GREEN, BLUE, YELLOW]
COLOR_NAMES = ["Black", "Red", "Green", "Blue", "Yellow"]

# Set up drawing settings
screen.fill(WHITE)
drawing = False
last_pos = None
brush_size = 5  # Default size
current_color = BLACK
drawn_lines = []  # Store drawn lines for undo feature
brush_pattern = 'solid'  # Options: 'solid', 'dotted'
current_shape = 'line'  # Options: 'line', 'circle', 'rectangle'

# Function to save the drawing with a custom path
def save_drawing():
    file_name = input("Enter filename to save (e.g., drawing.png): ")
    if not file_name.endswith('.png'):
        file_name += '.png'
    pygame.image.save(screen, file_name)
    print(f"Drawing saved as {file_name}")

# Function to undo the last drawn line
def undo():
    if drawn_lines:
        last_line = drawn_lines.pop()
        # Redraw everything except the last line
        screen.fill(WHITE)
        for line in drawn_lines:
            pygame.draw.lines(screen, line[0], False, line[1], line[2])
        pygame.display.update()

# Function to draw a shape (circle or rectangle)
def draw_shape(start_pos, end_pos, shape_type):
    if shape_type == 'circle':
        radius = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5)
        pygame.draw.circle(screen, current_color, start_pos, radius, brush_size)
    elif shape_type == 'rectangle':
        rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
        pygame.draw.rect(screen, current_color, rect, brush_size)

# Function to draw the color palette and size slider
def draw_ui():
    # Draw color palette at the top
    palette_x = 10
    palette_y = 10
    palette_width = 50
    palette_height = 50
    for i, color in enumerate(COLOR_OPTIONS):
        pygame.draw.rect(screen, color, (palette_x + i * (palette_width + 10), palette_y, palette_width, palette_height))
        pygame.draw.rect(screen, (0, 0, 0), (palette_x + i * (palette_width + 10), palette_y, palette_width, palette_height), 3)
        # Draw color names under each color
        font = pygame.font.SysFont(None, 24)
        color_name = font.render(COLOR_NAMES[i], True, (0, 0, 0))
        screen.blit(color_name, (palette_x + i * (palette_width + 10), palette_y + palette_height + 5))

    # Draw brush size control slider
    slider_x = 10
    slider_y = 80
    slider_width = 200
    slider_height = 20
    pygame.draw.rect(screen, (200, 200, 200), (slider_x, slider_y, slider_width, slider_height))
    pygame.draw.rect(screen, current_color, (slider_x + (brush_size - 1) * (slider_width / 10), slider_y, 20, slider_height))
    
    # Brush size text
    font = pygame.font.SysFont(None, 24)
    brush_size_text = font.render(f"Brush Size: {brush_size}", True, (0, 0, 0))
    screen.blit(brush_size_text, (slider_x + slider_width + 10, slider_y))

# Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Detect mouse (or trackpad) movement and drawing
        if event.type == MOUSEMOTION:
            if drawing:  # Only draw if the drawing mode is active
                if brush_pattern == 'solid':
                    pygame.draw.line(screen, current_color, last_pos, event.pos, brush_size)
                elif brush_pattern == 'dotted':
                    pygame.draw.circle(screen, current_color, event.pos, brush_size)  # Small circles for dotted effect
            last_pos = event.pos

        # Detect mouse button press (start drawing when finger touches trackpad)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button or trackpad press
                drawing = True
                last_pos = event.pos  # Set the starting point for drawing

                # Check if the user clicked on a color in the palette
                for i, color_rect in enumerate(COLOR_OPTIONS):
                    color_rect_x = 10 + i * 60
                    if color_rect_x <= event.pos[0] <= color_rect_x + 50 and 10 <= event.pos[1] <= 60:
                        current_color = COLOR_OPTIONS[i]

                # Check if the user clicked on the brush size slider
                if 10 <= event.pos[0] <= 210 and 80 <= event.pos[1] <= 100:
                    brush_size = max(1, min(10, (event.pos[0] - 10) // 20 + 1))

                # Record the drawing action for undo
                if current_shape == 'line':
                    drawn_lines.append((current_color, [last_pos], brush_size))
                elif current_shape in ['circle', 'rectangle']:
                    draw_shape(last_pos, last_pos, current_shape)

        # Detect mouse button release (stop drawing when finger is lifted)
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button or trackpad press release
                drawing = False
                if current_shape == 'line':
                    drawn_lines[-1][1].append(last_pos)  # Add the last position to the line

        # Keypresses for additional features
        if event.type == KEYDOWN:
            if event.key == K_c:  # Clear the screen
                screen.fill(WHITE)
                drawn_lines.clear()  # Clear stored lines for undo
            elif event.key == K_r:  # Change color to red
                current_color = RED
            elif event.key == K_g:  # Change color to green
                current_color = GREEN
            elif event.key == K_b:  # Change color to blue
                current_color = BLUE
            elif event.key == K_y:  # Change color to yellow
                current_color = YELLOW
            elif event.key == K_UP:  # Increase brush size
                brush_size += 1
            elif event.key == K_DOWN:  # Decrease brush size
                brush_size = max(1, brush_size - 1)  # Don't let brush size go below 1
            elif event.key == K_s:  # Save the drawing
                save_drawing()
            elif event.key == K_u:  # Undo the last drawing
                undo()
            elif event.key == K_d:  # Switch to dotted lines
                brush_pattern = 'dotted'
            elif event.key == K_l:  # Switch to solid lines
                brush_pattern = 'solid'
            elif event.key == K_1:  # Draw in line mode
                current_shape = 'line'
            elif event.key == K_2:  # Draw in circle mode
                current_shape = 'circle'
            elif event.key == K_3:  # Draw in rectangle mode
                current_shape = 'rectangle'

    # Draw UI elements (color palette and size slider)
    draw_ui()

    # Update the display
    pygame.display.update()
