#d6
label d6:
    $gday_count += 1
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



#d8
#단 둘이 드라이브 
init python:
    # - 호감도 음식 추가하기
    gfood_list = ["김치 볶음밥", "김밥", "에그마요 토스트"]
    gchoice= " "
    



