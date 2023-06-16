class Its:
    def __init__(self):
        self.states = [["r2qk2r/ppp2ppp/2n1p3/1B1pP3/3P1b2/2P5/P3NPPP/RNBQK2R b KQkq - 0 1",
          "r2qk2r/ppp2ppp/2n1p3/1B1pP3/3P4/2P5/P3NPPP/RNbQK2R w KQkq - 0 2",1],
          ["N4k1r/pb3ppp/1p1b1n2/2p1p3/2P5/4PN2/PP3PPP/R1B2RK1 w Qk - 0 1",
          "5k1r/pb3ppp/1N1b1n2/2p1p3/2P5/4PN2/PP3PPP/R1B2RK1 b Qk - 0 1",2],
          ["r2q3k/1p1r3n/p1p1p3/4Pp2/2NP1Pp1/2P2Q1R/PP4P1/2KR4 w q - 0 1",
          "r2q3k/1p1r3R/p1p1p3/4Pp2/2NP1Pp1/2P2Q2/PP4P1/2KR4 b q - 0 1",3],
          ["2r1r1k1/q4ppp/4b3/8/8/1Q3N1P/1P4P1/R4R1K w Q - 0 1",
           "4r1k1/5ppp/8/8/8/5N1P/1P4P1/R6K b - - 0 3",4],
           ["2rr3k/1b3ppp/3p2n1/p2N4/1p2PB2/1P6/P4QPP/q4RK1 b - - 0 1",
            "2rr3k/1b3ppp/3p2n1/p2N4/1p2PB2/1P6/P4QPP/5qK1 w - - 0 1",5]
            ]
        self.queen_desperado_remarks = ["Wow, what a move! The queen sacrifices herself for a great cause.",
                                    "Amazing! The queen is willing to risk it all to turn the tables.",
                                    "Incredible! The queen is a true desperado in this situation.",
                                    "Unbelievable! The queen refuses to go down without a fight.",
                                    "Impressive! The queen's sacrifice creates new opportunities.",
                                    "Brilliant! The queen finds a way to make the most of a desperate situation.",
                                    "Inspiring! The queen's courage in the face of adversity is remarkable.",
                                    "Outstanding! The queen is a true hero in this desperado scenario.",
                                    "Astounding! The queen's sacrifice changes the course of the game.",
                                    "Remarkable! The queen's daring move is a game-changer."]
        
        self.queen_desperado_negative_remarks = ["Unfortunately, the queen's sacrifice was missed, leading to a difficult position.",
                                    "Missing the queen's sacrifice might have been a missed opportunity to change the game.",    
                                    "The queen's sacrifice was a powerful move, which unfortunately went unnoticed.",    
                                    "Not considering the queen's sacrifice might have cost the game.",    
                                    "The queen's sacrifice was an ingenious idea that was overlooked.",    
                                    "Missing the queen's sacrifice might have led to a disadvantageous position.",    
                                    "The queen's sacrifice was a brilliant tactical idea that went unnoticed.",    
                                    "Not realizing the queen's potential sacrifice might have been a big mistake.",    
                                    "The queen's sacrifice was a clever move that unfortunately was not considered.",    
                                    "Missing the queen's sacrifice might have been a decisive blunder in this game."] 
        
        self.bishop_desperado_remarks = ["Wow, what a move! The bishop sacrifices itself for a great cause.",
                            "Amazing! The bishop is willing to risk it all to turn the tables.",    
                            "Incredible! The bishop is a true desperado in this situation.",    
                            "Unbelievable! The bishop refuses to go down without a fight.",    
                            "Impressive! The bishop's sacrifice creates new opportunities.",    
                            "Brilliant! The bishop finds a way to make the most of a desperate situation.",    
                            "Inspiring! The bishop's courage in the face of adversity is remarkable.",    
                            "Outstanding! The bishop is a true hero in this desperado scenario.",    
                            "Astounding! The bishop's sacrifice changes the course of the game.",    
                            "Remarkable! The bishop's daring move is a game-changer."]
         
        self.bishop_desperado_negative_remarks = ["Unfortunately, the bishop's sacrifice was missed, leading to a difficult position.",    
                                     "Missing the bishop's sacrifice might have been a missed opportunity to change the game.",    
                                     "The bishop's sacrifice was a powerful move, which unfortunately went unnoticed.",    
                                     "Not considering the bishop's sacrifice might have cost the game.",    
                                     "The bishop's sacrifice was an ingenious idea that was overlooked.",    
                                     "Missing the bishop's sacrifice might have led to a disadvantageous position.",    
                                     "The bishop's sacrifice was a brilliant tactical idea that went unnoticed.",    
                                     "Not realizing the bishop's potential sacrifice might have been a big mistake.",    
                                     "The bishop's sacrifice was a clever move that unfortunately was not considered.",    
                                     "Missing the bishop's sacrifice might have been a decisive blunder in this game."] 
        
        self.knight_desperado_remarks = ["What a move! The knight is willing to risk everything to turn the game around.",    
                            "Amazing! The knight's daring move is a true game-changer.",    
                            "Incredible! The knight's sacrifice is a bold and strategic decision.",    
                            "Unbelievable! The knight's move is a true desperado in this situation.",    
                            "Impressive! The knight's sacrifice creates new opportunities for victory.",    
                            "Brilliant! The knight finds a way to make the most of a desperate situation.",    
                            "Inspiring! The knight's courage in the face of adversity is remarkable.",    
                            "Outstanding! The knight is a true hero in this desperado scenario.",    
                            "Astounding! The knight's sacrifice changes the course of the game.",    
                            "Remarkable! The knight's daring move is a game-changer."]
        
        self.knight_desperado_negative_remarks = ["Unfortunately, the knight's sacrifice was missed, leading to a difficult position.",    
                                     "Missing the knight's sacrifice might have been a missed opportunity to change the game.",    
                                     "The knight's sacrifice was a powerful move, which unfortunately went unnoticed.",    
                                     "Not considering the knight's sacrifice might have cost the game.",    
                                     "The knight's sacrifice was an ingenious idea that was overlooked.",   
                                     "Missing the knight's sacrifice might have led to a disadvantageous position.",    
                                     "The knight's sacrifice was a brilliant tactical idea that went unnoticed.",    
                                     "Not realizing the knight's potential sacrifice might have been a big mistake.",    
                                     "The knight's sacrifice was a clever move that unfortunately was not considered.",    
                                     "Missing the knight's sacrifice might have been a decisive blunder in this game."]

        self.rook_desperado_remarks = ["What a move! The rook is willing to risk everything to turn the game around.",    
                          "Amazing! The rook's daring move is a true game-changer.",    
                          "Incredible! The rook's sacrifice is a bold and strategic decision.",    
                          "Unbelievable! The rook's move is a true desperado in this situation.",    
                          "Impressive! The rook's sacrifice creates new opportunities for victory.",    
                          "Brilliant! The rook finds a way to make the most of a desperate situation.",    
                          "Inspiring! The rook's courage in the face of adversity is remarkable.",    
                          "Outstanding! The rook is a true hero in this desperado scenario.",    
                          "Astounding! The rook's sacrifice changes the course of the game.",    
                          "Remarkable! The rook's daring move is a game-changer."]

        self.rook_desperado_negative_remarks = ["Unfortunately, the rook's sacrifice was missed, leading to a difficult position.",    
                                   "Missing the rook's sacrifice might have been a missed opportunity to change the game.",    
                                   "The rook's sacrifice was a powerful move, which unfortunately went unnoticed.",    
                                   "Not considering the rook's sacrifice might have cost the game.",    
                                   "The rook's sacrifice was an ingenious idea that was overlooked.",    
                                   "Missing the rook's sacrifice might have led to a disadvantageous position.",    
                                   "The rook's sacrifice was a brilliant tactical idea that went unnoticed.",    
                                   "Not realizing the rook's potential sacrifice might have been a big mistake.",    
                                   "The rook's sacrifice was a clever move that unfortunately was not considered.",    
                                   "Missing the rook's sacrifice might have been a decisive blunder in this game."] 

        self.advice_queen = ["Sometimes, to win the game, you have to lose your most powerful piece.",
                    "When your queen is blocking the way, sacrificing her might clear a path to victory.",
                    "A queen sacrifice can be a deadly surprise for your opponent.",
                    "Remember, it's not about the size of your army, but the strength of your strategy.",
                    "Don't be afraid to make bold moves, even if it means sacrificing your queen.",
                    "Sacrificing your queen can be the ultimate act of sacrifice and bravery.",
                    "In chess, as in life, sometimes you have to give up something valuable to gain something greater.",
                    "A queen sacrifice can be a powerful weapon in your arsenal, if used at the right time.",
                    "The queen is powerful, but sometimes her sacrifice can lead to a checkmate.",
                    "Sacrificing your queen can be a strategic move that throws your opponent off balance."
] 

        self.advice_rook = ["Sometimes sacrificing a rook can be the key to breaking through your opponent's defenses.",
                    "In chess, as in life, sacrifices must be made. Don't be afraid to sacrifice your rook for a greater goal.",
                    "A rook sacrifice can be a powerful surprise for your opponent.",
                    "A rook sacrifice can be a clever way to divert your opponent's attention and create opportunities.",
                    "Remember, a rook is a powerful piece, but sometimes it's worth more as a sacrifice than on the board.",
                    "Sacrificing a rook can create an open file that can be used to launch a devastating attack.",
                    "In chess, sometimes the greatest victories come from bold sacrifices. Consider sacrificing your rook if it advances your strategy.",
                    "The rook is a versatile piece that can be used for both attack and defense. Sacrificing it can create a critical imbalance in the game.",
                    "Don't underestimate the value of a well-timed rook sacrifice. It can turn the tide of a game in your favor.",
                    "A rook sacrifice can be a bold statement that shows your opponent you're not afraid to take risks to win."
] 

        self.advice_bishop = ["A bishop sacrifice can be a powerful way to open up your opponent's position.",
                    "In chess, sometimes sacrificing a bishop is necessary to gain an advantage in the endgame.",
                    "Sacrificing a bishop can be a strategic way to weaken your opponent's defenses.",
                    "A bishop sacrifice can create unexpected threats and put your opponent on the defensive.",
                    "Sometimes the value of a bishop sacrifice isn't immediately apparent, but it can pay off in the long run.",
                    "Don't be afraid to sacrifice a bishop if it creates a positional advantage or leads to a strong attack.",
                    "In chess, sacrifices are often required to break through stubborn defenses. Consider sacrificing your bishop to create opportunities.",
                    "The bishop is a powerful piece, but sacrificing it can be a creative way to create new possibilities and unsettle your opponent.",
                    "A well-timed bishop sacrifice can create an opening in your opponent's defenses that you can exploit.",
                    "Remember, a bishop sacrifice isn't just about material gain. It can also be a psychological blow to your opponent."
] 

        self.advice_knight = ["A knight sacrifice can be a bold and unexpected move that catches your opponent off guard.",
                    "In chess, sometimes sacrificing a knight is necessary to break through your opponent's defenses.",
                    "Don't underestimate the power of a well-timed knight sacrifice. It can create opportunities that were previously unavailable.",
                    "A knight sacrifice can be a strategic way to create an opening or a distraction for your other pieces.",
                    "Sometimes the value of a knight sacrifice isn't immediately apparent, but it can lead to a winning position.",
                    "Sacrificing a knight can be a creative way to disrupt your opponent's plans and gain an advantage.",
                    "In chess, bold sacrifices can be the key to victory. Don't be afraid to sacrifice your knight if it advances your strategy.",
                    "The knight is a versatile piece that can jump over obstacles and attack unexpected targets. Sacrificing it can create chaos in your opponent's camp.",
                    "A well-executed knight sacrifice can be a stunning blow that changes the course of the game.",
                    "Remember, a knight sacrifice isn't just about material gain. It can also be a way to put pressure on your opponent and force mistakes."
] 

