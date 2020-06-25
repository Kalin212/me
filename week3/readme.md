TODO: Reflect on what you learned this week and what is still unclear.

I found many resources for exercise one on how to check if the input is the correct type, but the one i oringally used involved ValueError which when the tests ran it didnt like. but then when i changed it to exception as e it worked fine. 

exercise 2 doesnt require any changes so that was easy to pass haha. the code in exercise 2 was easily understandable and very useful for exercise 3 and 4.

the not number rejector doesnt work properly for some reason the way i have done it, but i redeveloped it in exercise 3 so its fine now. 

exercise 3 was pretty easy. Using the code from exercise 2 and the code from exercise 1 made it a lot easier and pretty straightfoward. 

Exercise 4 was by far the hardest and involved a fair bit of research but i managed to complete it eventually after many tries. A strange occurence that i found is that rarely the tries counter will fail one of the tests if the computer guesses the number on the first try, because then the tries = 0. However if i made it so that guessing the number itself counts as a guess then half of exercise 4 wont pass because apparently its less than the expected required. I am not sure why this happens. i couldnt figure out whats wrong with my math in that because i think i am using the most effecient formula, so i assumed that when you guess the number it isnt meant to count as a try. This fixed it but about 10% of the time when i run the final test one of the parts in exercise 4 will fail due to getting it first try and tries counter being 0 so it assumes that i havent started the exercise. 