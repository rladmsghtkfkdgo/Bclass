label j_mqww: #산
    scene black
    with fade
    scene bg j_room1
    with fade
    "그러고보니 서윤을 못본지 꽤 된 것 같다."
    jp "음.. 연락해볼까?"
    play sound "j_door.ogg"
    "띵동"
    jp "누구지?"
    jp "올 사람이 없는데"
    jp "누구세요?"
    show bg j_room_bo1
    show j_pol
    $ renpy.music.stop(channel="music", fadeout=20.0)
    jg "경찰입니다."
    jg "잠시 협조 부탁드립니다."
    jp "아..네."
    jp "무슨 일이 있나요?"
    jg "옆집 사람과 친분이 있으신가요?"
    jp "아,네."
    jp "조금.. 있어요."
    jg "옆집 사람과 언제 마지막으로 연락하셨나요?"
    jp "아.. 일주일쯤 전에 연락했었어요."
    jg "이상한 낌새는 없었나요?"
    jp "음.. 고민이 있어보이긴 했는데.."
    jp "제가 끼어들만한게 아닌 것 같아서 무언가를 하진 않았어요.."
    jg "아.. 그렇군요."
    "그 후, 경찰은 몇가지 질문을 더 하고 돌아갔다."
    hide j_pol
    show bg j_room1
    jp "뭐지..? 옆집 사람한테 무슨 일이 있나..?"
    "경찰이 아직 복도에 있는지 희미하게 말소리가 들린다."
    play music "j_die.ogg"
    jg1 "젊은 나이에 참 안됐어."
    jg2 "그러게 말이야"
    jg1 "심지어 유튜버였다며?"
    jg2 "맞아 유피아였나? 여튼 인기 많은 사람이었어."
    jg1 "악플이 뭐라고 사람까지 죽게 만드는지.. 참.."
    "시간이 더 지나자 경찰들의 말소리가 사라졌다."
    jp "아.. 나가..보자..."
    show bg j_room_bo2
    jp "어.. 진짜..?"
    jp "아.. 아..!"
    jp "안돼.."
    scene bg j_room_bo3
    with fade
    jp "그때 얘기를 들어줬더라면.."
    jp "안죽었을지도 모르는데..."
    jp "그게 뭐라고.."
    "그 후, 한참동안 멍하니 폴리스 라인이 쳐진 옆집을 바라봤다."
    scene black
    with fade 
    scene bg j_room01
    with fade
    jp "아..."
    jp "그때 내가 들어줬더라면.."
    scene bg j_room02
    with fade
    jp "..."
    jp "이게 다 무슨 소용이야"
    jp "돌아갈 수도 없는데..."
    scene bg j_room03
    with fade
    "..."
    " "
    scene black
    with fade
    "diEngn_00.후회"
    scene bg j_room03
    with fade
    " "
    show j_mes_ti
    " "
    hide j_mes_ti
    show j_mes_1
    " "
    jp "어..?"
    jp "돌아갈 수.. 있어..?"
    jp "그럼..."
    jp "이번엔.."
    jp "..."
    hide j_mes_1
    show j_mes_2
    $ renpy.music.stop(channel="music", fadeout=5.0)
    scene bg j_white
    with fade
    " "
    " "
    scene bg j_room1
    with fade
    jump jn
    #게임 처음 화면으로
    #"띠링"
    #"유튜브 알람이 왔습니다."

label j_mqw: #길
    if ju >= 65:
        jump j_erty #결혼
    elif ju >= 45:
        jump j_rtyu #연애
    else:
        jump j_tyuiw #친구

