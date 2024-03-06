# Hill Climbing Algorithm for String Generation 🧗‍♂️🔠

## Overview 🌐

This repository contains a simple implementation of the Hill Climbing Algorithm in Python. The algorithm aims to generate a target string using the printable characters available.

## How to Use 🚀

1. Run the script.
2. Enter the target string when prompted.
3. The algorithm will attempt to generate the target string using the Hill Climbing approach.

## Algorithm Description 🔄

- **Initial State:** A random string is generated as the initial solution.
- **Evaluation Function:** The evaluation function calculates the difference between the current solution and the target string based on ASCII values.
- **Mutation:** The algorithm randomly mutates the current solution.
- **Iteration:** The algorithm iteratively improves the solution by selecting mutated solutions with lower evaluation scores.

## Parameters ⚙️

- **Iteration Limit:** The algorithm has a limit of 1,000,000 iterations to explore the solution space.

## Outcome 🎯

- If the algorithm successfully generates the target string, it will display the result along with the number of iterations it took.
- If the algorithm does not converge within the iteration limit, it will display a message indicating this.

## Notes 📝

- The success of the algorithm depends on the nature of the problem and the randomness involved.
- Consider adjusting the iteration limit based on the search space and requirements.

Feel free to experiment and modify the code as needed. If you have any questions or improvements, please let me know! 🤖
