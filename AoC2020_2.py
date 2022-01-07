import time


with open('data.txt') as f:
    change = [line.rstrip() for line in f]



if __name__ == "__main__":
  replit_start_time = time.perf_counter()

total = 0
for line in change:

    i = line.split(':')
  # print(i)
    j = i[0].split(' ')
  # print(j)
    k = j + i
  # print("K is ", k)

    count = 0


    g = k[0].split()

    h = int(g[0][0])
    print("h: ", h)

    hh = int(g[0][-1:])
    print("hh: ", hh)
    for letter in k[3]:
        if letter == k[1]:
            count +=1

    print('Count:', count)

    # gg = range(h,hh+1)

    if count in range(h,hh+1):
        total += 1
        print('Total:', total)

# This doesn't work, I think, when the start and finish numbers are double digit.



# works to here

# g = k[0].split()
# # print(g)
# # print(g[0][0])
# h = int(g[0][0])
# # print(h)
# hh = int(g[0][2])
# # print(hh)
# if count in range(h,hh+1):
#   total += 1



  # need to work out how to work through all of k[3]. Can't be that hard! Yay, done that!
  # Okay, now I need to compare 'count' to k[0]. Which ... hmm. It's a string. I have to make it an int. Of for x in range(k[0])? Is that a thing? okay, no, it's not! I'm going to have to transform k[0] into ... all the numbers in the range. How?





replit_end_time = time.perf_counter()
print("Elapsed time:", replit_end_time - replit_start_time)
