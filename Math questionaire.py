import random


#`start_test` function which starts the test
def start_test():



# these variables are random integer generation that gives me the random numbers for each prompt.
    times1 = random.randint(0, 12)
    times2 = random.randint(0, 12)
    divi1 = random.randint(1, 30)
    div2 = random.randint(1, 10)
    addsub1 = random.randint(0, 100)
    addsub2 = random.randint(0, 100)


#gives the answers to each operator with the random generated numbers 
    answert = int(times2) * int(times1)
    answerd = int(divi1) / int(div2)
    answera = int(addsub2) + int(addsub1)
    answers = int(addsub2) - int(addsub1)

    running = True


#while loop while running is true the program will grab a prompt from the length range of `i` and `prompt` and run the for loop which tells it if `userinput` equals the `prompt`
#^ answer it will print "Correct" if not it will print "Wrong"
    while running:
        prompt = (
            ('What is {} * {} ? '.format(times1, times2), answert),
            ('What is {} ÷ {} ? '.format(divi1, div2), answerd),
            ('What is {} + {} ? '.format(addsub1, addsub2), answera),
            ('What is {} - {} ? '.format(addsub1, addsub2), answers)
        )

        for i in range(len(prompt)):
            answer, question = prompt[i]
            userinput = input(answer)

            if str(question) == userinput:
                print("Correct")
            else:
                print("Wrong")


start_test()