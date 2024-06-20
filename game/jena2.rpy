label j_ho:
    show bg j_room1
    show j_labe_da
    " "
    hide j_labe_da
    menu:
        "지금 일어날까?":
            jump j_mu
        "아냐 좀만 더 자자":
            jump j_we
    label j_mu:
        "오늘은 뭐할까?"
        menu:
            "독서는 마음의 양식이지":
                jump j_qw
            "오랜만에 게임이나 할까?":
                jump j_er
            "여유로운 아침을 즐기자":
                jump j_tr
        label j_qw:
            jw"오랜만에 해포리터 읽을까?"
            "시리즈 책을 읽다보니 시간이 빨리 지나갔다."
            jw"역시 해포리터는 명작이야"
            jw"지금 몇시지?"
            jw"벌써 3시야?"
            jw"재밌어서 배고픈줄도 몰랐네"
            jw"배고픈데 뭐먹지?"
            jump j_yu
        label j_er:
            jw"좀만 할까?"
            "정신을 차려보니 어느덧 3시가 되었다."
            jw"지금 몇시지?"
            jw"벌써 3시야?"
            jw"재밌어서 배고픈줄도 몰랐네"
            jw"배고픈데 뭐먹지?"
            jump j_yu
        label j_tr:
            jw"여유로운 아침이네"
            jw"좀 더 이대로 있을까.."
            "포근한 날씨에 잠에 들었다."
            jw"으음...얼마나 잔거지..?"
            jw"벌써 4시네"
            jw"일찍 일어난 보람이 없네"
            jw"뭐, 잘 잤으니 됐나~"
            jw"그나저나 묘하게 배고프네"
            jw"뭐라도 먹을까?"
            jump j_yu
    label j_we:
        jw "좀만 더 자자"
        "한참을 자고나니 저절로 눈이 뜨였다."
        jw "으음... 몇시지?"
        jw "벌써 3시네.."
        jw "최근 잠이 부족하긴 했지"
        jw "음.. 배고픈데"
        jw "뭐라도 먹을까?"
        jump j_yu
        label j_yu:
            jw"집에서 먹을까, 밖에서 먹을까 고민되네"
            menu:
                "집에서 먹자":
                    jump j_io
                "밖에서 먹자":
                    jump j_ui
            label j_ui:
                scene bg j_room_bo
                "집을 나선다."
                scene bg j_room_ca
                jw"어,"
                jw"고양이다!"
                jw"배고픈가..?"
                jw"뭐라도 사올까.."
                hide bg j_room_ca
                show bg j_room_co
                show j_co_1 at left
                jco "안녕하세요, Gu입니다."
                jw "안녕하세요."
                jw "흠.. 츄르면 되려나?"
                jw "계산해 주세요."
                play sound "j_Beep.ogg"
                jco "(삑)"
                play sound "j_dodo.ogg"
                jco "3800원입니다."
                jco "감사합니다, 또 오세요"
                jw "안녕히 계세요~"
                hide j_co_1
                hide bg j_room_co
                show bg j_room_ca
                jw"고양이.. 아직 있으려나?"
                jw"아, 있다!"
                jw"어, 고양이랑..."
                show j_su1 at right
                jw"옆집 사람..??"
                jw"어쩌지?"
                menu:
                    "그냥 지나가자":
                        jump j_op
                    "어차피 옆집 사람인데.. 인사하고 지내자":
                        jump j_pa
                label j_op:
                    "츄르를 주머니에 넣고 지나갔다."
                    $u = -20
                    jump j_sd
                label j_pa:
                    jw"저.. 안녕하세요?"
                    jd"아..안녕하세요."
                    jw"고양이.. 좋아하세요?"
                    hide j_su1 
                    show j_su2 at right
                    jd"네, 좋아해요."
                    jd"고양이 좋아하세요?"
                    jw" 네, 좋아해요."
                    jw"아, 방금 츄르 사왔는데 줘보실래요?"
                    show j_su4 at right
                    jd"어...!"
                    hide j_su4
                    show j_su3 at right
                    jd"좋아요!"
                    jw"여기요."
                    hide j_su3
                    show j_su2 at right
                    jw"그러고보니 이름이 어떻게 되세요?"
                    hide j_su2
                    show j_su3 at right
                    js"서윤이에요, 서서윤."
                    js"이름이 어떻게 되세요?"
                    $jplayer_name = renpy.input("아! 제 이름은")
                    jp "아! 제 이름은 [jplayer_name](이)예요. "
                    hide j_su3
                    show j_su2 at right
                    jp "앞으로 인사하고 지내도 괜찮을까요?"
                    hide j_su2
                    show j_su3 at right
                    js "좋아요"
                    $u = +20
                    
                    "그 후, 서윤을 배웅했다."
                    jump j_sd
                    label j_sd:
                        jw "이제 편의점 가야지."
                        show bg j_room_co
                        show j_co_1 at left
                        jco "안녕하세요, Gu입니다."
                        jw "안녕하세요."
                        jw "흠.. 뭐 먹지?"
                        menu:
                            "따끈한 라면 먹자":
                                jump j_df
                            "한국인은 밥심이지, 도시락 먹자":
                                jump j_fg
                            "뭘 고민해, 둘 다 먹자":
                                jump j_gh
                        label j_df:
                            jw "계산해 주세요."
                            play sound "j_Beep.ogg"
                            jco "(삑)"
                            play sound "j_dodo.ogg"
                            jco "1500원입니다."
                            jco "감사합니다."
                            jump j_hj
                        label j_fg:
                            jw "계산해 주세요."
                            play sound "j_Beep.ogg"
                            jco "(삑)"
                            play sound "j_dodo.ogg"
                            jco "2300원입니다."
                            jco "감사합니다."
                            jump j_hj
                        label j_gh:
                            jw "계산해 주세요."
                            play sound "j_Beep.ogg"
                            jco "(삑)"
                            play sound "j_dodo.ogg"
                            jco "3800원입니다."
                            jco "감사합니다."
                            jump j_hj
                        label j_hj:
                            "ji"
                            