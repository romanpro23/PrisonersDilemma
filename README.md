**What Is the Prisoner's Dilemma?**

The prisoner's dilemma is a paradox in decision analysis in which two individuals acting in their own self-interests do not produce the optimal outcome.

A prime example of game theory, the prisoner's dilemma was developed in 1950 by RAND Corporation mathematicians Merrill Flood and Melvin Dresher during the Cold War (but later given its name by the game theorist Alvin Tucker). Some have speculated that the prisoner's dilemma was crafted to simulate strategic thinking between the U.S.A. and U.S.S.R. during the Cold War.

Today, the prisoner's dilemma is a paradigmatic example of how strategic thinking between individuals can lead to suboptimal outcomes for both players.

**Options for solving the problem**

The code presents a solution to this problem using a genetic algorithm.

The main unit is the player, represented by the Player class, from which anyone can create their own author class with any logic.

Two agents are placed on the stage, where they can choose one of two actions - cooperation or betrayal. If both agents interact, they get 3 points each. If someone decides to betray another, he gets 5 points. And if both players want to betray each other, they get one point each.

The code contains implementations for the most popular algorithms.

The implementation, which works on the basis of neural networks and is optimized using a genetic algorithm, is given separately.

A group of such players is put together for an experiment with other popular algorithms, where they compete against each other and get points, trying to get the maximum.

After the players have played with everyone else, the genetic operators of selection, crossover and mutation are performed on the neural network players to create a new generation that will absorb the best of the predecessors. 

And then the simulation is played again with new players.

**Analysis of results**

At the beginning, when there are a large number of maladaptive players who choose only interaction or betrayal, players who choose only betrayal gain a large number of points, which is reflected in the diagram.

![Scores_epoch_2](https://github.com/romanpro23/PrisonersDilemma/assets/87851373/5e500796-1e43-4c67-af24-924c1a1b68ab)

However, later on, when the number of bad players decreases due to the genetic algorithm helping to optimize, the total reward of the genetic algorithms decreases and their uniformity increases, and the established tit-for-tat algorithms come to the fore, which can also be seen in the graph.

![Scores_epoch_32](https://github.com/romanpro23/PrisonersDilemma/assets/87851373/a10a0ee6-7ad2-478b-9b5a-f0817e2a82ff)

We can summarize the results that the established algorithms can be considered the most effective, and there is no need to look for other solutions using different techniques.
