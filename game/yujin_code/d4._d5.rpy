#d4
label d4_1_밥_약속의_날: 
    #뭘 먹을지에 따라 다른 사진 띄우기
    scene classroom1
    m "내일이네.. 저녁 뭐먹자고 하지?"
    menu :
        "쭈꾸미 볶음":
            w "좋은데! "
            sys "호감도 +10"

        "짬뽕":
            w "나 매운거 잘못먹는데..가서 짜장면 먹을게"
            sys "호감도 -10"

    scene street1
    w "나쁘지 않은 식사였다. 그치?"
    m "든든하네."
    m "후식이나 먹으러 가자! "

    sys "후식은?"
    menu: 
        "탕후루":
            w "..너 먹어.. 난 옆에서 구경할게. 단거 별로.. "
            sys "호감도 -10"

        "디카페인 아메리카노":
            w "후식 고를줄 아는 친구일세 이거. "
            sys "호감도 +5"

#d5
label d5_동아리_정기_모임:
    scene classroom2
    sys "오늘은 동아리 정기 모임입니다."
    p "
    여러분! 첫 동아리 일정으로 어디를 갈 건지 정해야합니다. 
    각 조별로 회의해서 알려주세요.첫 공식 일정은 2주뒤로 하겠습니다. "

    p "저희조는 초보자가 많으니, 첫 일정은 난이도가 낮은 곳으로 가요."
    m "나즈막 산 어때요? 거기 난이도가 높지 않다고 하던데.. "
    p "That's a good idea! "
    p "거기 작년에 가봤을 때 괜찮았지. 지금쯤이면 등나무도꽃도 많이 피었겠어. 거기로 가자!"

    m "자연아 너넨 어디로 가? 우린 나즈막산."
    w "어! 우리도! "
    w "그래도 남주 너는 산악자전거가 처음이니까.. 연습하러 갑시다. 이번주 토요일 시간 비워."
    m "어! 알았어! 고마워! "

    # 운동갈까요? 



jump d6