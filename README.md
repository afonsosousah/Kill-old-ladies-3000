# Turbo Racing 3000

![Gameplay](https://github.com/afonsosousah/Turbo-Racing-3000/blob/1.0.1/assets/gameplay.gif)

## Project Description
This project is a car game, where in the singleplayer mode your goal is to avoid collisions with enemy cars to achieve the highest score possible.
In the multiplayer mode you are competing with another car that you can also collide with.

## Installation Instructions
1. Download the [release](https://github.com/afonsosousah/Turbo-Racing-3000/archive/refs/tags/1.0.1.zip)
2. If you haven't installed pip, please install it
3. Run ```pip install -r requirements.txt```
4. See the next section to run the code

## How to run the game
Open the 'game' folder on Visual Studio Code/PyCharm, and run 'main.py'

## Project Structure
- main.py - File that starts the game
- interface.py - Main menu, How to play and Credits GUIs
- game.py - Singleplayer game loop
- multiplayer_game.py - Multiplayer game loop
- car_selector.py - Car selector GUI
- multiplayer_car_selector.py - Multiplayer car selector GUI
- car.py - Define Car class
- power_up.py - Define PowerUp class and all the child classes
- fuel_can.py - Define the FuelCan class
- requirements.txt - Specifies the required modules
- /assets - Folder where all images and songs are stored

## Credits
- Afonso Hermenegildo 20221958
- Diogo Oliveira 20221930
- Tomás Rodrigues 20221956

## License

MIT License

Copyright (c) 2023 afonsosousah

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
