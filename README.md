<h1 align="center">Computing Theory Assignment 2: Creative Task</h1>
<h2 align="center">Paterson's Worms Simulator</h2>

<br>

<p align="center">
  <img src="https://github.com/dan-de-luca/ct-a2-creative-task/assets/80723764/ba722c24-3681-4157-91d9-19c02690f1c2" alt="Paterson's Worm Pixel Art" width="200px" height="50px">
</p>

<p>Name: Daniel De Luca</p>
<p>Student No.: s3951506</p>

<br>

### &nbsp;How to Run:

- Clone the repository: `git clone https://github.com/dan-de-luca/ct-a2-creative-task.git`
- Install python3 and pip on your machine if not already installed.
- Install the required packages with `pip install -r requirements.txt`
- Run the program with `python ./src/menu.py`
- The below Start Menu will appear:

<p align="center">
  <img src="https://github.com/dan-de-luca/ct-a2-creative-task/assets/80723764/ab9ce5d5-4d2e-47dc-9c0f-d624c624e718" alt="Start Menu" width="300px" height="300px">
</p>

- Select Start to run simulator with default configuration.


#### &nbsp;Simulator Defaults:
  - FPS: 60 fps (Trame rate)
  - GRID: 200 -> 200 x 200 cells in the simulator window. (The simulator window is set to 75% of your screen height, squared.)
  - PATTERN: Triangle (Triangular movement pattern)
  - TRACK: True, 10 (Keep track of worm path - last 10 cells visited / eaten)
  - WORMS: 5 (Number of worms to simulate)


#### &nbsp;Simulator Configuration Options:
- Select OPTIONS from the Start Menu to customise the given simulation parameters:

<p align="center">
  <img src="https://github.com/dan-de-luca/ct-a2-creative-task/assets/80723764/ac3622e2-4021-433b-863d-185cf78a8286" alt="Options Menu" width="300px" height="300px">
</p>

- When selecting options, click on the option you want to select, click on a value, then click the BACK button to return to the OPTIONS menu.
- Select any other options, then return to the Start Menu using the BACK button.
- FPS: Increasing the frame rate of the simulation will increase the speed of the worms.
- GRID: Increasing the grid size will increase the number of cells on the grid. NOTE: The window size will not increase, rather, the grid cells will decrease in size to fit within the simulator window.
- PATTERN: Select the movement pattern that the worms will move in. Movement will still be random.
- TRACK: Keep track of the given number of cells from the worms path. This prevents the worm from revisiting any of the selected number of previously visited cells.
- WORMS: The number of worms to simulate.
- Select START to run the simulation with the selected parameters.
- Your parameter selections will be printed to the terminal on simulation start, or the defaults for any unchanged parameters.
- To exit the simulator, click the X button in the top-right-corner if the simulation is running, or click EXIT from the Start Menu if the simulation is not running.

<br>

### &nbsp;The Simulation:

The following are examples of behaviours produced by my implementation of Paterson's Worms for the square movement pattern, followed by the triangle movement pattern.

![python_4vPTPOP7uZ](https://github.com/dan-de-luca/ct-a2-creative-task/assets/80723764/a7e1e8e7-c11d-401f-82e7-c748f9629898)

![python_HmRZGmjzX3](https://github.com/dan-de-luca/ct-a2-creative-task/assets/80723764/0ab3721c-6e11-4cc3-8716-2169697fb4f9)

The triangle movement pattern simulates behaviour closer to that simulated by Mike Paterson in 1969, along with more recent studies, where worms move along line segments on a triangular grid, allowing for six possible directional movements from each grid point, minus those points previously visited by the worms path.

The square movement pattern is a further adaptation of the triangle movement pattern, allowing for eight possible directional movements from any given square on a standard (square) grid, minus those squares previously visited. This adds further randomness to the worms behaviour, producing interesting results.

<br>

#### &nbsp;More Info:

See the ABOUT section located in the simulation Start Menu for more information on Paterson's Worms.

<br>

Thank you for visiting. I hope you enjoy my implementation!
