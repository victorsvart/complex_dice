
# COMPLEX DICE  (sort of)

This version of the Dice program allows the user to roll a maximum of 6 dices.

This version also includes a simple menu, dice rolling suspense and in version 0.0.4 I was finally able to figure the 'random' library out and add the summing of dice results feature.

I made this program to play Tabletob RPGs on Discord with my friends without the need of real dices. (Actually it was more of an excuse to code something than anything else)

Documentation:

In this version, a created a simple menu in a main() Function that inputs the user with the choice the roll dices or to quit the program. The accepted inputs are Yes or No but the user can write that any way he likes, as long as it still means "yes" or "no" in the end (uppercase and lowercase 'y' or 'n' are also accepted). I made this possible by simply applying the .lower() string method to the input. In case of a not accepted input, the user in prompted to try again.

The amount of dices rolled is chosen by the user(max of 6) and the rolls are randomly generated numbers that go from 1 to 6. My first two commits of the project didn't had the feature of summing the generated results like the dice_simple program. But now it HAS!

In the case of the user inputing a letter instead of a number or a out of bounds value, he will also be prompted to try again.

I used three different and simple libraries in this little project.

Used the OS library for a clean visual experience in the... terminal. The TIME library to create a little suspense in the dice roll result. And of course the RANDOM library to output a set of randomly generated numbers that go from 1 to 6.


