import os
import shutil

NEEDS_RENAMING = False

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






subfolders = [ f.path for f in os.scandir(".") if f.is_dir() ]
for w in subfolders:
    if w == ".": continue
    if not os.path.exists(w + '/extra'): os.makedirs(w + '/extra')

    for word in ['FIRSTNAME','LASTNAME','SIGN']:
        dots_path = w + "/" + word
        times_path = w + "/" + word + "_times"
        image_path = w + "/" + word + ".png"
        if(os.path.isfile(dots_path)):
            os.remove(dots_path)
            os.remove(times_path)
            os.remove(image_path)

        else:
            print("File Not Found: ", dots_path)
            continue
    for word in ['cъешь','ещё','этих','мягких','французских',
        'булок','да','выпей','чаю']:
        dots_path = w + "/" + word
        times_path = w + "/" + word + "_times"
        image_path = w + "/" + word + ".png"
        if(os.path.isfile(dots_path)):
            shutil.move(dots_path, w + "/extra/" + word)
            shutil.move(times_path, w + "/extra/" + word + "_times")
            shutil.move(image_path, w + "/extra/" + word + ".png")

        else:
            print("File Not Found: ", dots_path)
            continue



