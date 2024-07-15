#d5
label d5:
    $ renpy.notify('    동아리 정기 모임날  ')

    $gday_count += 1
    scene gblack
    play music "audio/yujin/알람음.mp3" noloop
    ga "오늘은 동아리 정기 모임입니다."

    play music "audio/yujin/경쾌_기본.mp3" fadeout 0.5
    scene gclassroom2
    gp1 "여러분! 첫 동아리 일정으로 어디를 갈 건지 정해야합니다. "
    gp1 "각 조별로 회의해서 알려주세요.첫 공식 일정은 2주뒤로 하겠습니다. "
    gn "네 ~ "
    gp2 "저희조는 초보자가 많으니, 첫 일정은 난이도가 낮은 곳으로 가요."
    gm "나즈막 산 어때요? 거기 난이도가 높지 않다고 하던데.. "
    gp2 "좋은데! "
    gp1 "거기 작년에 가봤을 때 괜찮았지. 지금쯤이면 등나무도꽃도 많이 피었겠어. 거기로 가자!"

    show gw_main_top
    gm "난~~~~~~희! 너넨 어디로 가? 우린 나즈막산."
    gw "어! 우리도! "
    gw "그래도 남주 너는 산악자전거가 처음이니까.. 같이 연습할래? 이번주 토요일 시간 비워."
    
    menu:
        "어! 알았어! 고마워! ":
            gw happy "후후후"
            ga "호감도 +10"
            $hogam += 10

        "나 그때 약속있는데":
            gw angry "그럼 뭐 어떡하게? 혼자 연습 잘할 수 있어?"
            gm "아냐.. 약속 미룰게."
            ga "호감도 - 15"
            $hogam += -15

        


        "이번주? 가족이랑 놀러가기로 했는데..":
            gw angry "..........."
            gm "근데 당일치기라 미룰 수 있어."
            gw "..........응? 그래도 괜찮겠어?"
            ga "호감도 -5"
            $hogam += -5

    hide gw_main_top
    scene gblack
    stop music

    $ renpy.notify('    집  ')
    gm "오늘도 재밌는 하루였다. "

    play music "audio/yujin/알람음.mp3" noloop
    ga "[str_question]"

    menu:
        "간다":
            $hogam += 10
            ga "당신은 좀 더 건강해지기 위해 밖으로 나갔습니다.."

        "가지 않는다":
            $hogam += 0

    jump d6