#d6
label d6:
    $ renpy.notify('주말')
    $gday_count += 1
    scene gblack
    ga "화창한 어느날 공원. "

    show gw_main_top
    gw "여태까지 갈고 닦은 실력을 보여줄래?"
    hide gw_main_top


    scene gm_ride_bike

    show gw_main_top
    gw "자네 자전거 타는 실력이 나쁘지 않군. 좋은 스승에게 배웠나봐?"
    
    menu:
        "훌륭하신 [gw] 선생님꼐 많이 배웠습니다.":
            ga "호감도 +10"
            $hogam += 10

    
        "내가 원래 운동신경이 훌륭하오.":
            ga "호감도 +0"
            $hogam += 0

    gw "이정도면 다음 동아리 정기 모임에서는 문제없겠어."
    gw "잘탈 수 있지?"
    gm "당연하지."

    menu:
        "먼저 집에가. 나는 좀만 더 연습하다가 갈게":
            gw "너무 무리하지는 마라!"
            ga "호감도 + 10"
            $hogam += 10

        "빨리 집에 가자. 피곤하다. 내일 학교 가려면 쉬어야지. ":
            gw "그래"
            ga "호감도 + 0"
            $hogam += 0
        
        "나는 저녁 약속이 있어서 먼저 가~":
            gw "그래 내일 보자."
            ga "호감도 - 20"
            $hogam += -20

    jump d7



