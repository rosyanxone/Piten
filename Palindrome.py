from time import sleep

def inputKata():
    contohKata = input("Berikan contoh kata : ")
    return contohKata

def palindrome(contohKata):
    kataDibalik = contohKata[::-1]
    return kataDibalik

def cekPalindrome(kataDibalik, contohKata):
    if kataDibalik == contohKata:
        return "Kata yang diberikan merupakan kata Palindrome\n"
    else:
        return "Kata yang diberikan bukan kata Palindrome\n"

def main():
    contohKata = inputKata()
    kataDibalik = palindrome(contohKata)
    hasilCek = cekPalindrome(kataDibalik, contohKata)
    print(hasilCek)
    sleep(0)

main()