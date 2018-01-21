# Game_openGl
A children game to teach them good and bad habits, numbers and letters. The game is formed of a maze with objects that are randomly distributed. The main character is the child who tries to collect the right object to win the game.

This code requires PyOpenGl, PyOpenGL_accelerate,numpy and pygame python libraries to run.

The main idea of creating the maze that the window is represented as a multi dimensional array, each block in the maze is represented by a single element in the array. The elements take numbers from 1 to 4, where 1 means top wall, 2 is the right one, 3 is the bottom ,4 is the left and 0 means there is no wall at the current block.
The characters movements depends on the number of the element where he stands, he can't move right if the current number is 2, There is a right wall!
Objects are randomly genereated withing the maze, their places are registered in a list, each movement of the charcater check this list to know if there is an object or not, if object is found it dissappeared and results in increasing score or losing a life.
The game consists of three levels:
1) Level 1: Collect specified number of good objects to win, there is limited attempts to pick a bad object.
2) Level 2: Collect the right letters (regardless to order) to complete a specified word, with a timer in the background.
3) Level 3: Collect the right numbers to give a specified total, with 3 chances to decrement the total and a timer in the background.

We used textures to load images in the game.
