#4

# def hollowtriangle(x): # buat fungsinya
#     for kolom in range(1,x+1): #menggunakan nested looping
#         for baris in range(1,x*2):
#             if kolom==x:
#                 print('*', end=' ')
#             elif baris+kolom==x+1 or baris-kolom==x-1:
#                 print('*', end='_')
#             else:
#                 print('_', end='_')
#         print()

# hollowtriangle(1)
# hollowtriangle(2)
# hollowtriangle(3)
# hollowtriangle(4)
# hollowtriangle(5)
# hollowtriangle(6)

# penjelasan no 4
# buat fungsinya
# menggunakan nested looping
# membuat 2 looping yaitu loopung baris dan looping kolom
# dalam looping kolom di tulis range(1,x+1) karena range itu start, stop, step. yang berarti dimulai dari 1 dan berhenti di x+1
# dalam looping baris di tulis range(1,x*2) yang berarti looping baris akan dimulai dari 1 dan selesai ketika x=x*2
# selanjutnya menggunakan conditional expression 
# dimana apabila kolom=x maka akan di print '*' dan penggunaan end=' ' bertujuan untuk mengganti format default print (pindah baris) menjadi spasi ke samping
# selanjutnya menggunakan elif dgn syarat apabila baris+kolom=x+1 or baris-kolom=x-1, penggunaan or disini adalah untuk mencetak salah satu di antara mereka
# apabila syarat elif terpenuhi maka akan mencetak '*' dan penggunaan end='_' bertujuan untuk mengganti format default print (pindah baris) menjadi _
# selanjutnya menggunakan else apabila syarat-syarat dri if dan elif tidak terpenuhi, maka akan mencetak '_' dan juga penggunaan end='_' bertujuan untuk mengganti format default print (pindah baris) menjadi _
# karena ini nasted looping maka looping akan dimulai dari kolom lalu ke baris dimana untuk mencetak baris harus melalui conditional expression, ketika baris sudah selesai baru me looping kolom lagi dst sampai syarat for looping tidak terpenuhi lagi