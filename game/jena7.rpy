label j_vbn: #길
    scene black
    with fade
    scene bg j_room1
    with fade
    "[ju]"
    show j_labe_me
    " "
    hide j_labe_me
    jp "뭐하지?"
    jp "흠.. 심심한데.."
    jp "서윤씨는 뭐하려나.."
    jp "연락해볼까?"
    "뚜르르"
    jp "여보세요?"
    show j_su3 at right
    js "네, 여보세요."
    hide j_su3
    show j_su2 at right
    jp "뭐하고 계세요?"
    hide j_su2
    show j_su3 at right
    js "아, 노래듣고 있어요"
    js "[jp]씨는요?"
    hide j_su3
    show j_su2 at right
    jp "그냥 있었어요"
    hide j_su2
    show j_su3 at right
    js "아하"
    jp "아, 혹시 고양이카페 좋아하세요?"
    hide j_su3
    show j_su3 at right
    js "당연하죠!"
    hide j_su3
    show j_su2 at right
    jp "같이 가실래요?"
    hide j_su2
    show j_su3 at right
    js "음..언제요?"
    hide j_su3
    show j_su2 at right
    jp "음.. 오늘 괜찮으세요?"
    hide j_su2
    show j_su3 at right
    js "그러면 조금 뒤에 복도에서 만날까요?"
    jp "네, 좀 이따 봬요!"
    js "네!"
    hide j_su3
    jp "음.. 그럼 뭐 입고 나가지?"
    menu:
        "무난하게 깔끔한 티":
            jump j_bnm
        "내가 좋아하는 노란 형광 티":
            jump j_nmq
    label j_bnm: #길 무난티
        jp "좋아, 골랐어!"
        jp "이제 나가볼까"
        show j_room_bo
        "집을 나선다"
        jp "서윤씨는 아직인가보네"
        show j_labe_za
        " "
        hide j_labe_za
        show j_su2 at right
        "서윤이 나왔다."
        jp "오셨어요?"
        hide j_su2
        show j_su4 at right

        js "앗, 많이 기다리셨나요?"
        jp "아니에요, 저도 나온지 얼마 안됐어요."
        hide j_su4
        show j_su3 at right
        js "다행이에요."
        hide j_su3
        show j_su2 at right
        jp "그럼 갈까요?"
        hide j_su2
        show j_su3 at right
        js "네!"
        hide bg j_room_bo
        scene black
        with fade
        scene bg j_room_caca
        with fade
        hide j_su3
        show j_su3 at right
        js "와, 고양이가 엄청 많네요!"
        hide j_su3
        show j_su2 at right
        "그 후, 한참동안 고양이와 놀았다."
        hide j_su2
        scene bg j_room_bo
        with fade
        show j_su3 at right
        js "오늘 정말 즐거웠어요"
        js "감사했습니다!"
        hide j_su3
        show j_su2 at right
        $u = +20
        jp "저도 오늘 즐거웠어요."
        jp "조심히 들어가세요!"
        hide j_su2
        show j_su3 at right
        js "네!"
        "그 후, 서윤을 배웅했다."
        hide j_su3
        scene black
        with fade
        scene bg j_room1
        with fade
        jump j_mqw


    label j_nmq: #길 형광티
        jp "좋아, 골랐어!"
        jp "이제 나가볼까"
        show j_room_bo
        "집을 나선다"
        jp "서윤씨는 아직인가보네"
        show j_labe_za
        " "
        hide j_labe_za
        show j_su5 at right
        "서윤이 나왔다."
        jp "오셨어요?"
        hide j_su5
        show j_su7 at right
        "앗.."
        "아.."
        "서윤은 형광색의 티를 보고 당황했으나 눈치채지 못한다"

        js "앗, 많이 기다리셨나요..?"
        hide j_su7
        show j_su5 at right
        jp "아니에요, 저도 나온지 얼마 안됐어요."
        hide j_su5
        show j_su7 at right
        js "다행이에요."
        hide j_su7
        show j_su5 at right
        jp "그럼 갈까요?"
        hide j_su5
        show j_su5 at right
        js "네.."
        hide bg j_room_bo
        show bg j_room_caca
        hide j_su5
        show j_su3 at right
        js "와, 고양이가 엄청 많네요"
        hide j_su3
        show j_su2 at right
        "그 후, 한참동안 고양이와 놀았다."
        hide j_su2
        scene bg j_room_bo
        with fade
        show j_su3 at right
        js "오늘 정말 즐거웠어요"
        js "감사했습니다!"
        hide j_su3
        show j_su2 at right
        $u = +10
        jp "저도 오늘 즐거웠어요."
        jp "조심히 들어가세요!"
        hide j_su2
        show j_su3 at right
        js "네!"
        "그 후, 서윤을 배웅했다."
        hide j_su3
        scene black
        with fade
        scene bg j_room1
        with fade
        jump j_mqw
       

        



