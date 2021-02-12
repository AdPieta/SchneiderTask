# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 17:50:46 2021

@author: Pieta
"""

board = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

    
#Mamy teraz listę która pozwoli nam zapisywac elementy gry (O i X)
#Teraz pokazmy ja w ladny, graficzny sposob

def wspolrzedne():
    print(str(1) + '|' + str(2) + '|' + str(3))
    print('-+-+-')
    print(str(4) + '|' + str(5) + '|' + str(6))
    print('-+-+-')
    print(str(7) + '|' + str(8) + '|' + str(9))
    
wspolrzedne()    
    
def print_board (board):
    print(board['1'] + ' | ' + board['2'] + '| ' + board['3'])
    print('--------')
    print(board['4'] + ' | ' + board['5'] + '| ' + board['6'])
    print('--------')
    print(board['7'] + ' | ' + board['8'] + '| ' + board['9'])
  
print_board(board)

#sama gra może być jako funkcja

def TicTacToe():
    
    #Wykonywanie ruchow
    ruch = 'O'
    count = 0
    wspolrzedne() 
    for i in range(10):
        
        print_board(board)
        print("Ruch " + ruch + ", wybierz wspolrzedna")
        
        move = input()
        
        if board[move] == ' ':
            board[move] = ruch
            count += 1
        else:
            print("To pole jest zajete, wybierz inne")
            continue
        
        
        #Sprawdzanie czy wygranie
        #nie da sie wygrac szybciej niz w 5 ruchach
        
        if count >= 5:
            #gorny rzad
            if board['1'] == board['2'] == board['3'] != ' ':
                print_board(board)
                print('Koniec gry, wygrana ' + ruch)
                break
            #srodkowy rzad
            elif board['4'] == board['5'] == board['6'] != ' ':
                print_board(board)
                print('Koniec gry, wygrana ' + ruch)
                break
            #dolny rzad
            elif board['7'] == board['8'] == board['9'] != ' ':
                print_board(board)
                print('Koniec gry, wygrana ' + ruch)
                break
            #lewa kolumna
            elif board['1'] == board['4'] == board['7'] != ' ':
                print_board(board)
                print('Koniec gry, wygrana ' + ruch)
                break
            #srodkowa kolumna
            elif board['2'] == board['5'] == board['8'] != ' ':
                print_board(board)
                print('Koniec gry, wygrana ' + ruch)
                break
            #prawa kolumna
            elif board['3'] == board['6'] == board['9'] != ' ':
                print_board(board)
                print('Koniec gry, wygrana ' + ruch)
                break
            #glowna diagonala (lewa gora -> prawy dol)
            elif board['1'] == board['5'] == board['9'] != ' ':
                print_board(board)
                print('Koniec gry, wygrana ' + ruch)
                break
            #druga diagonala (prawa gora -> lewy dol)
            elif board['3'] == board['5'] == board['7'] != ' ':
                print_board(board)
                print('Koniec gry, wygrana ' + ruch)
                break

        #Ale mamy dwoch graczy, drugi jest krzyzykiem
                #zmiana gracza co ruch            
        #Warunek dwoch graczy musi byc na koncu, bo inaczej pokazuje nam
        #przegranego jako zwyciezce
        if ruch == 'O':
            ruch = 'X'
        else:
            ruch ='O'

TicTacToe()


