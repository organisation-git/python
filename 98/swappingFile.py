#!/bin/env python3

def main():
    filename1 = input("first file ")
    filename2 = input("first file ")

    file1 = open(filename1, 'r')
    file2 = open(filename2, 'r')


    data_a = file1.read()
    data_b = file2.read()


    file1 = open(filename1, 'w')
    file2 = open(filename2, 'w')

    file2.write(data_a)
    file1.write(data_b)


main()
