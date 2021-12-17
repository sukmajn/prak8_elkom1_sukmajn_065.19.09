# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 05:35:14 2021

@author: Sukma Julia Nada
"""

def mulai():
    while True:
        masuk = input("Elkom?: ")
        if masuk == "1":
            elkom1()
        elif masuk == "2":
            elkom2()
        elif masuk == "e":
            break
        else:
            print("Pilih 1 atau 2, e untuk keluar\n")


def elkom1():
    masuk = input("PROGRAM MEMUNCULKAN KARAKTER INDEKS GANJIL\nMasukkan sebuah kata: ")

    def indeks_ganjil(huruf):
        list_huruf = []
        for index in range(1, len(huruf), 2):
            list_huruf.append(huruf[index])
        return "".join(list_huruf)

    print("Karakter indeks ganjil:", indeks_ganjil(masuk), "\n")


def elkom2():
    jumlah = 0

    pertama = int(input("PROGRAM MENGHITUNG JUMLAH RANGE\nMasukkan angka pertama: "))
    kedua = int(input("Masukkan angka kedua: "))

    while pertama <= kedua:
        jumlah += pertama
        pertama += 1

    print("Jumlah range adalah:", jumlah, "\n")


if __name__ == "__main__":
    mulai()