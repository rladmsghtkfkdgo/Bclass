label d3: 
    $gday_count += 1
    scene gblack
    $ renpy.notify('다음날')
    ga "오늘은 학교가는 날 입니다."

    scene gschool_morning   #  등교길 이미지 수정
    gm "어 ! [gw]이다! 인사할까?"
    
    menu:
        "인사한다." : 
            gw "어! 안녕!"
            ga "호감도 +0"
            $hogam += 0

        "인사하지 않는다." :
            gw "뭐야 [gm]! 반갑다!"
            ga "호감도 +0"
            $hogam += 0

        "춤추면서 달려간 후 인사한다.":
            gw "누구세요?"
            ga "호감도 -10"
            $hogam += -10

    
    gm "[gw] 수업가?"
    gw "응. 이동 수업 가려고."
    gm "이동수업? 혹시 다음교시 영어야?"
    gw "어~"
    gm "뭐야 나돈데. 우리 옆반이었네. 자주 놀러가야겠다. ~ "
    gm "아 ! [gw] ! 내일 저녁 알지? 내가 저녁 사기로 한 날! "

    gw "알지알지 기억하지."
    ga "저녁은 뭘 먹자고 할까?"


    # 저녁 메뉴에 따라 다르게 보여주기.
    init python:
        gdiner = ["쭈꾸미 볶음", "하와이안 피자", "마라탕", "떡볶이"]
    
    menu :
        "[gdiner[0]]":
            gm "[gdiner[0]]으로 먹자"
            gw "좋은데! "
            ga "호감도 +10"
            $hogam += 10
            jump d4_1


        "[gdiner[1]]":
            gm "[gdiner[1]]로 먹자"
            gw "나쁘지 않네"
            ga "호감도 +0"
            $hogam += 0
            jump d4_2

        "[gdiner[2]]":
            gm "[gdiner[2]]으로 먹자"
            gw ".........음"
            ga "호감도 +0"
            $hogam += 0
            jump d4_3

        "[gdiner[3]]":
            gm "[gdiner[3]]으로 먹자"
            gw ".........음...........음...........이게 최선이야?"
            ga "호감도 -20"
            $hogam += -20
            jump d4_4

    