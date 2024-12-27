This project is an open-source terminal-based solver for https://wafflegame.net

The code generates solved waffle boards after taking an unsolved waffle game as an input

To run it, launch main.py  
Input your waffle exactly as you see it on the screen  
On an average machine, an average Waffle should take around 3-5 seconds to solve completely  
The generation of optimal swaps should take under 1 minute for hard waffles and under 5 seconds for easier waffles

The algorithm will solve the Waffle completely using a list of 14855 5-letter words (All the words accepted by Wordle)

For now, the project only supports daily waffles (5x5), but support for 7x7 Waffles is on the roadmap

Other things on the roadmap include:\
-Optimisation for the current solver, possibly migrating computationally complex parts to C++\
-Optimization for the optimal swap generator\
-A more user-friendly GUI\
-A solver that accounts for yellow letters

If you want to contribute to the project or simply say thank you, you can find me on discord as `blanwhit`