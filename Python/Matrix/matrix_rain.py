__author__ = 'ilya_rubinshteyn'
import random
import string
import time
import os
import sys
#import
charset1 = ("ﾏ","ｱ","ｲ","ｳ","ｴ","ｵ","ｶ","ｷ","ｸ","ｹ","ｺ","ｻ","ｼ","ｽ","ｾ","ｿ")
charset2 = (' ','!','@','%','&','.',':','#')
charset3 = ("ﾀ","ﾁ","ﾔ","ﾑ","ﾐ","ﾃ","ﾘ","ｦ","ﾜ","ﾄ","ｬ","ﾎ","ﾈ","ﾉ","ﾣ","ﾊ","ﾏ","ｱ","ｲ","ｳ","ｴ","ｵ","ｶ","ｷ","ｸ","ｹ","ｺ","ｻ","ｼ","ｽ","ｾ","ｿ","ɀ","Ɂ","ɂ","ŧ","Ϣ","ϣ","ϯ","ϰ","Ϭ","ϭ","Ϯ","ϯ",",ϰ","༣","༤","༥","༦","༧","༩","༪","༫","༬","༭","༯","༰","༱","༲","༳","༶")

def gen(y):

    while True:
        a = random.choice(charset2)
        b = random.choice(charset3)
        c = random.choice(charset1)
        full_pool = random.choice(string.ascii_letters+string.digits*2+b*50+a+c)
        #print('%s'%full_pool)
        sys.stdout.write("\x1b7\x1b[2%d;2%df%s\x1b8"%random.choice(full_pool))
        sys.stdout.flush()
        time.sleep(0.1)



if __name__ == '__main__':
    y = 1
    os.system('clear')

    gen(y)
