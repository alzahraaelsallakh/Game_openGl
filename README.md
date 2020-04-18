# Habits Maze Game 

This project is for Computer Graphics course.

The maze game is a way to teach kids what are good and bad habits, number and letters. 
The maze contains many objects that are randomly distributed, where the player role is to collect the right objects to win using keyboard buttons.

## Games' Levels:
- Level 1: Collect specific number of objects that represent good habits. There is a limited attempts to pick bad habit object. 
- Level 2: Collect letters that form a specific word within the allowed time. 
- Level 3: Collect numbers that sums up the required total number, with 3 chances to decrement the total and the timer. 

The maze for level 1: 
<p align="center">
<img  src="../media/level1.jpg?raw=true" width="600" height="550"> 
</p>


## Implementation

The game is implemented in python and OpenGL 

  The main idea of creating the maze that the window is represented as a multi dimensional array, each block in the maze is represented by a single element in the array. The elements take numbers from 1 to 4, where 1 stands a top wall, 2 for right wall, 3 for bottom wall, 4 for left wall and 0 means there is no wall at the current block as follow:

 <p align="center">
<img  src="../media/fourWalls.png?raw=true">    <img  src="../media/twoWalls.png?raw=true">
</p>

The character movements depends on the number of the element where he stands, he can't move right if the current number is 2, as there is a right wall. 
Objects are randomly genereated withing the maze, their places are stored in a list, each movement of the charcater checks the list to know if there is an object or not, if object is found it dissappeared and results in increasing score or losing a life.  

Textures are used to load images in the game.

## Used Libraries
  - PyOpenGL 
  - PyOpenGL_accelerate 
  - numpy 
  - pygame
  



