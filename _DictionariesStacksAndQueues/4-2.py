import queue

# Tworzenie kolejki plików do wydrukowania
files_to_print = queue.Queue()

while True:
    print('1. Add file to print')
    print('2. Print file')
    print('0. Quit')
    
    # Menu wyboru
    menu = input('Select an option: ')
    
    if menu == '1':
        # Dodawanie nowego pliku do kolejki
        file_name = input('Enter file name to print: ')
        files_to_print.put(file_name)  # Dodaj plik do kolejki
        print(f'File {file_name} added to print queue.')

    elif menu == '2':
        # Drukowanie pliku
        if not files_to_print.empty():  # Sprawdzamy, czy kolejka nie jest pusta
            file_to_print = files_to_print.get()  # Pobieramy plik z przodu kolejki
            print(f'File {file_to_print} is currently being printed. Please wait!')
        else:
            print('No files in the queue to print.')

    elif menu == '0':
        print('Exiting program...')
        break
    else:
        print('Invalid option. Please choose again.')
