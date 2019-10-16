import math

num_ways = int(input("Avg num. ways to write a processing step:"))
num_ps = int(input("Number of processing steps:"))
num_re = int(input("Number of re-orderable processing steps:"))
num_ways_prog = int(math.pow(num_ways, num_ps))
num_re_prog = num_ways_prog * math.factorial (num_re)
num_odds = int(math.pow(num_re_prog, 2))
print ("There are about",num_ways_prog,"ways to write the program with no reordering.") 
print ("There are about",num_re_prog, "ways to write the program if 3 processing steps can be reordered.")
print ("The odds that your program is coincidentally identical to another program is about 1 in",num_odds)

num_odds_consec_flush = int(math.log(num_odds)/math.log(649739))
print("That is about the same as",num_odds_consec_flush,"consecutive royal flushes in poker.")

num_ways2 = int(input("Avg num. ways to write a processing step:"))
num_ps2 = int(input("Number of processing steps:"))
num_re2 = int(input("Number of re-orderable processing steps:"))
num_ways_prog2 = int(math.pow(num_ways2, num_ps2))
num_re_prog2 = num_ways_prog2 * math.factorial (num_re2)
num_odds2 = int(math.pow(num_re_prog2, 2))
print ("There are about",num_ways_prog2,"ways to write the program with no reordering.") 
print ("There are about",num_re_prog2, "ways to write the program if 3 processing steps can be reordered.")
num_odds = num_odds * num_odds2
print ("The odds that your first and second programs are coincidentally identical is about 1 in",num_odds)
num_odds_consec_flush = int(math.log(num_odds)/math.log(649739))
print("That is about the same as",num_odds_consec_flush,"consecutive royal flushes in poker.")
