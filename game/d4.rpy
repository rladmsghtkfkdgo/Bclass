#d4
label d4: 
    $gday_count += 1
    scene gblack
    ga "당신은 다음날 저녁을 먹으러 왔습니다. "

    scene gstreet1
    show gw_p
    gw "배부르다~"
    gm "든든하네."
    gm "후식이나 먹으러 가자! "

    ga "후식은?"
    menu: 
        "탕후루":
            gw "..너 먹어.. 난 옆에서 구경할게. 단거 별로.. "
            ga "호감도 -10"
            $hogam += -10

        "디카페인 아메리카노":
            gw "후식 고를줄 아는 친구일세 이거. "
            ga "호감도 +5"
            $hogam += 5

        "망고 빙수":
            gw "오!!"
            ga "호감도 +15"
            $hogam += 15

