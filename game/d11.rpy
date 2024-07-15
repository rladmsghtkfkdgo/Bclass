label d11:
    $gday_count += 1
    # 몇 달 후 같은거 넣기
    # 교실 이미지 
    scene gblack
    $ renpy.notify('    새로운 학기     ')
    ga "새로운 학기가 시작되었습니다."
    ga "당신은 산악자전거 동아리에 남기로 하였습니다."

    scene gclassroom1
    gp1 "어 승철 잘 지냈니? 특훈 이후로는 오랜만이다. 방학동안 자전거 소홀히 하지는 않았지?"
    gm "여어~ [gp1]. 오랜만이다. 무무물론.. 맨날 탔지~ "
    gp2 "어 !!! 승철~! "
    gm "어!! [gp2]!"

    show gw_main_top
    gw "승철 !"
    gm "난희~ "
    gw "하하하 안녕"
    hide gw_main_top

    gp1 "자 그러면~ 여러분 2학기 동아리 OT를 시작하겠습니다. 새로 들어오신 분도 있으니 소개를 하자면,  .  .(생략). . . "
    gp1 "..이제 조 추첨식을 진행하겠습니다."

    ga "몇 번을 뽑을까요?"
    menu:
        "1조" :
            show gw_main_top
            gm "난희야 몇 조야?"
            gw "나는 1조"
            gm "어!!! 같은 조다! 오예 ~ ! 이번학기 동아리 활동 너무 재밋겠다!"

        "2조" :
            show gw_main_top
            gm "난희야 몇 조야?"
            gw "나는 2조"
            gm "어!!! 같은 조다! 오예 ~ ! 이번학기 동아리 활동 너무 재밋겠다!"

        "3조" :
            show gw_main_top
            gm "난희야 몇 조야?"
            gw "나는 3조"
            gm "어!!! 같은 조다! 오예 ~ ! 이번학기 동아리 활동 너무 재밋겠다!"

    gp1 "뭐야 ~ 둘이 꽤나 친해졌네. "
    gp2 "그러게. 둘이 뭐야뭐야 ~"
 
    if hogam>=0:
        gw shy "..." # 샤이 버전
    else :
        gw ".."

    scene gblack
    $ renpy.notify('    저녁    ')
    ga "저녁이 되었습니다. "

    ga "[str_question]"

    menu:
        "간다":
            $hogam += 5

        "가지 않는다":
            $hogam += 0
            
    jump d12
