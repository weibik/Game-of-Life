# Conway's Game of Life

Conway's Game of Life implementation in Python using Pygame.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Preview](#preview)
- prerequisites(#prerequisites)


## Description

Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway. The "game" is a zero-player game, meaning that its evolution is determined by its initial state, with no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

This implementation includes a Pygame-based graphical user interface to visualize the evolution of the cells.

## Features

- Interactive Pygame GUI.
- Start/Stop button to toggle the simulation.
- Clear button to reset the board.
- Drawing mode to toggle cell states manually.
- Follows the rules of Conway's Game of Life.

## Prerequisites
1. Install poetry (on windows powershell)
    ```bash
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -)
2. Add path to the windows environmental variables:
   ```bash
    %APPDATA%\Python\Script

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/weibik/game-of-life.git

2. Navigate to the project directory:
   ```bash
   cd game-of-life

## Usage 
   ```bash
   poetry run main.py
```
  

- Use the "Start/Stop" button to toggle the simulation.
- Use the "Clear" button to reset the board.
- Click on cells to toggle their state in drawing mode.

## Preview
![image](https://github.com/weibik/Game-of-Life/assets/57102801/1c77ff01-7c82-41a4-b49e-57b86a4bc49e)
