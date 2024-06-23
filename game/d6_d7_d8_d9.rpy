#d6
label d6:
    scene gblack
    ga "화창한 어느날 공원에 왔다. "

    show gw_p
    gw "여태까지 갈고 닦은 실력을 봐보자."
    hide gw_p

    scene gm_ride_bike1
    
    show gw_p
    gw "자네 자전거 타는 실력이 나쁘지 않는군. 좋은 스승에게 배웠나봐."
    
    menu:
        "훌륭하신 자연 선생님덕분에 많이 배웠습니다.":
            ga "호감도 +10"
            $hogam += 10

    
        "내가 원래 운동신경이 좋아요.":
            ga "호감도 +0"
            $hogam += 0

#d7
#동아리 정기 자전거 타는 날 
label d7:
    scene black
    ga "오늘은 동아리 정기 자전거 타는 날입니다. 그동안 연습한 실력을 보여줍시다."
    
    scene gm_ride_bike2
    gp1 "어이어이 남주! 자전거 처음 아니었냐고 ! 이게 뭐야 ! 꽤나 하잖아 이녀석 !"
    gp2 "제법인데."

    show gw_p
    gm "지연 너의 특훈덕분에 칭찬 많이 들었어. 고마워! "
    gm "그.. 혹시 같이 주말에 자 전거 드라이브 안 갈래? 장소는.."

    init python:
        gspace = " "

    menu:
        "해안가 도로!" :
            gw "나쁘지 않은 선택이야."
            ga "호감도 +10"
            python:
                gspace = "해안가"

        "한강 자전거길" :
            ga "어! 한 번도 안 가봤어. 좋아!" 
            ga "호감도 +10"
            python:
                gspace = "한강"

    image gchoice_place = "background/[gspace].png"

    ga "test"

        

#d8 --> 삭제

#d9
#단 둘이 드라이브 
init python:
    # - 호감도 음식 추가하기
    gfood_list = ["김치 볶음밥", "김밥", "에그마요 토스트"]
    gchoice= " "
    

label d9:
    scene gblack
    ga "당신은 도시락을 싸려고 합니다. 뭘 만들까요?"
    menu:
        "스팸 김치 볶음밥":
            gm "역시 만들기 쉬운 김치 볶음밥"
            #볶음밥 이미지
            python:
                gchoice = gfood_list[0]

        "오이 듬뿍 김밥":
            #김밥 이미지 
            gm "김밥에는 오이가 듬뿍 들어가야 맛있지."
            python:
                gchoice = gfood_list[1]
                
        "에그마요 토스트":
            # 토스트 이미지 
            gm "역시 만들기 쉬운 에그마요."
            python:
                gchoice = gfood_list[2]


    scene gchoice_place
    gm "자연아 ! 여기야! 출발할까? "
    
    show gw_p
    gw "자 안전하게 탑시다. "
    hide gw_p

    #자전거 타는 이미지
    show gw_p
    gm "자전거 드라이빙 너무 재밌다!"
    gw "너가 자전거의 맛을 알게되어서 너무 기뻐."

    menu:
        "종종 같이 오자! 너랑 같이라 재밌는 거 같아.":
            gw "뭐야..! 빨리 뉴비 탈출해서 더 어려운 곳도 가자"
            ga "호감도 +15"
            $hogam += 15

        "나 이제 혼자서도 잘 탈 거 같은데 하하!":
            gw "나도 그렇게 생각해"
            ga "호감도 +0"
            $hogam += 0

    gw "배고프지 않아? 점심 뭐 먹지?"
    gm "오늘의 점심은 바로 내가 손수 만든 도시락!"
    gw "뭐라고 !!!!???!!"
    gm "메뉴는 바로~   [gchoice] " 
    # 음식 이미지 보여주기 
    
    if gchoice == gfood_list[0] :
            gw "맛있겠다."
            ga "호감도 +5"
            $hogam += 5
        
    elif gchoice == gfood_list[1] :
            gw "와 오이 듬뿍?? 진짜 진짜 맛있겠다!!!" 
            ga "호감도 +20"
            $hogam += 20

        
    elif gchoice == gfood_list[2] :
            gw "와 에그마요?? 나쁘지 않은데!" 
            ga "호감도 +5"
            $hogam += 5
        

    gw "만드느라 고생했겠다. 고마워 잘 먹을게."
    gm "나 사실 도시락 싸는 거 처음이야. "
    menu:
        "너랑 먹으려고 만든다고 생각하니까 너무 재밌더라.":
            gw "뭐야~ 잘 먹을게 고마워."
            ga "호감도 +10"

        "운동하고 도시락 먹으면 재밌을 것 같아서 싸봤어. 소풍 온 느낌나잖아.":
            gw "뭐야~ 잘 먹을게 고마워."
            ga "호감도 +10"

jump d11

