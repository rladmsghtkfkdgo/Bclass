#gdiner = ["쭈꾸미 볶음", "하와이안 피자", "마라탕", "떡볶이"]
label d4_1:
    #호감 +10
    $renpy.notify('저녁')
    $gday_count += 1
    scene gblack
    ga "당신은 저녁으로 [gdiner[0]] 먹으러 왔습니다. "
    
    scene gdiner_jju
    gw happy "우와 ~~~! 맛있겠다!! "
    gm "맛있게 먹어!"

    jump d4_main

label d4_2:
    #호감 +0
    $renpy.notify('저녁')
    $gday_count += 1
    scene gblack
    ga "당신은 저녁으로 [gdiner[1]] 먹으러 왔습니다. "
    
    scene gdiner_hawai
    gm "맛있게 먹어!"
    gw "응 ~ 너도~"

    jump d4_main

label d4_3:
    #호감 +0
    $renpy.notify('저녁')
    $gday_count += 1
    scene gblack
    ga "당신은 저녁으로 [gdiner[2]] 먹으러 왔습니다. "
    
    scene gdiner_mara
    gm "맛있게 먹어!"
    gw "응 ~ 너도~"

    jump d4_main

label d4_4:
    #호감 - 20 
    $renpy.notify('저녁')
    $gday_count += 1
    scene gblack
    ga "당신은 저녁으로 [gdiner[3]] 먹으러 왔습니다. "
    
    scene gdiner_ttok
    gm "맛있게 먹어!"
    gw angry "응.. 너도~.."

    jump d4_main


label d4_main:
    $renpy.notify('다 먹은 후..')
    scene gstreet
    show gw_main_top
    gw "배부르다~"
    gm "든든하네."
    gm "후식이나 먹으러 가자! "

    ga "후식은?"
    menu: 
        "탕후루":
            gw angry "..너 먹어.. 난 옆에서 구경할게. 단거 별로.. "
            ga "호감도 -10"
            $hogam += -10

        "디카페인 아메리카노":
            gw "후식 고를줄 아는 친구일세 이거. "
            ga "호감도 +5"
            $hogam += 5

        "망고 빙수":
            gw happy "오!!"
            ga "호감도 +15"
            $hogam += 15

    gw happy "오늘 저녁 잘먹었어 ~"
    gm "나도 재밌었어."
    gm "조심히 들어가! "



label d4_fin:
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

    jump d5

