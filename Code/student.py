import sys
sys.path.insert(0, "D://Stockfish")
import time
import os
import random
import math
from stockfish import Stockfish
stockfish=Stockfish("D://Stockfish//stockfish-11-win//Windows//stockfish_20011801_x64.exe")
def getMinMaxState(stateSet,n): # To get min state greater than n
    mi = 2**60
    ma = 0
    smi = stateSet[0]
    sma = stateSet[0]
    for state in stateSet:
        if(state[2] < mi and state[2] > n):
            mi = state[2]
            smi = state
        if(state[2]>ma):
            ma = state[2]
            sma = state

        
    return [mi,smi,ma,sma]
def getMinState(stateSet):# Get min unsolved state ie state with heuristic != -1
    mi = 2 ** 60
    smi = None
    for state in stateSet:
        if(state[2] < mi and state[2] != -1):
            mi = state[2]
            smi = state
    return smi

class Student:
    def __init__(self):
        states = None
    

        
    def play(self,it):
        print("Welcome to your desperado lesson!")
        solved = 1
        x = 0
        currentGame = getMinMaxState(it.states,x-1)[1] # Initially get the first game
        # currentGame = states[3]
        while True:
            stockfish.set_fen_position(currentGame[0])
            while (stockfish.get_fen_position() != currentGame[1]):
                if x == 1:
                    stockfish.make_moves_from_current_position([stockfish.get_best_move()])
                
                print(stockfish.get_board_visual())
                piece = str(stockfish.get_what_is_on_square(stockfish.get_best_move()[:2])) # Getting the piece to be moved in the ideal move
                n = piece.index('_')
                n += 1 # Getting the initial letter of the piece to be moved 
                ch = piece[n]
                advice = ""
                positiveFeedback = ""
                negativeFeedback = ""
                if ch == 'Q':
                    advice = it.advice_queen[math.floor(random.random() * 10)]
                    positiveFeedback = it.queen_desperado_remarks[math.floor(random.random() * 10)]
                    negativeFeedback = it.queen_desperado_negative_remarks[math.floor(random.random() * 10)]
                elif ch == 'R':
                    advice = it.advice_rook[math.floor(random.random() * 10)]
                    positiveFeedback = it.rook_desperado_remarks[math.floor(random.random() * 10)]
                    negativeFeedback = it.rook_desperado_negative_remarks[math.floor(random.random() * 10)]
                elif ch == 'K':
                    advice = it.advice_knight[math.floor(random.random() * 10)]
                    positiveFeedback = it.knight_desperado_remarks[math.floor(random.random() * 10)]
                    negativeFeedback = it.knight_desperado_negative_remarks[math.floor(random.random() * 10)]
                else:
                    advice = it.advice_bishop[math.floor(random.random() * 10)]
                    positiveFeedback = it.bishop_desperado_remarks[math.floor(random.random() * 10)]
                    negativeFeedback = it.bishop_desperado_negative_remarks[math.floor(random.random() * 10)]
                #print([state[2] for state in it.states]) # Not a part of final code. Just to observe changes in heuristic value
                print(f"Here is a piece of advice: {advice}")
                print("Make your move")
                move = input()
                best_move = stockfish.get_best_move()
                if move == best_move:
                    print(positiveFeedback)
                    stockfish.make_moves_from_current_position([move])
                    #print(stockfish.get_fen_position()) # Not a part of final code
                    #print(currentGame[1]) # Not a part of final code
                    print(stockfish.get_board_visual())
                    x = 1


                    continue
                else:
                    x = 0
                    print(negativeFeedback)
                    tryAgain = input("Do you wish to try again Y/N?")
                    if tryAgain == 'Y':
                        continue
                    else:
                        solved = 0
                        difficulty = int(input("On a scale of 1 to 3, how difficult do you feel is the puzzle?"))
                        currentGame[2] += difficulty # Depending on the feedback of user, the priorty is changed
                        break
            x = 0
            if solved == 1:
                currentGame[2] = -1 # Setting it to be the easiest as it is solved
                print(stockfish.get_board_visual())
            anotherGame = input("Do you wish to play another game? Y/N")
            if anotherGame == 'Y':
                currentGame = getMinState(it.states)
                continue
            else:
                print("Thank You For Playing")
                break