label j_erty:
    jp "어, 서윤씨 전화네?"
    jp "네, 여보세요?"
    show j_su3 at right
    js "네, 여보세요"
    js "혹시 오늘 시간 괜찮으세요?"
    hide j_su3
    show j_su2 at right
    jp "네, 괜찮아요!"
    hide j_su2
    show j_su3 at right
    js "그러면 라온카페에서 3시에 봬요."
    hide j_su3
    show j_su2 at right
    jp "네, 그때 봬요!"
    hide j_su2
    show bg j_room_en
    show j_labe_za
    ""
    hide j_labe_za
    show j_su3 at right
    js "앗 여기에요!"
    hide j_su3
    show j_su2 at right
    jp "안녕하세요"
    jp "조금 더 일찍 나올 걸 그랬네요"
    hide j_su2
    show j_su3 at right
    js "아니에요"
    js "저도 조금전에 도착했어요."
    js "어디 앉으실래요?"
    hide j_su3
    show j_su2 at right
    jp "음.. 저기 앉죠"
    hide j_su2
    show j_su3 at right
    js "좋아요"
    hide j_su3
    show j_su2 at right
    jp "혹시 오늘 부르신 이유가.."
    hide j_su2
    show j_su3 at right
    js "그게.."
    js "사실 저는 '유피아'라는 이름으로 활동중인 유튜버예요."
    js "요즘 많이 힘들었는데 [jp]씨 덕분에 잘 이겨낼 수 있었어요"
    js "그래서 감사하다고 말하고 싶었어요"
    hide j_su3
    show j_su2 at right
    jp "아, 아니에요"
    jp "크게 해드린 것도 없는 걸요"
    hide j_su2
    show j_su3 at right
    #볼이 상기된 서윤
    js "아니에요, 저한텐 정말 큰 도움이었어요."
    js "혹시 [jp]씨만 괜찮으시다면 저와 사귀어 주실래요?"
    hide j_su3
    show j_su2 at right
    jp "...!"
    jp "좋아요!"
    hide j_su2
    show j_su3 at right
    scene black
    with fade
    scene bg j_room1
    with fade
    "그 후, 우리는 연인이 되었다."
    "그리고 유튜브는.."
    menu:
        "계속 하기로 했다":
            jump j_tyuir
        "그만두기로 했다":
            jump j_yuio
    label j_tyuir:
        "계속 하기로 했다"
        "달라진 것이 있다면 나도 방송에 종종 나온다는 것이다."
        "유피아의 방송은 일상 위주의 방송이 되었고, \n 팬들은 그런 유피아를 응원해 주었다."
        "그리고 4월 1일에는 결혼 발표 영상을 올릴 예정이다."
        scene black
        with fade
        scene bg j_room_we
        with fade
        "우리는 앞으로도 함께할 것이다."
        " "
        " "
        scene black
        with fade
        scene bg j_end_01 at right
        with fade
        $ renpy.pause(7.0)
            

        return
        
    label j_yuio:
        "그만두기로 했다"
        "서윤, 그러니까 유피아는 마지막 영상을 올리고 유튜브를 그만두었다."
        "서윤에게 아깝지는 않냐고 묻자 서윤은 지금이 더 좋다고 답했다"
        scene black
        with fade
        scene bg j_room_we
        with fade
        "우리는 앞으로도 함께할 것이다."
        " "
        " "
        "Ending_02.행복한 결혼"
        return

