label j_vbn: #길
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
    "뭐하지?"
    "흠.. 심심한데.."
    "서윤씨는 뭐하려나.."
    "연락해볼까?"
    "여보세요?"
    "네, 여보세요."
    "뭐하고 계세요?"
    "아, 노래듣고 있어요"
    "[jp]씨는요?"
    "그냥 있었어요"
    "아하"
    "아, 혹시 고양이카페 좋아하세요?"
    "당연하죠!"
    "같이 가실래요?"
    "음..언제요?"
    "음.. 오늘 괜찮으세요?"
    "그러면 조금 뒤에 복도에서 만날까요?"
    "네, 좀 이따 봬요!"
    "네!"
    "음.. 그럼 뭐 입고 나가지?"
    menu:
        "무난하게 깔끔한 티":
            jump j_bnm
        "내가 좋아하는 노란 형광 티":
            jump j_nmq
    label j_bnm:
        "d"
    label j_nmq:
        "s"

        



label j_nbvq: #산
    show j_labe_da
    " "
    hide j_labe_da
    "[u]"
