label d8:
    $gday_count += 1
    $ renpy.notify('어느날 아침')
    init python:
    # - 호감도 음식 추가하기
        gfood_lunch = ["김치 볶음밥", "김밥", "샌드위치", "불향 가득 짬뽕밥"]
        gchoice= " "

    scene gblack
    ga "당신은 점심 도시락을 싸려고 합니다. 뭘 만들까요?"

    menu:
        #김치 볶음밥
        "[gfood_lunch[0]]":
            gm "역시 만들기 쉬운 김치 볶음밥"
            python:
                gchoice = gfood_lunch[0]
            image gchoice_food = "food/[gfood_lunch[0]].png"

        "[gfood_lunch[1]]": 
            gm "김밥에는 오이가 듬뿍 들어가야 맛있지."
            python:
                gchoice = gfood_lunch[1]
            image gchoice_food = "food/[gfood_lunch[1]].png"
                
        "[gfood_lunch[2]]":
            gm "역시 만들기 쉬운 샌드위치."
            python:
                gchoice = gfood_lunch[2]
            image gchoice_food = "food/[gfood_lunch[2]].png"
                
        "[gfood_lunch[3]]":
            gm "역시 운동하고 나서 먹는 든든한 짬뽕밥."
            python:
                gchoice = gfood_lunch[3]
            image gchoice_food = "food/[gfood_lunch[3]].png"
                

    $ renpy.notify('약속 장소')
    scene gchoice_place
    gm "자연아 ! 여기야! 출발할까? "
    
    show gbike at right
    show gw_trainng 
    gw "자 안전하게 타자구~ "
    hide gw_trainng
    
    scene gm_ride_bike3     # 몇 초동안 보여주기
    gm "자전거 드라이빙 너무 재밌다!"
    gw happy "너가 자전거 타기의 즐거움을 알게 되어서 너무 기뻐."

    scene gchoice_place
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
    gw happy "뭐라고 !!!!???!!"
    gm "메뉴는 바로~  [gchoice]! " 
    # 음식 이미지 보여주기 
    
    if gchoice == gfood_lunch[0] :
        #scene gchoice_food
        scene grice
        gw "맛있겠다."
        ga "호감도 +5"
        $hogam += 5
        
    elif gchoice == gfood_lunch[1] :
        #scene gchoice_food
        scene gkimbab
        gw happy "와 오이 듬뿍?? 진짜 진짜 맛있겠다!!!" 
        ga "호감도 +20"
        $hogam += 20

        
    elif gchoice == gfood_lunch[2] :
        #scene gchoice_food
        #scene gsandwitch2
        show gsandwitch
        gw "와 샌드위치?? 나쁘지 않은데!" 
        ga "호감도 +5"
        $hogam += 5
        
    elif gchoice == gfood_lunch[3] :
        #scene gchoice_food
        scene gzzanmbbong
        gw angry "[gfood_lunch[3]]?? 음.. 잘먹을게.." 
        ga "호감도 - 20"
        $hogam += -20
        

    gw "만드느라 고생했겠다. 고마워 잘 먹을게."
    gm "나 사실 도시락 싸는 거 처음이야. "
    
    menu:
        "너랑 먹으려고 만든다고 생각하니까 너무 재밌더라.":
            gw happy "뭐야~ 잘 먹을게 고마워."
            ga "호감도 +10"
            $hogam += 10

        "운동하고 도시락 먹으면 재밌을 것 같아서 싸봤어. 소풍 온 느낌나잖아.":
            gw happy "뭐야~ 잘 먹을게 고마워."
            ga "호감도 +10"
            $hogam += 10


    scene groom
    $renpy.notify('집')
    gm "오늘도 즐거웠다.  "
    ga "[str_question]"

    menu:
        "간다":
            $hogam += 5
            ga "당신은 운동을 하러 밖으로 나갔습니다.."

        "가지 않는다":
            $hogam += 0


    jump d9