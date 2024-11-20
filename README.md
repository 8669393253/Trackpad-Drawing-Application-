# Trackpad Drawing Application - README

## Overview

This is a simple **drawing application** built with **Python** and the **Pygame library**. The application allows users to draw freely on the screen using their mouse or trackpad, change brush sizes, select colors, and even switch between different shapes for drawing (lines, circles, rectangles). Additional features include saving the drawing, undoing actions, clearing the screen, and switching between solid and dotted lines.

## Features

- **Freeform Drawing**: Draw freely with the mouse or trackpad.
- **Color Palette**: Choose from five preset colors (Black, Red, Green, Blue, Yellow) for drawing.
- **Brush Size Control**: Adjust the size of the brush using a simple slider.
- **Shape Selection**: Choose between three drawing modes: **Line**, **Circle**, and **Rectangle**.
- **Solid and Dotted Lines**: Toggle between solid lines and dotted lines for drawing.
- **Undo**: Undo the last drawn line with a single keystroke.
- **Clear Screen**: Clear the entire canvas with a keystroke.
- **Save Drawing**: Save the current drawing to a PNG file.
- **Customizable**: Easily modify and extend drawing options like colors, shapes, and more.


## Requirements

- Python 3.x
- Pygame library

To install **Pygame**, run the following command:
pip install pygame

## How to Run

1. Ensure you have Python 3.x installed.
2. Install **Pygame** using the command mentioned above.
3. Save the provided Python script (e.g., `drawing_app.py`).
4. Run the script in your terminal or command prompt:

python drawing_app.p

## Controls

- **Drawing with Mouse/Trackpad**: 
  - Left-click (or tap on trackpad) to start drawing.
  - Hold the mouse/trackpad button and move to draw.
  - Release the button to stop drawing.

- **Color Palette**: 
  - Click on one of the colored squares at the top of the screen to select a drawing color (Black, Red, Green, Blue, Yellow).
  - The selected color will be highlighted, and all drawing will occur in that color.

- **Brush Size**: 
  - Adjust the brush size by clicking and dragging the slider below the color palette.
  - The slider ranges from **1 (smallest)** to **10 (largest)**.

- **Shape Selection**: 
  - Press **1** to select **Line** mode.
  - Press **2** to select **Circle** mode.
  - Press **3** to select **Rectangle** mode.
  - Use the mouse to draw the selected shape (drag for circles/rectangles, click for lines).

- **Drawing Patterns**: 
  - Press **D** to switch to **Dotted Line** mode (small dots will be drawn instead of continuous lines).
  - Press **L** to switch to **Solid Line** mode (default).

- **Undo Action**: 
  - Press **U** to undo the last drawn line.
  - The application will remove the last line drawn and redraw everything except the undone line.

- **Clear the Screen**: 
  - Press **C** to clear the entire drawing area and reset the canvas.

- **Save Drawing**: 
  - Press **S** to save the drawing to a file.
  - You will be prompted to enter a filename (e.g., `drawing.png`).

- **Keyboard Shortcuts**: 
  - **R**: Change the drawing color to **Red**.
  - **G**: Change the drawing color to **Green**.
  - **B**: Change the drawing color to **Blue**.
  - **Y**: Change the drawing color to **Yellow**.
  - **Up Arrow**: Increase the brush size.
  - **Down Arrow**: Decrease the brush size (brush size can't be smaller than 1).


## User Interface

The application includes a basic graphical user interface (GUI) with the following elements:

1. **Color Palette**: A row of color rectangles that allows the user to select the color to draw with.
2. **Brush Size Slider**: A slider under the color palette that adjusts the brush size.
3. **Text Display**: Labels and instructions, such as the current brush size.
4. **Drawing Area**: The main area where users can draw shapes or freeform lines.


## Code Breakdown

### Key Variables:

- **COLOR_OPTIONS**: List of colors available for drawing.
- **COLOR_NAMES**: List of names corresponding to each color in `COLOR_OPTIONS`.
- **brush_size**: Defines the current size of the brush (range from 1 to 10).
- **current_color**: Holds the color currently selected for drawing.
- **drawn_lines**: List that stores drawn lines, used for the undo functionality.
- **brush_pattern**: Defines whether the brush draws solid lines or dotted lines.
- **current_shape**: Defines the current shape for drawing (line, circle, or rectangle).

### Key Functions:

- **save_drawing()**: Allows the user to save their drawing as a PNG file.
- **undo()**: Undoes the last line drawn, by removing it from the drawing history and re-rendering the remaining lines.
- **draw_shape()**: Draws a circle or rectangle, depending on the selected shape mode.
- **draw_ui()**: Draws the user interface elements like the color palette and brush size slider.


## Example Screenshot

Here’s an example of how the app might look when running:


## Customization

You can easily customize this drawing application by:

- **Adding More Colors**: Modify the `COLOR_OPTIONS` and `COLOR_NAMES` lists to include more color choices.
- **Adjusting Brush Size Range**: Change the range of brush sizes by modifying the `brush_size` range in the code.
- **Adding New Shapes**: To introduce more shapes, update the `draw_shape()` function to include new shape types (e.g., triangles, polygons).
- **Expanding UI**: You can add more UI elements such as buttons or even a menu system.


## Known Issues

- **Mouse Lag**: On some systems, there might be a slight lag in drawing due to trackpad sensitivity or mouse input.
- **File Dialog**: The file save mechanism uses a simple input prompt, which may not be user-friendly on all platforms. Implementing a file dialog could improve usability.


## License

This project is open-source and free to use. Feel free to contribute and modify it as needed.


## Contact

If you have any questions or suggestions, please feel free to contact the author or submit an issue on the project repository.
