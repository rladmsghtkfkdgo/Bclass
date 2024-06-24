label pchess:
    ph "호오..자신있느냐?"
    pp "아 당연하죠."
    ph "짐은 마왕. 마음만 먹으면 인간따위 상대도 안되느니라."
    scene hu_chess
    $ fen =STARTING_FEN
    $ movetime =2000 
    menu:
        "Please select a difficulty lev
        "Easy":
            $ depth 
        "Medium":
            $ depth 
        "Hard":
            $ depth =
    menu:
        "Please select Player col
        "White":
            $ player_color = WHITE # this constant is defined in chess_displayable.r
        "Black":
            # board view flipped so that the player's color is at the bottom of the screen
            $ player_color = BL
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
        ph "비겼구나."
    else: # RESIGN or CHECKMATE
        $ winner = "백" if _return == WHITE else "흑"
        ph "[winner]이 이겼구나."
        if player_color is not None: # PvC
            if _return == player_color:
                ph "상을 주마.바라는것이 무엇이냐."
                menu:
                    "하루동안 [pp]의 말에 토달지 않기":
                        "헹. 건방진 인간이로다."
                    "하루동안 존댓말 쓰기":
                        show hu_sad
                        "알겠다....요.."
            else:
                ph "후후후. 어리석은 인간이여, 감히 짐을 이기려 드느냐."
                ph "벌을 줘야 하지만, 짐은 너그러운 마왕이니 기회를 주마. 나를 데리고 동물원에 가거라!"
                jump pzoo