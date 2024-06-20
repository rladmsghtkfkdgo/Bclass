label j_lz:
    
    if u <= 19:
        "옆집 사람과는 동선이 꽤 겹치는 것 같다."
        jump j_zx
    else:
        "옆집 사람과 대화하며 지낸지 며칠이 지났다."
        jump j_xc

        label j_zx:
            "..."
            "어색한데.."
            "좀 피해다녀야지.."
            show j_labe_ge
            " "
            hide j_labe_ge
            "그 후로 옆집 사람을 보지 못했다."
            "듣기로는 이사를 간 듯 싶다."

        label j_xc:
            "꽤 자주 마주쳐 같이 움직일 떄도 있다."
            scene bg j_room_bo
            show j_su2 at right
            jp "아, 서윤씨! 안녕하세요!"
            hide j_su2
            show j_su3 at right
            js "안녕하세요"
            jp "어디가세요?"
            "잠시 산책하러 가려구요"
            "[jp]씨는요?"




