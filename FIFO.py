import random

odp_page_faults = 0.0


for _ in range(100):
    #Generowanie listy referencji stron (losowych liczb całkowitych od 0 do 20)
    page_reference = [random.randint(0 , 20) for i in range(100)]

    capacity = 3 #Pojemność pamięci

    data = [] #Lista przechowująca aktualnie załadowane strony
    page_faults = 0 #Licznik błędów strony
    index_remove_page = 0 #Index którą stronę mamy usunąć

    for i in range(len(page_reference)):

        if page_reference[i] in data: #Sprawdzenie, czy strona jest już w pamięci
            continue #Jeśli strona jest w pamięci, przechodzimy do następnej iteracji
        else:
            if len(data) == capacity: #Jeśli strona nie jest w pamięci, a pamięć jest pełna, usuwamy najstarszą stronę
                data.pop(index_remove_page % capacity)

        data.insert(index_remove_page % capacity , page_reference[i]) #Dodajemy nową stronę do pamięci na odpowiednie miejsce

        index_remove_page += 1 #Zwiększamy licznik, aby odpowiednią stronę usunąć
        page_faults += 1 #Zwiększanie licznika błędów strony


    #print(page_faults) #Wyświetlenie liczby błędów strony

    odp_page_faults += page_faults #Dodawanie do sumy, aby na koniec obliczyć średnią średniej liczby błędów


print(odp_page_faults/100) #Obliczanie średniej liczby błędów
