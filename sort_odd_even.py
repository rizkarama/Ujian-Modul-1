#3
# sort_odd_even=([5, 3, 2, 8, 1, 4])
# odd numbers ascending: [1, 3,    5, ] ( Odds number in the index 0, 1, and 4)
# even numbers descending: [    8, 4,  2] (Evens number in the index 2,3, and 5)


list1=[5, 3, 2, 8, 1, 4]

def sort_odd_even(num):
    odd_numbers=[]
    even_numbers=[]
    for i in num:
        if i % 2==0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    odd_numbers.sort(reverse=False)
    even_numbers.sort(reverse=True)
    for i in range(len(odd_numbers)):
        num[odd_numbers[i]]=even_numbers[i]
    return num

print(sort_odd_even(list1))


# penjelasan
# bikin fungsinya dulu
# bikin list kosong untuk menampung hasil pemisahan dari list 1
# setelah itu menggunakkan for loop untuk memindahkan isi dari list1
# untuk memindahkannya digunakan if dan else karena ada perbedaan kondidi dimana ada odd numbers dan even numbers
# untuk even numbers digunakan if dimana apabila i habis dibagi dengan 2
# untuk odd numbers digunakkan else yang mana nilai dri odd numbers adalah bilangan ganjil dan even numbers adalah bilangan genap
# mengurutkan kedua list baru
# setelah itu digabungkan kedua list tersebut (tapi aku ga bisa ga bunginnya)