label j_rtyu:
    #"연애"
    jp "어, 서윤씨 전화네?"
    jp "네, 여보세요?"
    show j_su3 at right
    js "네, 여보세요"
    js "혹시 오늘 시간 괜찮으세요?"
    hide j_su3
    show j_su2 at right
    jp "네, 괜찮아요!"
    hide j_su2
    show j_su3 at right
    js "그러면 라온카페에서 3시에 봬요."
    hide j_su3
    show j_su2 at right
    jp "네, 그때 봬요!"
    hide j_su2
    show bg j_room_en
    show j_labe_za
    ""
    hide j_labe_za
    show j_su3 at right
    js "앗 여기에요!"
    hide j_su3
    show j_su2 at right
    jp "안녕하세요"
    jp "조금 더 일찍 나올 걸 그랬네요"
    hide j_su2
    show j_su3 at right
    js "아니에요"
    js "저도 조금전에 도착했어요."
    js "어디 앉으실래요?"
    hide j_su3
    show j_su2 at right
    jp "음.. 저기 앉죠"
    hide j_su2
    show j_su3 at right
    js "좋아요"
    hide j_su3
    show j_su2 at right
    jp "혹시 오늘 부르신 이유가.."
    hide j_su2
    show j_su3 at right
    js "그게.."
    js "사실 저는 '유피아'라는 이름으로 활동중인 유튜버예요."
    js "요즘 많이 힘들었는데 [jp]씨 덕분에 잘 이겨낼 수 있었어요"
    js "그래서 감사하다고 말하고 싶었어요"
    hide j_su3
    show j_su2 at right
    jp "아, 아니에요"
    jp "크게 해드린 것도 없는 걸요"
    hide j_su2
    show j_su3 at right
    #볼이 상기된 서윤
    js "아니에요, 저한텐 정말 큰 도움이었어요."
    js "혹시 [jp]씨만 괜찮으시다면 저와 사귀어 주실래요?"
    hide j_su3
    show j_su2 at right
    jp "...!"
    jp "좋아요!"
    hide j_su2
    show j_su3 at right
    scene black
    with fade
    scene bg j_room1
    with fade
    "그 후, 우리는 연인이 되었다."
    "서윤은 계속해서 유튜브를 하고있다."
    "시간이 지나며 악플도 사그라들었다."
    "같이 힘든 시기를 이겨내며 우리 사이는 더 가까워졌다."
    scene black
    with fade
    scene bg j_ending_03 at right
    with fade
    "요즘은 데이트를 하며 시간을 보낸다."
    "앞으로도 이런 날이 계속되길."
    
    scene black
    with fade
    scene bg j_end_03 at right
    with fade
    $ renpy.pause(7.0)
            

    return



label j_tyuiw: #친구
    jp "어, 서윤씨 전화네?"
    jp "네, 여보세요?"
    show j_su3 at right
    js "네, 여보세요"
    js "혹시 오늘 시간 괜찮으세요?"
    hide j_su3
    show j_su2 at right
    jp "네, 괜찮아요!"
    hide j_su2
    show j_su3 at right
    js "그러면 라온카페에서 3시에 봬요."
    hide j_su3
    show j_su2 at right
    jp "네, 그때 봬요!"
    hide j_su2
    show bg j_room_en
    show j_labe_za
    ""
    hide j_labe_za
    show j_su3 at right
    js "앗 여기에요!"
    hide j_su3
    show j_su2 at right
    jp "안녕하세요"
    jp "조금 더 일찍 나올 걸 그랬네요"
    hide j_su2
    show j_su3 at right
    js "아니에요"
    js "저도 조금전에 도착했어요."
    js "어디 앉으실래요?"
    hide j_su3
    show j_su2 at right
    jp "음.. 저기 앉죠"
    hide j_su2
    show j_su3 at right
    js "좋아요"
    hide j_su3
    show j_su2 at right
    jp "혹시 오늘 부르신 이유가.."
    hide j_su2
    show j_su3 at right
    js "그게.."
    js "사실 저는 '유피아'라는 이름으로 활동중인 유튜버예요."
    js "요즘 많이 힘들었는데 [jp]씨 덕분에 잘 이겨낼 수 있었어요"
    js "그래서 감사하다고 말하고 싶었어요"
    hide j_su3
    show j_su2 at right
    jp "아, 아니에요"
    jp "크게 해드린 것도 없는 걸요"
    hide j_su2
    show j_su3 at right
    js "아니에요, 저한텐 정말 큰 도움이었어요."
    js "혹시 [jp]씨만 괜찮으시다면 저와 더 친하게 지내주실래요?"
    hide j_su3
    show j_su2 at right
    jp "좋아요!"
    hide j_su2
    show j_su3 at right
    scene black
    with fade
    scene bg j_room1
    with fade
    "그 후, 우리는 친구가 되었다."
    "서윤은 악플을 잘 이겨내고 유튜브를 이어나가고 있다."
    "종종 서윤의 유튜브를 보며 연락을 주고받곤 한다"
    "그러다가 가끔 마주치면 함께 고양이를 놀아주기도한다."
    "가끔이지만 만나면 즐거운 애다."
    "Ending_04.가끔 연락하는 애"
    

    




