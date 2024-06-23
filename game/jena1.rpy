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
                $ju-=10
    
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
            $u+=10
            hide j_su2
            jump j_ry
        label j_by:
            "당황한 사이 옆집 사람이 들어가버렸다. "
            $ju-=10
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


    return
