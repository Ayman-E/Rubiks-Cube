# Rubiks-Cube
Algorithm that solves a Rubiks cube using the beginners method

Further Improvements to the project:
- Utilizle Computer Vision better
  - Currently, the cube has to be in a fixed position. I would like to make the computer detect the edges of the cube and read the colors from there
- Test the code further
  - Tested with randomized testing by making a function that randomizes the cube. Would run the code 10,000 times in a row with no errors
  - Would like to do further unit testing
- Clean up the code
  - Partially complete, needs more work
  - Reduce repetitive lists/dictionaries
  - Potentially combine similar helper functions
  - Descriptive and concise comments
- Make the algorithm more efficient and take less steps
  - The current average steps to solve is 223, it has been shown that any cube can be solved in 20 moves or less
  - Skip steps like Yellow Daisy / Switch algorithm to non-beginner algorithm
- Add more error catching, if the input is invalid, it continuously tries to solve the impossible cube
