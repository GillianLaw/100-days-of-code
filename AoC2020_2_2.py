import time


with open('data.txt') as f:
    change = [line.rstrip() for line in f]



if __name__ == "__main__":
  replit_start_time = time.perf_counter()

total = 0
for line in change:
    i = line.split(':')
    j = i[0].split(' ')
    k = j + i

    count = 0

    g = k[0].split()
    if g[0][1] == '-':
        h = int(g[0][0])
    else:
        h = int(g[0][0:2])

    if g[0][-2:-1] == '-':
        hh = int(g[0][-1:])
    else:
        hh = int(g[0][-2:])

    # if k[1] == k[3][h] and k[1] == k[3][hh]:
    #     pass
    if k[1] == k[3][h] or k[1] == k[3][hh]:
        count += 1
    if k[1] == k[3][h] and k[1] == k[3][hh]:
        count -= 1



    # print('Count:', count)


    if count == 1:
        total += 1
        print('Total:', total)






replit_end_time = time.perf_counter()
print("Elapsed time:", replit_end_time - replit_start_time)
