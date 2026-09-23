#String bertingkat di python 
pesan = """meletus balon hijau, DUARRR.
hatiku samgat kacau"""

print(pesan)

print() 

#Akses karakter-karakter dalam string
laptop = "lenovo"

print(laptop[0])
print(laptop[3])

print() 

#with minus indexing
laptop = "lenovo"

print(laptop[-2])
print(laptop[-4])

print()

laptop = "lenovo"

print(laptop[0:4])

print() 

#String bersifat immutable 
model = 'Opus'
version = '5'

model = model + " " + version
print(model)    # Opus 5

print() 

#Metode-metode strings dalam python
text = "Manchester United is Great"

new_text = text.replace("Manchester United", "Barcelona")

print(new_text)

print() 

#Uji keanggotaan string
print('Chat' in 'ChatGPT')       
print('Claude' not in 'ChatGPT')

print() 

#Iterate through string 
lamp = "philips"

for i in lamp:
    print(i)

print() 

#Panjang string dalam pyhton 
kasur = "central"

print(len(kasur))

print() 

#Escape sequences sequence
example = "He said, \"What's there?\""

example = 'He said, "What\'s there?"'

print(example)

print() 

#Pemformatan string (f-string)
processor = "9 Core Ultra"
perusahaan = "Intel"

text = f"{processor} adlah line up dari {perusahaan}"
