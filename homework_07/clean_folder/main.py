import re
import sys
import shutil
from pathlib import Path

folders = {'archives':{'ZIP', 'GZ', 'TAR'},
           'video':{'AVI', 'MP4', 'MOV', 'MKV'},
           'audio':{'MP3', 'OGG', 'WAV', 'AMR'}, 
           'documents':{'DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'XLS', 'DJVU'}, 
           'images':{'JPEG', 'PNG', 'JPG', 'SVG', 'BMP'},
           'scripts':{'SH', 'BAT'},
           'unknown':{}
           }

# make folders fo sorted files
def create_sort_dirs(main_path):         
    for folder in folders.keys():    
        if Path(main_path + '/' + folder).exists():
            continue
        else:
            Path(main_path + '/' + folder).mkdir()

# make list of all files
def make_file_list(main_path):          
    list = []
    main_path = Path(main_path)
    for el in main_path.glob('**/*'):                                   # list of files paths in all subfolders
        if el.is_file() and not (set(el.parts) & set(folders.keys())):  # select files and exclude files in sorted folders
            list.append(el)
    #print(list)    
    return list

def normalize(old_name):
    ru = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
          'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я')
    en = ('a', 'b', 'v', 'g', 'd', 'e', 'e', 'zh','z', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
          'r', 's', 't', 'u', 'f', 'h', 'ts','ch','sh','sch','\'','y','\'','e', 'ju', 'ya')
    dict = {}
    for r, e in zip(ru, en):
        dict[ord(r)] = e
        dict[ord(r.upper())] = e.upper()
    new_name = re.sub(r'[^A-Za-z0-9.!]', '_', old_name.translate(dict))  # tranlslit names and substitute symbols except ! and . to _ 
    return new_name

def copy_files(path, file):
    if path.exists():               # check if file exists in destination folder
        print(f'{file.name} exists, rewriting')
        file.replace(path)          # rewriting existing file
    else:    
        file.rename(path)           # move file to destination folder
        print(f'{file.name} relocated to {path}')
            

def sort_files(main_path, file_list):
    ext = set()
    known_ext = set()
    unknown_ext = set()
    
    for val in folders.values():           # create set of extentions 
        ext = ext.union(val)

    for item in file_list:
        file = Path(item)
        extention = file.suffix.lstrip('.').upper()     # get file extention
        if extention in ext:                            # check if file extention in extentions list
            known_ext.add(extention)                    # make set of known extentions
            for fold,val in folders.items():            # sort files by folders 
                if fold == 'archives' and extention in val:
                    shutil.unpack_archive(file, f'{main_path}/{fold}/{normalize(file.stem)}')
                    print(f'{file.name} unpacked to {main_path}/{fold}/{file.stem}')
                    file.unlink()
                elif extention in val:
                    sort_path = Path(f'{main_path}/{fold}/{normalize(file.stem)}{file.suffix}') 
                    copy_files(sort_path, file)
        else:
            unknown_ext.add(extention)                  # files without extention or with unknown extentions move to "unknown"
            sort_path = Path(f'{main_path}/unknown/{file.name}')
            copy_files(sort_path, file)
    print('{:-^60}'.format('  files was relocated successfuly!  '))
    print(f'\nKnown extentions:\n{known_ext}\n', '{:-^60}'.format(''),
          f'\nUnknown extentions:\n{unknown_ext}\n', '{:-^60}'.format(''),'\n')

#remove empty folders
def rm_empty_dirs(path,orig_path):                         
    main_path = Path(path)
    if main_path.exists() and main_path.is_dir() and not (set(main_path.parts) & set(folders.keys())):
        if any(main_path.iterdir()):             #check if folder  empty - remove, else check subfoldes 
            for dir in main_path.iterdir():  
                rm_empty_dirs(dir,orig_path)
            if path != orig_path:                        # stop when root folder
                rm_empty_dirs(main_path,orig_path)         # check folder again after checking and deleting subfolders
        else:
            main_path.rmdir()

#-------------------------------------    

def run():

    if len(sys.argv) < 2: 
        p = input('set path: ')
    else:
        p = sys.argv[1]

    while True:
        if Path(p).exists() and p != '' and not Path(p).is_file():
            select = input(f'Do you want to sort {p}? ')
            if select == 'yes' or select == 'y':
                break
            elif select == 'no' or select == 'n':
                p = input('set path: ')
        else:
            p = input('Wrong path!Enter correct path: ')


    create_sort_dirs(p)
    file_list = make_file_list(p)
    sort_files(p, file_list)

    for dir in folders.keys():      # list of sorted files in every dir
        sorted = []
        for el in Path(p + '/' + dir).iterdir():
            sorted.append(el.name)
        print('{:-^60}'.format(f'  {dir}  '),'\n', f'{sorted}')

    rm_empty_dirs(p,p)

if __name__ == '__main__':
    run()