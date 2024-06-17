# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"


# 여기에서부터 게임이 시작합니다.
label jn:
    scene bg room1

    play sound "dodo.ogg"
    "유튜브에서 알람이 왔다"
    show hand
    show alm
    " "
    hide alm
    show utb
    w"아, 유튜브 알람이네"
    w"이왕 들어온거 유튜브나 볼까"
    hide utb
    "뭐 볼까?"

    menu:
        "영상 보자":
            "(유피아의 영상이 뜬다)"
            jump fir
        "숏츠 보자":
            show upi_1
            jump fir
    label fir:
        w "요즘 이 사람 많이 보이네"
        hide upi_1
        show labe_2
        " "
        hide hand
        hide labe_2

        w"유튜브만 2시간 봤네, 슬 다른거 할까?"
    

    menu:
        "밥을 먹는다":
            jump bab
        "운동을 한다":
            jump muc
        "유튜브를 마저 본다":
            jump utb
            

    label bab:
        "마침 밥 시간이네. 뭐 먹지?"
        menu:
            "귀찮지만 만들어먹자":
                jump na

            "귀찮은데 뭘 만들어. 시켜먹자":
                jump two
            
        label two:
                w"오랜만에 치킨 먹을까.."
                "(뚜르르)"
                w"네, 여기 00아파트 00동...."
                show labe_za
                " "
                hide labe_za
                "(띵동)"
                w"오 왔다!"
                scene bg room_bo
                "(문을 연다)"
                show su1 at right
                
                w ".....!"
                scene bg room1
                hide su1
                "놀라서 인사도 잊어버린 채 다시 들어왔다."
                $u = -10
    
                w "아..깜짝이야.."
                w "치킨이나 먹어야지.."
                "그 후, 먹은 것을 대충 치우고 잠들었다."
                jump ho


        label na:
            "(냉장고를 연다)
            냉장고에 뭐가 있더라"
            w "흠.. 뭐가 없네, 마트 다녀와야겠다."
            jump vip
    label muc:
        w "흠...오랜만에 운동이나 할까?"
        w "무슨 운동하지.."
        w "오랜만의 운동인데 헬스장 가야겠다."
        jump vip

    label utb:
        w "아니다."
        w "보는 김에 마저 볼까?"
        show labe_3
        " "
        hide labe_3
        w "벌써 시간이.."
        w "저녁 먹어야겠다."
        w "배달시켜 먹어야지"
        jump two

    label vip:
        scene bg room_bo
        "집을 나선다"
        
        show su1 at right
        "어, 옆집사람이네.."
        "어쩌지?"
        menu:
            "이웃인데 인사는 하고 지내야지. 가볍게 목례하고 지나간다.":
                jump hi
            "갑작스러운 만남에 당황스러워한다.":
                jump by
        label hi:
            hide su1
            show su2 at right
            "(꾸벅)"
            "옆집 사람도 목례하며 집으로 들어간다."
            $u = +10
            hide su2
            jump ry
        label by:
            "당황한 사이 옆집 사람이 들어가버렸다. "
            $u = -10
            hide su1
            w"아.. 어쩔 수 없지"
            jump ry
        label ry:
            w"어디 가려 했더라?"

            menu:
                "아, 마트 가려고 했지":
                    jump ma
                
                "아, 운동 가려고 했지":
                    jump ka
            label ma:
                w"아 그랬었지"
                w"장 보러 가자"
                show bg room_k
                "그 후, 장 봐온 것들로 음식을 만들어 먹었다."
                show food_pa
                w"음, 맛있네~"
                w"요리.. 꽤 재능 있을지도?"
                hide food_pa
                w"아.. 근데 설거지.."
                w"일단 자고 일어나서 할까.."
                "그 후, 피곤해서 금방 잠들었다."
                jump ho

            label ka:
                w"아, 그랬었지"
                w"운동하러 가자"
                scene bg room_h
                show hh_1 at left
                hh"오랜만에 오셨네요."
                w"네, 오랜만에 운동하려 왔어요"
                hh "즐거운 운동되세요."
                w "네!"
                hide hh_1

                "그 후, 열심히 운동했다"
                w"너무 무리했나?"
                w"집가서 쉬어야겠다."
                scene bg room1
                "너무 무리해서인지 집에 돌아오자마자 뻗어서 잤다"
                jump ho



    label ho:
        show bg room1
        show labe_da
        " "
        hide labe_da
        menu:
            "지금 일어날까?":
                jump mu
            "아냐 좀만 더 자자":
                jump we
        label mu:
            "오늘은 뭐할까?"
            menu:
                "독서는 마음의 양식이지":
                    jump qw
                "오랜만에 게임이나 할까?":
                    jump er
                "여유로운 아침을 즐기자":
                    jump tr
            label qw:
                w"오랜만에 해포리터 읽을까?"
                "시리즈 책을 읽다보니 시간이 빨리 지나갔다."
                w"역시 해포리터는 명작이야"
                w"지금 몇시지?"
                w"벌써 3시야?"
                w"재밌어서 배고픈줄도 몰랐네"
                w"배고픈데 뭐먹지?"
                jump yu
            label er:
                w"좀만 할까?"
                "정신을 차려보니 어느덧 3시가 되었다."
                w"지금 몇시지?"
                w"벌써 3시야?"
                w"재밌어서 배고픈줄도 몰랐네"
                w"배고픈데 뭐먹지?"
                jump yu
            label tr:
                w"여유로운 아침이네"
                w"좀 더 이대로 있을까.."
                "포근한 날씨에 잠에 들었다."
                w"으음...얼마나 잔거지..?"
                w"벌써 4시네"
                w"일찍 일어난 보람이 없네"
                w"뭐, 잘 잤으니 됐나~"
                w"그나저나 묘하게 배고프네"
                w"뭐라도 먹을까?"
                jump yu

        label we:
            w"좀만 더 자자"
            "한참을 자고나니 저절로 눈이 뜨였다."
            w"으음... 몇시지?"
            w"벌써 3시네.."
            w"최근 잠이 부족하긴 했지"
            w"음.. 배고픈데"
            w"뭐라도 먹을까?"
            jump yu

            label yu:
                w"집에서 먹을까, 밖에서 먹을까 고민되네"
                menu:
                    "집에서 먹자":
                        jump io
                    "밖에서 먹자":
                        jump ui
                label ui:
                    scene bg room_bo
                    "집을 나선다."
                    scene bg room_ca
                    w"어,"
                    w"고양이다!"
                    w"배고픈가..?"
                    w"뭐라도 사올까.."
                    hide bg room_ca
                    show bg room_co
                    show co_1 at left
                    co "안녕하세요, Gu입니다."
                    w "안녕하세요."
                    w "흠.. 츄르면 되려나?"
                    w "계산해 주세요."
                    play sound "Beep.ogg"
                    co "(삑)"
                    play sound "dodo.ogg"
                    co "3800원입니다."
                    co "감사합니다, 또 오세요"
                    w "안녕히 계세요~"
                    hide co_1
                    hide bg room_co
                    show bg room_ca

                    w"고양이.. 아직 있으려나?"
                    w"아, 있다!"
                    w"어, 고양이랑..."
                    w"옆집 사람..??"
                    w"어쩌지?"
                    menu:
                        "그냥 지나가자":
                            jump op
                        "어차피 옆집 사람인데.. 인사하고 지내자":
                            jump pa
                    label op:
                        "츄르를 주머니에 넣고 지나갔다."
                        $u = -20
                        jump sd
                    label pa:
                        w"저.. 안녕하세요?"
                        show su1 at right
                        d"아..안녕하세요."
                        w"고양이.. 좋아하세요?"
                        hide su1 
                        show su2 at right
                        d"네, 좋아해요."
                        d"고양이 좋아하세요?"
                        w" 네, 좋아해요."
                        w"아, 방금 츄르 사왔는데 줘보실래요?"
                        show su4 at right
                        d"어...!"
                        hide su4
                        show su3 at right
                        d"좋아요!"
                        w"여기요."
                        hide su3
                        show su2 at right
                        w"그러고보니 이름이 어떻게 되세요?"
                        hide su2
                        show su3 at right
                        s"서윤이에요, 서서윤."
                        s"이름이 어떻게 되세요?"
                        $player_name = renpy.input("아! 제 이름은")
                        p "아! 제 이름은 [player_name](이)예요. "
                        hide su3
                        show su2 at right
                        p "앞으로 인사하고 지내도 괜찮을까요?"
                        hide su2
                        show su3 at right

                        s "좋아요"
                        
                        "그 후, 서윤을 배웅했다."
                        w "이제 편의점 가야지."
                        show bg room_co
                        show co_1 at left
                        co "안녕하세요, Gu입니다."
                        w "안녕하세요."
                        w "흠.. 무ㅝ 먹지?"









    return
