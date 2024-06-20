# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"


# 여기에서부터 게임이 시작합니다.
label jn:
    scene bg j_room1

    play sound "j_dodo.ogg"
    "유튜브에서 알람이 왔다"
    show j_hand
    show j_alm
    " "
    hide j_alm
    show j_utb
    jw"아, 유튜브 알람이네"
    jw"이왕 들어온거 유튜브나 볼까"
    hide j_utb
    "뭐 볼까?"

    menu:
        "영상 보자":
            "(유피아의 영상이 뜬다)"
            jump j_fir
        "숏츠 보자":
            show j_upi_1
            jump j_fir
    label j_fir:
        jw "요즘 이 사람 많이 보이네"
        hide j_upi_1
        show j_labe_2
        " "
        hide j_hand
        hide j_labe_2

        jw"유튜브만 2시간 봤네, 슬 다른거 할까?"
    

    menu:
        "밥을 먹는다":
            jump j_bab
        "운동을 한다":
            jump j_muc
        "유튜브를 마저 본다":
            jump j_utb
            

    label j_bab:
        "마침 밥 시간이네. 뭐 먹지?"
        menu:
            "귀찮지만 만들어먹자":
                jump j_na

            "귀찮은데 뭘 만들어. 시켜먹자":
                jump j_two
            
        label j_two:
                jw"오랜만에 치킨 먹을까.."
                "(뚜르르)"
                jw"네, 여기 00아파트 00동...."
                show j_labe_za
                " "
                hide j_labe_za
                "(띵동)"
                jw"오 왔다!"
                scene bg j_room_bo
                "(문을 연다)"
                show j_su1 at right
                
                jw ".....!"
                scene bg j_room1
                hide su1
                "놀라서 인사도 잊어버린 채 다시 들어왔다."
                $u = -10
    
                jw "아..깜짝이야.."
                jw "치킨이나 먹어야지.."
                "그 후, 먹은 것을 대충 치우고 잠들었다."
                jump j_ho


        label j_na:
            "(냉장고를 연다)/n
            냉장고에 뭐가 있더라"
            jw "흠.. 뭐가 없네, 마트 다녀와야겠다."
            jump j_vip
    label j_muc:
        jw "흠...오랜만에 운동이나 할까?"
        jw "무슨 운동하지.."
        jw "오랜만의 운동인데 헬스장 가야겠다."
        jump j_vip

    label j_utb:
        jw "아니다."
        jw "보는 김에 마저 볼까?"
        show j_labe_3
        " "
        hide j_labe_3
        jw "벌써 시간이.."
        jw "저녁 먹어야겠다."
        jw "배달시켜 먹어야지"
        jump j_two

    label j_vip:
        scene bg j_room_bo
        "집을 나선다"
        
        show j_su1 at right
        "어, 옆집사람이네.."
        "어쩌지?"
        menu:
            "이웃인데 인사는 하고 지내야지. 가볍게 목례하고 지나간다.":
                jump j_hi
            "갑작스러운 만남에 당황스러워한다.":
                jump j_by
        label j_hi:
            hide j_su1
            show j_su2 at right
            "(꾸벅)"
            "옆집 사람도 목례하며 집으로 들어간다."
            $u = +10
            hide j_su2
            jump j_ry
        label j_by:
            "당황한 사이 옆집 사람이 들어가버렸다. "
            $u = -10
            hide j_su1
            jw"아.. 어쩔 수 없지"
            jump j_ry
        label j_ry:
            jw"어디 가려 했더라?"

            menu:
                "아, 마트 가려고 했지":
                    jump j_ma
                
                "아, 운동 가려고 했지":
                    jump j_ka
            label j_ma:
                jw"아 그랬었지"
                jw"장 보러 가자"
                show bg j_room_k
                "그 후, 장 봐온 것들로 음식을 만들어 먹었다."
                show j_food_pa
                jw"음, 맛있네~"
                jw"요리.. 꽤 재능 있을지도?"
                hide j_food_pa
                jw"아.. 근데 설거지.."
                jw"일단 자고 일어나서 할까.."
                "그 후, 피곤해서 금방 잠들었다."
                jump j_ho

            label j_ka:
                jw"아, 그랬었지"
                jw"운동하러 가자"
                scene bg j_room_h
                show j_hh_1 at left
                jhh"오랜만에 오셨네요."
                jw"네, 오랜만에 운동하려 왔어요"
                jhh "즐거운 운동되세요."
                jw "네!"
                hide j_hh_1

                "그 후, 열심히 운동했다"
                jw"너무 무리했나?"
                jw"집가서 쉬어야겠다."
                scene bg j_room1
                "너무 무리해서인지 집에 돌아오자마자 뻗어서 잤다"
                jump j_ho



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
            jw"좀만 더 자자"
            "한참을 자고나니 저절로 눈이 뜨였다."
            jw"으음... 몇시지?"
            jw"벌써 3시네.."
            jw"최근 잠이 부족하긴 했지"
            jw"음.. 배고픈데"
            jw"뭐라도 먹을까?"
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
                        show j_su1 at right
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
                        jp "아! 제 이름은 [player_name](이)예요. "
                        hide j_su3
                        show j_su2 at right
                        jp "앞으로 인사하고 지내도 괜찮을까요?"
                        hide j_su2
                        show j_su3 at right

                        js "좋아요"
                        
                        "그 후, 서윤을 배웅했다."
                        jw "이제 편의점 가야지."
                        show bg j_room_co
                        show j_co_1 at left
                        jco "안녕하세요, Gu입니다."
                        jw "안녕하세요."
                        jw "흠.. 뭐 먹지?"









    return
