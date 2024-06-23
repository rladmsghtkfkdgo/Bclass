label mk3:
    scene black
    with fade
    play music "hu_birdsound.ogg"
    #play sound "옷뒤적거리는 소리"
    ph "인간은 잠도 많구나. 오늘은 짐이 가고싶은 곳이 있다. 따라오라."
    menu:
        "얌전히 따라간다":
            ph "동물원에 갈 것 이다!"

        "싫다.오늘은 꼭 집에서 쉬어야겠다.":
            #show hu_한심하게보는휴
            ph "정말 게으른 인간이로구나..."
            pp "집에서 할 수 있는 놀이도 많아"
            ph "오냐 받아주지. 하지만 니놈이 이기지 못하면 벌을 받을 줄 알거라."
            menu:
                "무슨게임으로 겨뤄볼까?"
                
                "체스":
                    ph "호오..자신있느냐?"
                    pp "아 당연하죠."
                    ph "짐은 마왕. 마음만 먹으면 인간따위 상대도 안되느니라."
                    scene hu_chess
                    $ fen =STARTING_FEN
                    $ movetime =2000 
                    menu:
                        "Please select a difficulty level"

                        "Easy":
                            $ depth = 2

                        "Medium":
                            $ depth = 6

                        "Hard":
                            $ depth = 12

                    menu:
                        "Please select Player color"

                        "White":
                            $ player_color = WHITE # this constant is defined in chess_displayable.rpy 

                        "Black":
                            # board view flipped so that the player's color is at the bottom of the screen
                            $ player_color = BLACK

                    window hide
                    $ quick_menu = False
                
                    # avoid rolling back and losing chess game state
                    $ renpy.block_rollback()
                
                    call screen chess(fen, player_color, movetime, depth)
                
                    # avoid rolling back and entering the chess game again
                    $ renpy.block_rollback()
                
                    # restore rollback from this point on
                    $ renpy.checkpoint()
                
                    $ quick_menu = True
                    window show
                
                    if _return == DRAW:
                        e "The game ended in a draw."
                    else: # RESIGN or CHECKMATE
                        $ winner = "White" if _return == WHITE else "Black"
                        e "The winner is [winner]."
                        if player_color is not None: # PvC
                            if _return == player_color:
                                e "Congratulations, player!"
                            else:
                                e "Better luck next time, player."
                
                    return                  
                        
                "템플런":
                    ""
                "좀비죽이기":
                    ""
                "물고기 사냥":
                    ""