label j_lz:
    scene black
    with fade
    scene bg j_room1
    with fade
    
    if ju <= 19:
        show j_labe_me
        " "
        hide j_labe_me
        "옆집 사람과는 동선이 꽤 겹치는 것 같다.."
        jump j_zx
    else:
        show j_labe_me
        " "
        hide j_labe_me
        "옆집 사람과 대화하며 지낸지 며칠이 지났다."
        jump j_xc

        label j_zx:
            "..."
            "어색한데.."
            "좀 피해다녀야지.."
            scene black
            with fade
            scene bg j_room1
            with fade
            show j_labe_ge
            " "
            hide j_labe_ge
            "그 후로 옆집 사람을 보지 못했다."
            "듣기로는 이사를 간 듯 싶다."
            scene black
            with fade
            scene bg j_end_05 at right
            with fade
            $ renpy.pause(7.0)
            

            return

        label j_xc:
            "자주 마주쳐 같이 움직일 때도 많다."
            scene bg j_room_bo
            show j_su2 at right
            jp "아, 서윤씨! 안녕하세요!"
            hide j_su2
            show j_su3 at right
            js "안녕하세요"
            hide j_su3
            show j_su2 at right
            jp "어디가세요?"
            hide j_su2
            show j_su3 at right
            js"잠시 산책하러 가려구요"
            js"[jp]씨는요?"
            hide j_su3
            show j_su2 at right
            jp "앗, 저도 마침 산책 가려했는데 같이 가도 되나요?"
            hide j_su2
            show j_su3 at right
            js"그래주시면 저야 좋죠"
            hide j_su3
            show j_su2 at right
            scene black
            with fade
            scene bg j_room_sa
            with fade
            show j_su2 at right
            "그 후, 같이 산책하며 이런저런 이야기를 나눴다."
            show j_labe_sa
            " "
            hide j_labe_sa
            jp"번호 주실 수 있나요?"
            jp"그래도 이웃인데 번호 가지고 있으면 좋을 것 같아서요."
            hide j_su2
            show j_su3 at right
            js"좋아요"
            js"휴대폰 주세요"
            hide j_su3
            show j_su2 at right
            jp"감사합니다!"
            jp"아 맞다"
            jp"오늘 같이 산책해서 좋았어요"
            jp"조심히 들어가세요!"
            hide j_su2
            show j_su3 at right
            js"저도요, 조심히 들어가세요"
            jp"네!"
            hide j_su3
            scene black
            with fade
            scene bg j_room1
            with fade
            "그 후, 집에 돌아와서 한동안 서윤에 대해 생각했다."
            jump j_cv

                




