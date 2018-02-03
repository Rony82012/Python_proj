import os

def rename_file():
    file_list = os.listdir(r"/Users/varunramarajudandu/Downloads/Prank")
    print(file_list[1:])
    saved_path = os.getcwd()
    print("Current Working directory is " + saved_path)
    os.chdir(r"/Users/varunramarajudandu/Downloads/Prank")

    for file_name in file_list[1:]:
        #translation_table = str.maketrans("0123456789", "          ", "0123456789")
        os.rename(file_name, file_name.translate(str.maketrans("","","0123456789")))

    os.chdir(saved_path)


rename_file()