TODO: Reflect on what you learned this week and what is still unclear.

exercise 1 was fairly straightfoward. i think that my little experience in Pascal from school has allowed me to grasp the basics of Python a lot faster. Python seems more simple than pascal cuz in pascal u have to define all the variables and there types and shit at the start of the file for it to work but in python u can introduce a variable anywhere in the code it seems. One thing i dont like about python is that indentation actually will fuck up the execution if u do it wrong and im not exactly sure where im meant to indent in python but thats a minor issue and i can fix it pretty quick usually. 

exercise 2: 'Map' object is not subscriptable error occuring at line 18 but when running the full test it comes off as a green tick so im just gonna move on since it works despite that error message. 

ive put a breakpoint at line 12 on exercise 3 to test the first task but when i try to run the full test of just the F5 test it reads beyond the breakpoint and returns a syntax error line 41 so i cant even see if ive done the first thing right. kinda annoying. Ive made a new file just to test out different solutions so i dont have to rely on the test.exe thing cuz it fucks up as soon as you make a syntax errer. I am running it and it stops at exercise 3 cuz it cant read it properly and then gives me a nyan cat and tells me ive completed all the exerices when really i havent. kinda annoyed at constantly seeing this nyan cat now >:(  lol. not a rad cat - im sorry. 

for the loops_1a: im confused how the for loop works. I can complete the task with a while loop but for loops are different than how they worked in pascal so idk what to do and im struggling to understand them even with google. I think i have to make an array or list for this exercise and thats generally something i have struggled with before and never understood too well. 

alright i have undone the code i have done beyond is_odd cuz it wasnt working anyway and it least it somewhat fixed the tests.py execute. cuz now it can read my is_odd solution and is giving me a pass on it. but im not getting any crosses beyond that so idk what i have done wrong anymore. maybe i needa find the original file and replace everything beyond the first task on exercise 3 to fix the tests.py. OK nevermind. i wrote return none instead of return None (capital letter missing) and this fixed the tests.py and im getting the crosses on the exercises i havent done so thats good. 

i made stackoverflow and microsoft teams to dark mode cuz i like it more and it doesnt blind me like a flashbang everytime i alt-tab to google to search a question for python lol. every website should be dark mode by default ngl. 

i thought i understood what return does but i done anymore. keep getting - SyntaxError: 'return' outside function. now and its messing up the tests. i guess i needa try figure out what return does exactly to understand y im getting errors around it that are messing up everything

something said ALT - F8 too look at problem or something and i tried it and it seems pretty useful cuz its showing me problems which the debugger and the tests.py arent. this seems very useful. hopefully it will help me understand the errors in the code that the computer is not liking. 

OK so moves and should_move are booleans which means that they are true/false values but when i write 
    if moves == True and should_move == True:
    fix_it = 'No Problem'
it says moves is undefined variable. and when i type moves its not the same colour as it is in the def statement. idk what this is all about but i think it has something to do with all the errors and the code not working. i dont think i understand def or return very well and its messing me up a bit i think idk. 

So ive just noticed in loops 1a if you dont have everything indented once from the def loops_1a u get an error of return being outside of normal function. I think i have been having this error before but now ik that i have to do that at least. 

i looked at the video tutorial, im just confused y for n in range(10):
        return ('*')
that doesnt work so im doing the star list method. 

for loops 1c: i tried this
..................
    hashtag_list = []
    for i in range(number_of_items):
        hashtag_list.append (symbol)
    return hashtag_list
...................
but it doesnt work right for some reason


i tried this
.................
list_in_list=1
    while list_in_list < 11:
        list_in_list=list_in_list+1
        star_list = []
    for n in range(10):
        star_list.append ('*')
    return star_list
..................
but it didnt work because its not list inside list. 

I completed that exercise using the video tutorial, but i think im gonna keep it expanded instead of contracting it by referencing previous code even though its easier to read because this way it is easier to understand what the code is doing and i will probably be looking back at it when doing other code to understand how it works


loops_3
WOW, i just got the ascending number thing first try without even looking at your vids. lol. I am quite happy with myself for figuring it out so quickly and that it actually worked perfectly first try. 
OK so nvm. the debug console produces the right result but it doesnt pass the tests.py. WHY. when i press F5 i get 
0000000000
1111111111
2222222222
3333333333
4444444444
5555555555
6666666666
7777777777
8888888888
9999999999
but when i run the test it doesnt pass
Current code: 
.....................................
number = 0
    number_square = []
    for j in range (10):
        number_list = []
        for i in range(10):
            number_list.append (number)
        number_square.append(number_list)
        number = number + 1
    return number_square
.....................................
OK i think that this is maybe because it is returning integers instead of strings.
i will try fix that
NICE. ok so i literally just added the str in front of number and it worked. awesome. 

loop 5 was fairly straightfoward

Im just a bit confused as to why for loop 6 u have to do j + 1 instead of making the range 11. they output the same result...

managed to get loop 7 fairly easily to my surprise. 