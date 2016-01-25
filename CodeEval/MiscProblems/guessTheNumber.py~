"""Given a range, and a sequence of instructions: "Higher", "Lower",
"Yay", guess the right number. Arrive at the number in logs(N) guesses"""

filename = "test_guessthenumber.txt"

with open(filename) as f:
    for test in f:
        test = test.strip()
        upper = int(test.split(" ")[0]) 
        lower = 0
        guess = upper/2
        instructions = test.split(" ")[1:]
        print instructions
        for ins in instructions:
            print guess, ins
            if(ins == "Higher"):
                lower = guess
                guess = guess + (upper - lower)/2
            if(ins == "Lower"):
                upper = guess
                guess = guess - (upper - lower)/2
            if(ins == "Yay!"):
                print guess
                break
