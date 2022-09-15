import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

NEEDS_RENAMING = True

WORDS=['А','а','Б','б','В','в','Г','г','Д','д','Е','е','Ё','ё','Ж','ж','З','з',
        'И','и','Й','й','К','к','Л','л','М','м','Н','н','О','о','П','п','Р','р',
        'С','с','Т','т','У','у','Ф','ф','Х','х','Ц','ц','Ч','ч','Ш','ш','Щ','щ',
        'Ъ','ъ','Ы','ы','Ь','ь','Э','э','Ю','ю','Я','я','0','1','2','3','4','5',
        '6','7','8','9','cъешь','ещё','этих','мягких','французских',
        'булок','да','выпей','чаю','FIRSTNAME','LASTNAME','SIGN']

SYMBOLS = ['А','а','Б','б','В','в','Г','г','Д','д','Е','е','Ё','ё','Ж','ж','З','з',
        'И','и','Й','й','К','к','Л','л','М','м','Н','н','О','о','П','п','Р','р',
        'С','с','Т','т','У','у','Ф','ф','Х','х','Ц','ц','Ч','ч','Ш','ш','Щ','щ',
        'Ъ','ъ','Ы','ы','Ь','ь','Э','э','Ю','ю','Я','я','0','1','2','3','4','5',
        '6','7','8','9']

MNIST_IMAGE_SIZE = 28


def trapez(y,y0,w):
    return np.clip(np.minimum(y+1+w/2-y0, -y+1+w/2+y0),0,1)

def weighted_line(r0, c0, r1, c1, w, rmin=0, rmax=np.inf):
    # The algorithm below works fine if c1 >= c0 and c1-c0 >= abs(r1-r0).
    # If either of these cases are violated, do some switches.
    if abs(c1-c0) < abs(r1-r0):
        # Switch x and y, and switch again when returning.
        xx, yy, val = weighted_line(c0, r0, c1, r1, w, rmin=rmin, rmax=rmax)
        return (yy, xx, val)

    # At this point we know that the distance in columns (x) is greater
    # than that in rows (y). Possibly one more switch if c0 > c1.
    if c0 > c1:
        return weighted_line(r1, c1, r0, c0, w, rmin=rmin, rmax=rmax)


    # The following is now always < 1 in abs
    slope = (r1-r0) / (c1-c0)
    if c1 == c0: slope = 0
    # Adjust weight by the slope
    w *= np.sqrt(1+np.abs(slope)) / 2

    # We write y as a function of x, because the slope is always <= 1
    # (in absolute value)
    x = np.arange(c0, c1+1, dtype=float)
    if c1 == c0: y = np.arange(r0, r1+1, dtype=float) # x * slope + (c1*r0-c0*r1)
    else: y = x * slope + (c1*r0-c0*r1) / (c1-c0)

    # Now instead of 2 values for y, we have 2*np.ceil(w/2).
    # All values are 1 except the upmost and bottommost.
    thickness = np.ceil(w/2)
    yy = (np.floor(y).reshape(-1,1) + np.arange(-thickness-1,thickness+2).reshape(1,-1))
    xx = np.repeat(x, yy.shape[1])

    vals = trapez(yy, y.reshape(-1,1), w).flatten()

    yy = yy.flatten()

    # Exclude useless parts and those outside of the interval
    # to avoid parts outside of the picture
    mask = np.logical_and.reduce((yy >= rmin, yy < rmax, vals > 0))

    return (yy[mask].astype(int), xx[mask].astype(int), vals[mask])

def connect_points(x, y, img, times):
    times_mean = times[1:].mean()
    for i in range(1, len(x)):
        #  number "3" here is experimentally derived
        if times[i] > 3 * times_mean: continue
        ys, xs, vals = weighted_line(x[i-1], y[i-1], x[i], y[i], w=2, rmin=0, rmax=27)
        img[xs, MNIST_IMAGE_SIZE - 1 - ys] = vals
    return img



writers = list()
subfolders = [ f.path for f in os.scandir("../new") if f.is_dir() ]

for w in subfolders:
    if w == ".": continue
    writer_name = ''.join([i for i in w if not i.isdigit()])
    if writer_name not in writers: writers.append(writer_name)
    print(w)
    for i in tqdm(range(len(WORDS))):
        data = []
        times = []
        dots_path = w + "/" + WORDS[i]
        times_path = w + "/" + WORDS[i] + "_times"
        if(os.path.isfile(dots_path)):
            with open(w + "/" + WORDS[i], 'r', newline='') as f:
                r = csv.reader(f, delimiter=',')

                data = list(map(int, list(r)[0]))
        else:
            print("File Not Found: ", dots_path)
            continue
        if(os.path.isfile(times_path)):
            with open(times_path, 'r', newline='') as f:
                r = csv.reader(f, delimiter=',')
                times = np.array(list(map(int, list(r)[0])))
        else:
            print("File Not Found: ", times_path)
            continue


        x = np.array(data[::2])
        y = np.array(data[1::2])
        if len(x) == 0 or len(y) == 0: continue
        min_corner = [x.min(), y.min()]

        x = x - min_corner[0]
        y = y - min_corner[1]

        x = np.rint((MNIST_IMAGE_SIZE - 1) * x / x.max()).astype(int)
        y = np.rint((MNIST_IMAGE_SIZE - 1) * y / y.max()).astype(int)

        max_corner = [x.max(), y.max()]
        min_corner = [0, 0]


        connected_dots = np.zeros((MNIST_IMAGE_SIZE, MNIST_IMAGE_SIZE), dtype=float)
        scattered_dots = np.zeros((MNIST_IMAGE_SIZE, MNIST_IMAGE_SIZE), dtype=int)
        for j in range(len(x)):
            scattered_dots[x[j], y[j]] = 1
        scattered_dots = np.rot90(scattered_dots)

        # plt.imshow(scattered_dots)
        # plt.title("Scattered " + w + "/" + WORDS[i])
        # plt.show()

        connected_dots = connect_points(x, y, connected_dots, times)
        connected_dots = np.rot90(connected_dots)
        connected_dots = np.rot90(connected_dots)

        # plt.imshow(connected_dots)
        # plt.title("Connected " + w + "/" + WORDS[i])
        # plt.show()



        if WORDS[i] in SYMBOLS:
            mnist_path = w + "/mnist-like/" + WORDS[i] + ".csv"
            os.makedirs(os.path.dirname(mnist_path), exist_ok=True)
            with open(mnist_path, 'w', newline='') as f:
                np.savetxt(mnist_path, connected_dots, delimiter=",")

    if NEEDS_RENAMING:
        attempt = ''.join([c for c in w if c.isdigit()])
        attempt = int(attempt) if len(attempt) > 0 else 0
        os.rename(w, "../new/w_" + str(9 + writers.index(writer_name)) + "_" + str(attempt))
