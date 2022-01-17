# coding
import os, shutil, time, datetime, glob

 
path_to_watch = "C:/Users/denni/Desktop/FolderA/"
path_for_take = "C:/Users/denni/Desktop/FolderB/"
before = dict([(f, 0) for f in os.listdir(path_to_watch)])
while 1:
    time.sleep(3)
    after = dict([(f, 0) for f in os.listdir(path_to_watch)])
    if len(os.listdir(path_to_watch)) == len(os.listdir(path_for_take)):
        print('No new files.')
    else:
        print('New file:')
        files_in_watch_type = [i for i in os.listdir(path_to_watch)]
        files_in_watch = [i[0:-4] for i in files_in_watch_type]
        files_in_take_type = [i for i in os.listdir(path_for_take)]
        files_in_take = [i[0:-4] for i in os.listdir(path_for_take)]
        el_not_in = sorted(list(set(files_in_take) ^ set(files_in_watch)), reverse=False)
        if len(el_not_in) > 1:
            
            # ----------if cuple files----------
            if os.path.getsize(path_to_watch + el_not_in[-1] + '.txt') == 0:
                print('Copy all...')
                for i in el_not_in[0:-1]:
                    full_path_name_without_last = path_to_watch + i + '.txt'
                    shutil.copy(full_path_name_without_last, path_for_take)
                    full_path_name_all_one_coding = path_for_take + i + '.txt'
                    
        #-----------if only one new file------------
        elif len(el_not_in) == 1:
            print('There is a new file, check:')
            el_with_type = path_to_watch + el_not_in[-1] + '.txt'
            #------------------if wait---------------------
            if os.path.getsize(el_with_type) == 0:
                print('There is an undownloaded file, we are waiting for...')
            #------------------if new ----------------------
            elif os.path.getsize(el_with_type) != 0:
                print('There is a new file, I start copying...')
                full_path_name_one = path_to_watch + el_not_in[-1]+'.txt'
                shutil.copy(full_path_name_one, path_for_take)
                full_path_name_one_coding = path_for_take + el_not_in[-1]+'.txt'
                print('Ready.')
