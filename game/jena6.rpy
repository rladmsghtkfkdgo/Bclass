label j_dfg: #길
    show j_labe_da
    " "
    hide j_labe_da
    jp"흠.. 집이 좀 더러운 것 같네.."
    jp"청소할까?"
    menu:
        "이왕 하는거 대청소하자":
            jump j_fgh
        "귀찮은데 좀만 미루자":
            jump j_ghj
    label j_fgh:
        jp"할게 산더미네.."
        "그 후, 한참동안 청소했다."
        show j_trash
        " "
        jp"쓰레기도 엄청 나왔네.."
        jp"버리고 와야겠다."
        jp"겸사겸사 밥도 먹고 와야지"
        hide j_trash
        show bg j_room_bo
        "집을 나선다"
        show bg j_room_ca2
        jump j_hjk

    label j_ghj:
        jp"밥이나 먹을까?"
        show bg j_room_ca2
        "집을 나선다"
        jump j_hjk

        label j_hjk:
            show j_su2 at right
            jp"어, 서윤씨?"
            jp"인사해야겠다."
            jp"안녕하세요!"
            jp"뭐하고 계셨어요?"
            show j_su3 at right
            js"아, 고양이 보고 있었어요."
            hide j_su3
            show j_su7 at right
            js"지금은 가버렸지만요"
            hide j_su7
            show j_su3 at right
            js"[jp]씨는요?"
            hide j_su3
            show j_su2 at right
            jp"아, 밥먹으러 가려구요"
            jp"서윤씨는 밥 드셨나요?"
            hide j_su2
            show j_su3 at right
            js"앗, 아직 안먹었어요"
            hide j_su3
            show j_su2 at right
            jp"아, 그럼 같이 드실래요?"
            hide j_su2
            show j_su3 at right
            js "좋아요"
            hide j_su3
            show j_su2 at right
            jump j_jkl

            label j_jkl:
                jp "뭐 드실래요?"
                jump j_klz

                label j_klz:
                    hide j_su2
                    show j_su3 at right
                    js "음.. 간단한 거로 먹을까요?"
                    hide j_su3
                    show j_su2 at right
                    menu:
                        "그럼 제가 만들어드릴까요?":
                            jump j_lzx
                        "그럼 샌드위치 어때요?":
                            jump j_zxc
                    label j_lzx:
                        hide j_su2
                        show j_su3 at right
                        js "앗, 네..!"
                        hide j_su3
                        show j_su2 at right
                        show bg j_room1
                        "서윤과 같이 집으로 돌아왔다."
                        show bg j_room_k
                        jp "혹시 싫어하는거 있으세요?"
                        hide j_su2
                        show j_su3 at right
                        js "음.. 아무거나 좋아요!"
                        hide j_su3
                        show j_su2 at right
                        jp "그러면.."
                        menu:
                            "간단한 닭가슴살":
                                jump j_xcv
                            "간단한 파스타":
                                jump j_cvb
                        label j_xcv:
                            show j_labe_za
                            " "
                            hide j_labe_za
                            jp "다 됐어요"
                            show j_food_dak
                            hide j_su2
                            jp "간단하게 닭가슴살해봤는데 어때요?"
                            jp "드시기 편하게 조금 잘라놨어요."
                            js "아.."
                            js "잘 먹겠습니다.."
                            "그 후, 어두워진 서윤의 낯빛을 눈치채지 못하고 즐겁게 식사를 마쳤다."
                            hide j_food_dak
                            show j_su7 at right
                            js "잘 먹었습니다.."
                            js "맛있었어요.."
                            hide j_su7
                            show j_su5 at right
                            jp "그쵸? 자주 해먹는데 간단하고 맛있더라구요."
                            $ju-=10
                            show j_su7 at right
                            js "아..네..."
                            js "밥 잘 먹었어요, 감사합니다"
                            js "이만 들어가볼게요"
                            hide j_su7
                            show j_su5 at right
                            jp "네, 안녕히 가세요!"
                            hide j_su5
                            show j_su7 at right
                            js "네"
                            hide j_su7
                            show bg j_room_bo
                            hide j_su7
                            show j_su5 at right
                            "그 후, 서윤을 배웅했다"
                            show bg j_room1
                            " "
                            hide j_su5
                            jump j_vbn

                        label j_cvb:
                            show j_labe_za
                            " "
                            hide j_labe_za
                            jp "다 됐어요"
                            show j_food_papa
                            jp "간단하게 파스타해봤는데 어때요?"
                            hide j_su2
                            show j_su3 at right
                            js "잘 먹겠습니다!"
                            "그 후, 즐겁게 식사를 마쳤다."
                            hide j_food_papa
                            js "잘 먹었습니다"
                            js"맛있었어요!"
                            hide j_su3
                            show j_su2 at right
                            jp "그쵸? 자주 해먹는데 간단하고 맛있더라구요."
                            $ju+=10
                            hide j_su2
                            show j_su3 at right
                            js"네, 좋았어요."
                            js "밥 잘 먹었어요, 감사합니다"
                            js "이만 들어가볼게요."
                            jp "네, 안녕히 가세요!"
                            js "네!"
                            show bg j_room_bo
                            hide j_su3
                            "그 후, 서윤을 배웅했다"
                            show bg j_room1
                            jump j_vbn

                    label j_zxc:
                        js "좋아요"
                        jp "샌드위치 맛있는 곳 아는데 거기로 갈까요?"
                        hide j_su2
                        show j_su3 at right
                        js "네!"
                        show bg j_room_sand
                        "그 후, 서윤과 함께 점심을 먹었다."
                        js "덕분에 맛있는 곳 알게 된 것 같아요."
                        js "감사합니다!"
                        hide j_su3
                        show j_su2 at right
                        jp "맛있었다니 다행이에요"
                        jp "밥도 먹었으니 가볍게 산책이라도 할까요?"
                        hide j_su2
                        show j_su3 at right
                        js "좋아요!"
                        hide bg j_room_sand
                        show bg j_room_sa
                        hide j_su3
                        show j_su2 at right
                        "서윤과 산책하며 이런저런 얘기를 나눴다."
                        $u+=20
                        show bg j_room_bo
                       
                        "산책이 끝난 후, 서윤을 배웅해주었다."
                        hide j_su2
                        show j_su3 at right
                        js "오늘 감사했어요"
                        js "조심히 들어가세요!"
                        jp "네, 저도요."
                        jp "조심히 들어가세요!"
                        hide j_su3
                        show bg j_room1
                        "그 후, 집에 돌아와 서윤의 생각을 했다."
                        jump j_vbn


            


       


