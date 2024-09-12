#d7
#동아리 정기 자전거 타는 날 
label d7:
    $gday_count += 1
    $ renpy.notify('    동아리 정기 활동일  ')
    scene black
    play music "audio/yujin/알람음.mp3" noloop
    ga "오늘은 동아리 정기 자전거 타는 날입니다. 그동안 연습한 실력을 보여줍시다."
    
    play music "audio/yujin/경쾌_빠른.mp3" fadeout 0.5
    scene gm_ride_bike3
    # 몇 초동안 보여주기 ? 
    gp1 "어이어이 남주! 자전거 처음 아니었냐고 ! 이게 뭐야 ! 꽤나 하잖아 이녀석 !"
    gp2 "제법인데."

    scene gpark
    show gbike at right
    show gw_main_top
    gm "난희 너의 특훈덕분에 칭찬 많이 들었어. 고마워! "
    gm "덕분에 굉장히 뿌듯하고 기분이 좋아."
    gw happy "별말씀을 후후"
    gm "그.. 혹시 같이 주말에 자 전거 드라이브 안 갈래? 장소는.."

    init python:
        gspace = " "

    menu:
        "해안가 자전거 도로" :
            gw "나쁘지 않은 선택이야."
            python:
                gspace = "해안가"

        "한강 자전거길" :
            gw "어! 한 번도 안 가봤어. 좋아!" 
            python:
                gspace = "한강"

    image gchoice_place = "background/[gspace].png"

    gw "주말에 그럼 늘 보던 그 곳에서 만나자. 시간은 10시 어때?"
    gm "오케이 ~ "
    stop music

    scene groom
    $renpy.notify('집')
    gm "오늘도 즐거웠다.  "
    play music "audio/yujin/알람음.mp3" noloop
    ga "[str_question]"

    menu:
        "간다":
            $hogam += 5
            ga "당신은 운동을 하러 밖으로 나갔습니다.."

        "가지 않는다":
            $hogam += 0


    jump d8
