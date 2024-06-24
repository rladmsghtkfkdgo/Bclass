label d13:
    # 몇 달 후 같은거 넣기
    # 교실 이미지 
    scene gblack
    ga "새로운 학기가 시작되었습니다."
    ga "당신은 산악자전거 동아리에 남기로 하였습니다."

    scene gclassroom1
    gp1 "어 승철 잘 지냈니 오랜만이다. 방학동안 자전거 특훈은 했어?"
    gm "여어~ [gp1]. 오랜만이다"
    gp2 "어 !!! 승철~! "
    gm "어!! [gp2]!"

    show gw_p
    gm "난희~ 아침에도 봤지만 하이하이 ~ "
    gw "하하하 안녕"
    hide gw_p

    gp1 "여러분 2학기 동아리 OT를 시작하겠습니다. 새로 들어오신 분도 있으니 소개를 하자면,  .  .(생략). . . "
    gp1 "아무튼 이제 조 추첨식을 진행하겠습니다."

    ga "몇 번을 뽑을까요?"
    menu:
        "1조" :
            show gw_p
            gm "난희야 몇 조야?"
            gw "나는 1조"
            gm "어!!! 같은 조다! 오예 ~ ! 이번학기 동아리 활동 너무 재밋겠다!"

        "2조" :
            show gw_p
            gm "난희야 몇 조야?"
            gw "나는 1조"
            gm "어!!! 같은 조다! 오예 ~ ! 이번학기 동아리 활동 너무 재밋겠다!"

        "3조" :
            show gw_p
            gm "난희야 몇 조야?"
            gw "나는 1조"
            gm "어!!! 같은 조다! 오예 ~ ! 이번학기 동아리 활동 너무 재밋겠다!"

    gp1 "뭐야 ~ 둘이 꽤나 친해졌네. "
    gp2 "그러게. 둘이 뭐야뭐야 ~"

    
    # 호감도가 일정수준 이상이면 난희가 샤이 하는 이미지 보여주기. 아니라면 그냥 난희다. 
    if hogam>=100:
        show gw_p # 샤이 버전
    else :
        show gw_p

    scene gblack
    ga "저녁이 되었습니다. "

    # 카톡화면 
    gw "오늘 런닝갈거임?"
    
    menu:
        "간다.":
            gm "레츠고~"
        "안 간다.":
            gm "오늘은 쉴래."

    #둘이 함께 런닝하는 뒷모습.

    jump d14


label d14:
    ga "오늘은 2학기 정기 동아리 산악회입니다. "

    gp1 "자자! 다들 항상 중요한건 뭐다? 안전이다. 조심히 항상 조심히 탑시다. "
    gm "예압 !"

    #대충 산 이미지 
    gw "승철.. 이제 혼자 잘 타네.. 뿌듯하다."

    # 소리 --> 끼이이익 쾅 하는 소리 넣기
    gw "으악 !"
    gm "뭐야 난희야!!"
    gp1 "난희야!! 괜찮아??"
    gp2 "난희!"

    gw "으악....아.. 쪽팔리다. 이런실수를 하다니.."
    gm "난희야! 무릎에서 피나!"

    gw "어쩐지 아프더라.. 피가 났구나.. 많이 나네.. 으악."
    gm "안되겠다. 내려가자 먼저. 제가 난희 데리고 먼저 내려갈게요. 계획대로 다 타고 조심히 오세요."
    gw "뭐? 승철아 그러면 너는 완주 못하잖아."
    gm "아냐 괜찮아. 친구가 아프다는데, 어떻게 그냥 가. 가자. 내려가는거 도와줄게."
    gw "승철아.. 진짜 고마워. 미안해. 진짜 고마워."
    gm "고마우면 뭐 ~ 밥이라도 사주던가~"
    gw "그래 내일 시간 돼? 내일 먹자."

    ga "당신에 대한 난희의 호감도가 +30 상승했습니다."
    # 호감도 변수 올리기

    jump d15