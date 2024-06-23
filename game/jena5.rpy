label j_yui:
    "자면서 꿈을 꿨다."
    "무슨 꿈이었을까?"
    menu:
        "옆집 사람이 사라지는 꿈을 꿨다.":
            show j_dream_su
            jump j_uio
        "고양이한테 가득 휩싸여 있는 꿈을 꿨다.":
            show j_dream_ca
            jump j_iop
    label j_uio:
        " "
        hide j_dream_su
        with fade
        show bg j_room1
        jp "뭔 이런 꿈을..."
        jp "음... 고양이나 보러갈까?"
        jump j_opa
    label j_iop:
        " "
        hide j_dream_ca
        with fade
        show bg j_room1
        jp "말랑한 꿈이라 좋았어."
        jp "이왕 꿈 꾼거 고양이 보러 가야겠다."
        jump j_opa
    label j_opa:
        show bg j_room_bo
        "집을 나선다."
        show bg j_room_ca2
        jp "고양이 어디있지?"
        show j_su5 at right
        jp "어?"
        "익숙한 모습이 보인다."
        jp "안녕하세요!"
        js "아.. 안녕하세요"
        "서윤의 안색이 나빠보인다."
        jp "혹시 무슨 일 있으세요?"
        show j_su7 at right
        js "아.. 그게.."
        hide j_su7
        menu:
            "털어놓는 것만으로도 괜찮아질 때가 있잖아요, 말해보세요":
                jump j_pas
            "음.. 필요하면 말해주겠지..":
                jump j_asd
        label j_pas: #길
            show j_su7 at right 
            js "사실 요즘 좀 힘들어서요.."
            hide j_su7
            show j_su5
            "그 후, 한참동안 서윤의 이야기를 들어주었다."
            $u = +15
            hide j_su5
            show j_su3 at right
            js "덕분에 많이 좋아진 것 같아요."
            js "감사합니다!"
            hide j_su3
            show j_su2 at right
            jp "아니에요, 얘기 들어줄 사람 필요하면 불러주세요."
            hide j_su2
            show j_su3 at right
            js "네! [jp]씨도요!"
            hide j_su3
            show j_su2 at right
            "서윤은 인사하고 들어갔다."
            hide j_su2
            jump j_sdf

        label j_asd: #산
            hide j_su7
            show j_su5 at right
            jp "말하기 힘드시면 다음에 말해주세요."
            js "사실.."
            "그 때, 고양이가 물을 엎어 서윤의 옷이 젖었다."
            hide j_su5
            show j_su8 at right
            js "아.."
            jp "앗, 괜찮으세요?"
            hide j_su8
            show j_su7 at right
            js "괜찮아요..."
            hide j_su7
            show j_su5 at right
            jp "근데 무슨 말 하지 않으셨어요?"
            hide j_su5
            show j_su7 at right
            js "아.. 아니예요.."
            js "먼저 들어가볼게요, 다음에 또 봬요"
            $u = -10
            jp "네, 다음에 또 봬요!"
            hide j_su7
            jump j_fds

        label j_sdf: #길
            "그 후, 고양이와 놀아주다가 집에 들어갔다."
            scene black
            with fade
            scene bg j_room1
            with fade
            jump j_dfg

            label j_fds: #산
            "그 후, 고양이와 놀아주다가 집에 들어갔다."
            scene black
            with fade
            scene bg j_room1
            with fade
            jump j_gfd
