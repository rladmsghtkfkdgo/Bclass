

# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"


# 여기에서부터 게임이 시작합니다.
# 프롤로그 
label start:
    scene room
    a "지금 우리 동네에 핫한 동호회!
            이런 동호회는 어때요?"

    #alert "이런 동호회는 어때요? "

    m "운동 동호회? 이번에는 좀 괜찮은 곳일까? "
    m "매번 어떻게 가입하는 곳마다 사건이 터지냐..  "

    menu: 
        "동호회에 가입한다":
            m "그래, 가입만 해보자"

        "동호회에 가입하지 않는다.":
            m "가입만 하는건데 뭐 어때.. 가입해보자!"
    

    label alert:
        a "박승철님이 메세지를 보냈습니다. "
        #show image = "카톡 이미지.png"

        m "아 맞다! 내일 동아리 어디 가입하지?"
        m ".. 내일 구경해보고 결정하자 ~ "

    #==========================================================
    # Day 1
    jump d1_first
    jump d1

    # Day 2
    jump d2_만나기_전
    jump d2_공원
    jump d2_저녁
    jump d2_집

    # Day 3
    jump d3_학교

    # Day 4
    jump d4_1_밥_약속의_날

    # Day 5
    jump d5_동아리_정기_모임

    # Day 6
    jump d6
    
    # Day 7
    jump d7

    # Day 8
    #jump d8

    # Day 9
    jump d9
return

    
