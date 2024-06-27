#d7
#동아리 정기 자전거 타는 날 
label d7:
    $gday_count += 1
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