label j_gfd: #산
    show j_labe_da
    " "
    hide j_labe_da
    jp "흠.. 집이 좀 더러운 것 같네.."
    jp "청소할까?"
    menu:
        "이왕 하는거 대청소하자":
            jump j_hgf
        "귀찮은데 좀만 미루자":
            jump j_jhg
    label j_hgf:
        jp "할게 산더미네.."
        "그 후, 한참동안 청소했다."
        " "
        show j_trash
        jp "쓰레기도 엄청 나왔네.."
        jp "버리고 와야겠다."
        jp "겸사겸사 밥도 먹고 와야지"
        hide j_trash
        show bg j_room_ca2
        "집을 나선다"
        jump j_kjh

    label j_jhg:
        "밥이나 먹을까?"
        show bg j_room_ca2
        "집을 나선다"
        jump j_kjh

        label j_kjh:
            show j_su5 at right
            jp "어, 서윤씨?"
            jp "인사해야겠다."
            jp "안녕하세요!"
            show j_su7 at right
            js "아.. 안녕하세요.."
            hide j_su7
            show j_su5 at right
            jp "뭐하고 계셨어요?"
            hide j_su5
            show j_su7 at right
            js "아, 고양이 보고 있었어요."
            hide j_su7
            show j_su8 at right
            js "지금은 가버렸지만요"
            
            js "[jp]씨는요?"
            hide j_su8
            show j_su5 at right
            jp "아, 밥먹으러 가려구요"
            jp "서윤씨는 밥 드셨나요?"
            hide j_su5
            show j_su7 at right
            js "저는 별로 생각이 없어서.."
            hide j_su7
            show j_su5 at right

            jp "그럼 안돼요"
            jp "밥은 먹어야죠"
            jp "무슨 고민 있으세요?"
            hide j_su5
            show j_su7 at right
            js"아.."
            menu:
                "밥 생각도 없으실 정도면 큰 일 아니에요?":
                    jump j_xcvq
                "뭐, 지금 당장 말해주실 필요는 없으니까요. \n 원하실때 말해주세요.":
                    jump j_vcxq
            label j_xcvq:
                js "그게.."
                "그 후, 한동안 서윤의 고민을 들어주었다."
                jp "아.. 그동안 고생하셨겠네요.."
                js "아니에요"
                hide j_su7
                show j_su3 at right
                js "그래도 [jp]씨가 들어주셔서 많이 좋아졌어요."
                hide j_su3
                show j_su2 at right
                jp "다행이에요."
                jp "나중에 또 힘드신 일 있으면 얘기해주세요!"
                hide j_su2
                show j_su3 at right
                js "네, [jp]씨도요!"
                hide j_su3
                show j_su2 at right
                jp "그럼 아까보다 기분도 나아졌겠다."
                jp "뭐라도 먹을까요?"
                $ju+=10
                show j_su3 at right
                js "좋아요"
                jump j_lkj
            
            label j_vcxq: #산
                js "네.."
                jp "그래도 밥은 중요하니까요."
                jp "뭐라도 먹어야죠."
                jp "밀 나온 김에 같이 먹어요."
                label j_zlkq:
                    js "음.. 그럼 간단한 거로.."
                    menu:
                        "그럼 제가 만들어드릴까요?":
                            jump j_xzlq
                        "그럼 샌드위치 어때요?":
                            jump j_cxzq
                    label j_xzlq:
                        js "앗, 네.."
                        show bg j_room1
                        "서윤과 같이 집으로 돌아왔다."
                        show bg j_room_k
                        jp "혹시 싫어하는거 있으세요?"
                        js "음.. 아무거나 좋아요."
                        jp "그러면.."
                        menu:
                            "간단한 닭가슴살":
                                jump j_vcxqq
                            "간단한 파스타":
                                jump j_bvcq
                        label j_vcxqq:
                            show j_labe_za
                            " "
                            hide j_labe_za
                            jp "다 됐어요"
                            show j_food_dak
                            jp "간단하게 닭가슴살해봤는데 어때요?"
                            jp "드시기 편하게 조금 잘라놨어요."
                            hide j_su2
                            show j_su7 at right
                            js "아.."
                            js "잘 먹겠습니다.."
                            "그 후, 어두워진 서윤의 낯빛을 눈치채지 못하고 즐겁게 식사를 마쳤다."
                            hide j_food_dak
                            js "잘 먹었습니다.."
                            js "맛있었어요.."
                            hide j_su7
                            show j_su5 at right
                            jp "그쵸? 자주 해먹는데 간단하고 맛있더라구요."
                            $ju-=10
                            hide j_su5
                            show j_su7 at right
                            js "아..네..."
                            js "밥 잘 먹었어요, 감사합니다.."
                            js "이만 들어가볼게요"
                            hide j_su7
                            show j_su5 at right
                            jp "네, 안녕히 가세요!"
                            hide j_su5
                            show j_su7 at right
                            js "네.."
                            show bg j_room_bo
                            hide j_su7
                            "그 후, 서윤을 배웅했다"
                            show bg j_room1
                            jump j_nbvq

                        label j_bvcq:
                            show j_labe_za
                            " "
                            hide j_labe_za
                            jp "다 됐어요"
                            show j_food_papa
                            jp "간단하게 파스타해봤는데 어때요?"
                            show j_su7 at right
                            js "아, 잘 먹겠습니다.."
                            "그 후, 즐겁게 식사를 마쳤다."
                            hide j_food_papa
                            js "잘 먹었습니다"
                            js "맛있었어요"
                            hide j_su7
                            show j_su5 at right
                            jp "그쵸? 자주 해먹는데 간단하고 맛있더라구요."
                            $ju+=10
                            hide j_su5
                            show j_su7 at right
                            js "네, 좋았어요."
                            js "밥 잘 먹었어요, 감사합니다"
                            js "이만 들어가볼게요."
                            jp "네, 안녕히 가세요!"
                            js "네"
                            show bg j_room_bo
                            hide j_su7
                            "그 후, 서윤을 배웅했다"
                            show bg j_room1
                            jump j_nbvq

                    label j_cxzq:
                        js "좋아요"
                        jp "샌드위치 맛있는 곳 아는데 거기로 갈까요?"
                        show j_su7 at right
                        js "네."
                        show bg j_room_sand
                        "그 후, 서윤과 함께 점심을 먹었다."
                        js "덕분에 맛있는 곳 알게 된 것 같아요."
                        js "감사합니다"
                        $ju+=10
                        hide j_su7
                        show j_su5 at right
                        jp "맛있었다니 다행이에요"
                        jp "밥도 먹었으니 가볍게 산책이라도 할까요?"
                        hide j_su5
                        show j_su7 at right
                        js "아니에요, 먼저 들어가볼게요"
                        js "산책은 다음에 같이 해요."
                        jp "아.. 그럼 바래다 드릴게요!"
                        js "아, 감사합니다."
                        show bg j_room_bo
                        hide j_su7
                        "그 후, 서윤을 배웅해주었다."
                        show bg j_room1
                        jump j_nbvq

    

            
            label j_lkj: #길
                jp "뭐 드실래요?"
                jump j_zlk

                label j_zlk:
                    js "음.. 간단한 거로 먹을까요?"
                    menu:
                        "그럼 제가 만들어드릴까요?":
                            jump j_xzl
                        "그럼 샌드위치 어때요?":
                            jump j_cxz
                    label j_xzl:
                        js "앗, 네..!"
                        hide j_su3
                        show j_su2 at right
                        show bg j_room1
                        "서윤과 같이 집으로 돌아왔다."
                        show bg j_room_k
                        jp "혹시 싫어하는거 있으세요?"
                        hide j_su2
                        show j_su3 at right
                        js "음.. 아무거나 좋아요!"
                        hide j_su3
                        show j_su2 at right
                        jp "그러면.."
                        menu:
                            "간단한 닭가슴살":
                                jump j_vcx
                            "간단한 파스타":
                                jump j_bvc
                        label j_vcx:
                            show j_labe_za
                            " "
                            hide j_labe_za
                            jp "다 됐어요"
                            show j_food_dak
                            jp "간단하게 닭가슴살해봤는데 어때요?"
                            jp "드시기 편하게 조금 잘라놨어요."
                            hide j_su2
                            show j_su7 at right
                            js "아.."
                            js "잘 먹겠습니다.."
                            "그 후, 어두워진 서윤의 낯빛을 눈치채지 못하고 즐겁게 식사를 마쳤다."
                            hide j_food_dak
                            js "잘 먹었습니다.."
                            js "맛있었어요.."
                            hide j_su7
                            show j_su5 at right
                            jp "그쵸? 자주 해먹는데 간단하고 맛있더라구요."
                            $ju-=10
                            show j_su7 at right
                            js "아..네..."
                            js "밥 잘 먹었어요, 감사합니다"
                            js "이만 들어가볼게요"
                            hide j_su7
                            show j_su5 at right
                            jp "네, 안녕히 가세요!"
                            hide j_su5
                            show j_su7 at right
                            js "네"
                            hide j_su7
                            show bg j_room_bo
                            "그 후, 서윤을 배웅했다"
                            show bg j_room1
                            jump j_nbv

                        label j_bvc:
                            show j_labe_za
                            " "
                            hide j_labe_za
                            jp "다 됐어요"
                            show j_food_papa
                            jp "간단하게 파스타해봤는데 어때요?"
                            show j_su3 at right
                            js "아, 잘 먹겠습니다!"
                            "그 후, 즐겁게 식사를 마쳤다."
                            hide j_food_papa
                            js "잘 먹었습니다"
                            js "맛있었어요!"
                            hide j_su3
                            show j_su2 at right
                            jp "그쵸? 자주 해먹는데 간단하고 맛있더라구요."
                            $ju+=10
                            hide j_su2
                            show j_su3 at right
                            js"네, 좋았어요."
                            js "밥 잘 먹었어요, 감사합니다"
                            js "이만 들어가볼게요."
                            jp "네, 안녕히 가세요!"
                            js "네!"
                            hide j_su3
                            show bg j_room_bo
                            "그 후, 서윤을 배웅했다"
                            show bg j_room1
                            jump j_nbv

                    label j_cxz:
                        js "좋아요"
                        jp "샌드위치 맛있는 곳 아는데 거기로 갈까요?"
                        show j_su3 at right
                        js "네!"
                        show bg j_room_sand
                        "그 후, 서윤과 함께 점심을 먹었다."
                        js "덕분에 맛있는 곳 알게 된 것 같아요."
                        js "감사합니다!"
                        hide j_su3
                        show j_su2 at right
                        jp "맛있었다니 다행이에요"
                        jp "밥도 먹었으니 가볍게 산책이라도 할까요?"
                        hide j_su2
                        show j_su3 at right
                        js "좋아요!"
                        hide bg j_room_sand
                        show bg j_room_sa
                        "서윤과 산책하며 이런저런 얘기를 나눴다."
                        $ju+=20
                        show bg j_room_bo
                        "산책이 끝난 후, 서윤을 배웅해주었다."
                        js "오늘 감사했어요"
                        js "조심히 들어가세요!"
                        jp "네, 저도요."
                        jp "조심히 들어가세요!"
                        hide j_su3
                        show bg j_room1
                        "그 후, 집에 돌아와 서윤의 생각을 했다."
                        jump j_nbv


    