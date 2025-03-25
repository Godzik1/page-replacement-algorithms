import random

odp_page_faults = 0.0

for _ in range(100):
    #Generowanie listy referencji stron (losowych liczb całkowitych od 0 do 20)
    page_reference = [random.randint(0 , 20) for i in range(100)]

    capacity = 3 #Pojemność pamięci

    data = [] #Lista przechowująca aktualnie załadowane strony
    page_faults = 0 #Licznik błędów strony

    for i in range(len(page_reference)):

        if page_reference[i] in data: #Sprawdzenie, czy strona jest już w pamięci
            data.remove(page_reference[i]) #Usunięcie istniejącej strony (LRU)

        else:
            if capacity == len(data): #Jeśli pamięć jest pełna, usuń najstarszą stronę (pierwsza w liście)
                x = data[0]
                data.remove(x)

            page_faults += 1 #Zwiększanie licznika błędów strony
        data.append(page_reference[i]) #Dodanie nowej strony do pamięci


    #print(page_faults) #Wyświetlenie liczby błędów strony

    odp_page_faults += page_faults #Dodawanie do sumy, aby na koniec obliczyć średnią średniej liczby błędów

print(odp_page_faults/100) #Obliczanie średniej liczby błędów