label j_nbvq: #산
    scene black
    with fade
    scene bg j_room1
    with fade
    show j_labe_da
    " "
    hide j_labe_da
    "[u]"
    show j_labe_me
    " "
    hide j_labe_me
    jp "뭐하지?"
    jp "흠.. 심심한데.."
    jp "서윤씨는 뭐하려나.."
    jp "연락해볼까?"
    "뚜르르"
    jp "여보세요?"
    show j_su7 at right
    js "네, 여보세요."
    hide j_su7
    show j_su5 at right
    jp "뭐하고 계세요?"
    hide j_su5
    show j_su7 at right
    js "아.. 노래듣고 있어요"
    js "[jp]씨는요?"
    hide j_su7
    show j_su5 at right
    jp "그냥 있었어요"
    hide j_su5
    show j_su7 at right
    js "아하"
    jp "아, 혹시 고양이카페 좋아하세요?"
    "좋아하긴 한데.."
    menu:
        "같이 가요":
            jump j_qweaw
        "일 있으시면 다음에 같이 가도 괜찮구요!":
            jump j_qwezw
   
    
    label j_qwezw: #산 산
        js "아.."
        js "그럼 다음에 같이 가요"
        jp "좋아요!"
        hide j_su7
        "뚝"
        jp "흠.. 바쁘신가보네"
        jp "다음에 다시 연락해봐야겠다."
        scene black
        with fade
        scene j_room1
        with fade
        jump j_mqww

    

    label j_qweaw: #산 길
        jp "기분 전환이 될거에요"
        js "음, 그럼.."
        jp "언제가 편하세요?"
        js "그러면 조금 뒤에 복도에서 만날까요?"
        jp "네, 좀 이따 봬요"
        js "네."
        jump j_ertw

label j_ertw:
    jp "음.. 그럼 뭐 입고 나가지?"
    menu:
        "무난하게 깔끔한 티":
            jump j_bnmw
        "내가 좋아하는 노란 형광 티":
            jump j_nmqw
    label j_bnmw: #산 무난티
        jp "좋아, 골랐어!"
        jp "이제 나가볼까"
        show j_room_bo
        "집을 나선다"
        jp "서윤씨는 아직인가보네"
        show j_labe_za
        " "
        hide j_labe_za
        show j_su5 at right
        "서윤이 나왔다."
        jp "오셨어요?"
        hide j_su5
        show j_su4 at right

        js "앗, 많이 기다리셨나요?"
        jp "아니에요, 저도 나온지 얼마 안됐어요."
        hide j_su4
        show j_su3 at right
        js "다행이에요."
        hide j_su3
        show j_su5 at right
        jp "그럼 갈까요?"
        hide j_su5
        show j_su3 at right
        js "네!"
        hide bg j_room_bo
        scene black
        with fade
        scene bg j_room_caca
        with fade
        
        hide j_su3
        show j_su3 at right
        js "와, 고양이가 엄청 많네요!"
        hide j_su3
        show j_su2 at right
        "그 후, 한참동안 고양이와 놀았다."
        hide j_su2
        scene bg j_room_bo
        with fade
        show j_su3 at right
        js "오늘 정말 즐거웠어요"
        js "감사했습니다!"
        hide j_su3
        show j_su2 at right
        $u = +20
        jp "저도 오늘 즐거웠어요."
        jp "조심히 들어가세요!"
        hide j_su2
        show j_su3 at right
        js "네!"
        "그 후, 서윤을 배웅했다."
        hide j_su3
        scene black
        with fade
        scene bg j_room1
        with fade

        jump j_mqw


    label j_nmqw: #산 형광티
        jp "좋아, 골랐어!"
        jp "이제 나가볼까"
        show j_room_bo
        "집을 나선다"
        jp "서윤씨는 아직인가보네"
        show j_labe_za
        " "
        hide j_labe_za
        show j_su5 at right
        "서윤이 나왔다."
        jp "오셨어요?"
        hide j_su5
        show j_su7 at right
        "앗.."
        "아.."
        "서윤은 형광색의 티를 보고 당황했으나 눈치채지 못한다"

        js "앗, 많이 기다리셨나요..?"
        hide j_su7
        show j_su5 at right
        jp "아니에요, 저도 나온지 얼마 안됐어요."
        hide j_su5
        show j_su7 at right
        js "다행이에요."
        hide j_su7
        show j_su5 at right
        jp "그럼 갈까요?"
        hide j_su5
        show j_su5 at right
        js "네.."
        hide bg j_room_bo
        scene black
        with fade
        scene bg j_room_caca
        with fade
        hide j_su5
        show j_su3 at right
        js "와, 고양이가 엄청 많네요"
        hide j_su3
        show j_su2 at right
        "그 후, 한참동안 고양이와 놀았다."
        hide j_su2
        scene bg j_room_bo
        with fade
        show j_su3 at right
        js "오늘 정말 즐거웠어요"
        js "감사했습니다!"
        hide j_su3
        show j_su2 at right
        $u = +20
        jp "저도 오늘 즐거웠어요."
        jp "조심히 들어가세요!"
        hide j_su2
        show j_su3 at right
        js "네!"
        "그 후, 서윤을 배웅했다."
        hide j_su3
        scene black
        with fade
        scene bg j_room1
        with fade
        jump j_mqw