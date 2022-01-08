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
    # print("G: ", g)

    if g[0][1] == '-':
        h = int(g[0][0])
    else:
        h = int(g[0][0:2])
    print("h: ", h)

    if g[0][-2:-1] == '-':
        hh = int(g[0][-1:])
    else:
        hh = int(g[0][-2:])
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





replit_end_time = time.perf_counter()
print("Elapsed time:", replit_end_time - replit_start_time)
