label j_cv:
    show j_labe_zu
    " "
    hide j_labe_zu
    menu:
        "밖에 나가볼까?":
            jump j_vb
        "집이 최고지 집에 있자":
            "뭐할까?"
            "흠.. 유튜브나 보자"
            jump j_qwe
    label j_vb:
        "나가는 김에 과자도 사올까?"
        "고양이.. 있으려나?"
        "츄르... 가져갈까?"
        "음.. 가져가자."
        show bg j_room_ca2
        "어, 없나?"
        show bg j_room_ca1
        "아, 있다!"
        "거기 있었구나"
        "배고프지?"
        "츄르 줄게, 이리 와"
        "고양이.. 서윤씨도 좋아할텐데.."
        "다음엔 같이 오자고 해야겠다."
        "서윤의 생각을 하며 편의점으로 갔다."
        show bg j_room_co
        show j_co_1 at left
        jco "안녕하세요, Gu입니다."
        jp "안녕하세요."
        "뭐 살까?"
        menu:
            "양심의 가책을 덜기 위한 포카chip!":
                jump j_nm
            "과자는 단짠단짠이지, 꼬깔corn 매콤달콤맛!":
                jump j_nm
        label j_nm:
            "좋아, 이거로 결정!"
            "과자를 들고 즐거운 발걸음으로 집에 돌아갔다."
            hide bg j_room_co
            show bg j_room1
            "유튜브 보면서 과자나 먹을까"
            "(과자를 뜯으며) \n 유튜브나 볼까"
            jump j_qwe

    label j_qwe:
        show j_hand
        "유튜브를 본다"
        "유피아의 영상에 심한 악플이 달린 것을 보게 된다."
        "뭐지..?"
        "음.."
        menu:
            "이 사람도 고생이 많네.. \n 근데 좀 심한 거 같은데..?":
                jump j_wer
            "뭐.., 욕 먹을 만한 짓을 했겠지. \n 다른 영상이나 보자.":
                jump j_ert
        label j_wer:
            "잠시 멈칫 했지만 금방 다른 영상으로 넘어갔다."
            jump j_rty
        label j_ert:
            "금방 다른 영상으로 넘어갔다."
            jump j_rty

            label j_rty:
                #show labe 한참뒤
                " "

                "슬슬 다른 거 할까?"
                "이제 뭐하지?"
                "옷 안 산지 꽤 된 것 같은데.."
                "옷 살까?"
                "뭐가 좋을까?"
                menu:
                    "무난하게 깔끔한 티":
                        jump j_tyu
                    "내가 좋아하는 노란 형광티":
                        jump j_tyu
                label j_tyu:
                    "좋아, 이거로 결정!"
                    "마음에 드는 옷을 사, 기분 좋게 잠들었다."
                    jump j_yui


                



        











    