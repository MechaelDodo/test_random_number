import time, random, pickle
#RANDOM_NUM = {'ramdom_num': 0}

if __name__=='__main__':
    #with ('data_random.pkl', 'wb') as db:
    #    while True:
    #        RANDOM_NUM['ramdom_num'] = random.randint(0, 100)
    #        print(RANDOM_NUM['ramdom_num'])
    #        pickle.dump(RANDOM_NUM, db)
    #        time.sleep(5)
    while True:
        #db = open('data_random.pkl', 'wb')
        #RANDOM_NUM['ramdom_num'] = random.randint(0, 100)
        #print(RANDOM_NUM['ramdom_num'])
        #pickle.dump(RANDOM_NUM, db)
        #time.sleep(5)
        #db.close()

        #db = open('E:/allprojects/testnum/testproject/testapp/data_random.pkl', 'rb')
        #r = pickle.load(db)
        #print(r)
        file = open('data.txt', 'w')
        file.seek(0)
        RANDOM_NUM = random.randint(0, 100)
        file.write('%d'%RANDOM_NUM)
        file.close()
        time.sleep(5)
        


        
    
