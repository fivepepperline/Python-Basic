#Contoh fungsi rekrusif 
def faktorial(x):

    if x == 1:
        return 1
    else: 
        return(x * faktorial(x-1))

angka = int(input("Angka yang ingin difaktorialkan: "))
print("faktorial dari",angka, "adalah:", faktorial(angka))
