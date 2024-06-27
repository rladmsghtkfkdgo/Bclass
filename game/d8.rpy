label d8:
    $gday_count += 1
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

    jump d9