label d3: 
    scene black
    ga "오늘은 학교가는 날 입니다."

    scene gclassroom2
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

        "춤추면서 달려간다.":
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
    menu :
        "쭈꾸미 볶음":
            gw "좋은데! "
            ga "호감도 +10"
            $hogam += 10


        "고구마 피자":
            gw "나쁘지 않네"
            ga "호감도 +5"
            $hogam += 5

        "마라탕":
            gw ".........음"
            ga "호감도 +0"
            $hogam += 0

        "떡볶이":
            gw ".........음...........음...........이게 최선이야?"
            ga "호감도 -20"
            $hogam += -20

    jump d4