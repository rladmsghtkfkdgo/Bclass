label j_mqww: #산
    "그러고보니 서윤을 못본지 꽤 된 것 같다."
    "음.. 연락해볼까?"
    "띵동"
    "누구지?"
    "올 사람이 없는데"
    "누구세요?"
    "경찰입니다."
    "잠시 협조 부탁드립니다."
    "아..네."
    "무슨 일이 있나요?"
    "옆집 사람과 친분이 있으신가요?"
    "아,네."
    "조금.. 있어요."
    "옆집 사람과 언제 마지막으로 연락하셨나요?"
    "아.. 일주일쯤 전에 연락했었어요."
    "이상한 낌새는 없었나요?"
    "음.. 고민이 있어보이긴 했는데.."
    "제가 끼어들만한게 아닌 것 같아서 무언가를 하진 않았어요.."
    "아.. 그렇군요."
    "그 후, 경찰은 몇가지 질문을 더 하고 돌아갔다."
    "뭐지..? 옆집 사람한테 무슨 일이 있나..?"
    "경찰이 아직 복도에 있는지 희미하게 말소리가 들린다."
    "젊은 나이에 참 안됐어."
    "그러게 말이야"
    "심지어 유튜버였다며?"
    "맞아 유피아였나? 여튼 인기 많은 사람이었어."
    "악플이 뭐라고 사람까지 죽게 만드는지.. 참.."
    "시간이 더 지나자 경찰들의 말소리가 사라졌다."
    "아.. 나가..보자..."
    "어.. 진짜..?"
    "아.. 아..!"
    "안돼.."
    "그때 얘기를 들어줬더라면.."
    "안죽었을지도 모르는데..."
    "그게 뭐라고.."
    "그 후, 한참동안 멍하니 폴리스 라인이 쳐진 옆집을 바라봤다."
    #페이드 아웃 후 어두워진 집
    "아..."
    "그때 내가 들어줬더라면.."
    "..."
    "이게 다 무슨 소용이야"
    "돌아갈 수도 없는데..."
    "..."
    "띠링"
    #빛나는 선택지 창 
    "다시 시작하시겠습니까냥?"
    "어..?"
    "돌아갈 수.. 있어..?"
    "그럼 이번엔..."
    "네가 죽지 않게끔.."
    #페이드 아웃 흰색
    #게임 처음 화면으로
    "띠링"
    "유튜브 알람이 왔습니다."

label j_mqw: #길
    if ju >= 65:
        jump j_erty #결혼
    elif ju >= 45:
        jump j_rtyu #연애
    elif ju >= 30:
        jump j_tyui #친구
    else:
        jump j_yuio #배드엔딩

label j_erty:
    "어, 서윤씨 전화네?"
    "네, 여보세요?"
    "네, 여보세요"
    "혹시 오늘 시간 괜찮으세요?"
    "네, 괜찮아요!"
    "그러면 라온카페에서 3시에 봬요."
    "네, 그때 봬요!"
    show j_labe_za
    ""
    hide j_labe_za
    "앗 여기에요!"
    "안녕하세요"
    "조금 더 일찍 나올 걸 그랬네요"
    "아니에요"
    "저도 조금전에 도착했어요."
    "어디 앉으실래요?"
    "음.. 저기 앉죠"
    "좋아요"
    "혹시 오늘 부르신 이유가.."
    js "그게.."
    js "사실 저는 '유피아'라는 이름으로 활동중인 유튜버예요."
    js "요즘 많이 힘들었는데 [jp]씨 덕분에 잘 이겨낼 수 있었어요"
    "그래서 감사하다고 말하고 싶었어요"
    "아, 아니에요"
    "크게 해드린 것도 없는 걸요"
    #볼이 상기된 서윤
    "아니에요, 저한텐 정말 큰 도움이었어요."
    "혹시 00씨만 괜찮으시다면 저란 사귀어 주실래요?"
    "...!"
    "좋아요!"
    "그 후, 우리는 연인이 되었다."
    "그리고 유튜브는.."
    menu:
        "계속 하기로 했다":
            jump j_tyui
        "그만두기로 했다":
            jump j_yuio
    label j_tyui:
        "달라진 것이 잇다면 나도 방송에 종종 나온다는 것이다."
        "유피아의 방송은 일상 위주의 방송이 되었고, \n 팬들은 그런 유피아를 응원해 주었다."
        "그리고 4월 1일에는 결혼 발표 영상을 올릴 예정이다."
        "우리는 앞으로도 함께할 것이다."
        #결혼식 사진

    label j_yuio:
        "서윤, 그러니까 유피아는 마지막 영상을 올리고 유튜브를 그만두었다."
        "서윤에게 아깝지는 않냐고 묻자 서윤은 지금이 더 좋다고 답했다"
        "우리는 앞으로도 함께할 것이다."
        #결혼식 사진
label j_rtyu:
    "연애"
label j_yui:
    "친구"
label j_yuio:
    "배드엔딩"
    




