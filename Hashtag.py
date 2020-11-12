# 1
# def Hashtag(string): #bikin fungsinya #menggunakan conditional expression untuk memisahkan jenis pertanyaan.
#     if len(string)>25: # menghitung panjang string, lalu membuat batasan yaitu len(string) lebih besar dari 25
#         print(string.title()) # apabila panjang string lebih besar dari 25 maka string akan di cetak dan menggunakan fungsi title untuk membuat setiap awal kata menjadi huruf kapital
#     elif 1<=len(string)<=25: #karena ada berbagai pertanyaan yang berbeda, maka digunakan elif untuk membuat batasan baru
#         print(string.replace(' ','')) #apabila panjang string lebih besar sama dengan 1 dan lebih kecil sama dengan 25 maka, string akan di print dan menggunakan function replace untuk menghilangkan ' ' spasi
#     elif len(string)>=140: #karena ada syarat apabila panjang string lebih dari sama dengan 140 maka saya masih menggunakan elif
#         print('false') #apabila panjang string lebih besar sama dengan 140 maka akan di print false
#     else: #penggunaan else bertujuan untuk membuat fungsi hastag kosong menjadi flase
#         print(False)

# Hashtag("Hello there how are you doing")
# Hashtag("     Hello     World   ")
# Hashtag("")