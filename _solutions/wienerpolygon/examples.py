# Example 1
for c in range(2000):
    a=1.0

    for i in range(c):
        a=a/2

    x = a  # uncomment to show problem

    for i in range(c):
        a=a*2

    # Prints: number of iterations; value of a after first loop; value of a after second loop.
    print(c, x, a)  # shows problem of a becoming 2000

    #print(c , a)

print("###############################################################")

#Example 2
for c in range(2000):
    a=1.0

    for i in range(c):
        a=a/2+1.0

    x = a  # uncomment to show problem

    for i in range(c):
        a=(a-1.0)*2


    # Prints: number of iterations; value of a after first loop; value of a after second loop.
    print(c, x, a)  # shows problem of a becoming 2000

    #print(c , a)


print("###############################################################")

#Example 3
for c in range(2000):
    a=1.0

    for i in range(c):
        a=a/2+10000.0

    x = a  # uncomment to show problem

    for i in range(c):
        a=(a-10000.0)*2

    # Prints: number of iterations; value of a after first loop; value of a after second loop.
    print(c, x, a)  # shows problem of a becoming 2000

    #print(c, a)
