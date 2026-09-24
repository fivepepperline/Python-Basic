#Variabel lokal dalam python
def salam():
    pesan = "selamat sore"

    print("lokal: ", pesan)

salam()

#print(pesan) //error 

print()

#Variabel global dalam python 
pesan = "Selamat sore, how's your day?"

def salam(): 
    print("Lokal: ", pesan)

salam()

print("Global: ", pesan)

print()

#Variabel nonlokal dalam python 
def outside():
    pesan = "Lokal"

    def inner(): 

        nonlocal pesan

        pesan = "Nonlokal"
        print("Inner: ", pesan)

    inner()
    print("Outer: ",pesan)

outside()
