# TicTacToe with AI
Tic-Tac-Toe is a two-player game where players alternate marking a 3×3 grid, aiming to align three marks in a row. 
With 138 unique terminal board states, the game is solvable, and optimal play ensures either a win or a draw for the first player (X).

## MiniMax Algorithm
The minimax algorithm, used in AI for Tic-Tac-Toe, evaluates all possible moves by constructing a game tree and assigning scores 
to each state: +10 for wins, -10 for losses, and 0 for ties. The algorithm optimizes moves for the AI (maximizer) 
while accounting for the opponent's (minimizer) best responses.

### Ilustration
Lets understand MiniMax algorithm using a example
consider this state and ai wants to make a move so it will gr through all possible moves and will choose most optimal one. 


![state](https://github.com/user-attachments/assets/d727ea1d-0096-4863-955a-83ef930e1b83)


At the maximizer stage (i.e., the AI's turn), the AI will try to maximize its score by using Max(). 
The player (assuming they are playing optimally) will aim to maximize their own score, which effectively minimizes the AI's score. 
Therefore, we use Min() during the player's turn.

![explaination](https://github.com/user-attachments/assets/c050be3c-d861-4a53-8a2a-6cc01497afba)
