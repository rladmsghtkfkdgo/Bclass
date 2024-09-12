label d9:
    $gday_count += 1
    $ renpy.notify('    등굣길      ')
    init python:
        gdrink = ['단백질쉐이크', '옥수수 수염차', '달달한 커피', '신상 고농축 망고 주스']
        gdrink_img_list =["단백질쉐이크.png", "food/[gdrink[1]].png", "food/[gdrink[2]].png", "food/[gdrink[3]].png" ]
        gd_choice = " "

    scene gblack
    play music "audio/yujin/알람음.mp3" noloop
    ga "학교가는 날입니다.편의점에 들려서 마실 것을 삽시다."

    play music "audio/yujin/경쾌_기본.mp3" fadeout 0.5
    scene gmarket
    gm "오늘은 어떤 마실거를 살까.."
    ga "어떤 음료수를 살까요?"

    menu:
        "[gdrink[0]]":
            python:
                gd_choice = gdrink[0]

            image drink_gift = "[gdrink_img_list[0]]"
            #image drink_gift = "[gd_choice].png" 
            gm "근손실 오면 안돼. 마침 1+1이니 난희 줘야겠다."

            

        "[gdrink[1]]" :
            python:
                gd_choice = gdrink[1]
            #image drink_gift = "food/단백질쉐이크.png"
            gm "무난하게..! 마침 1+1이니 난희 줘야겠다."

        "[gdrink[2]]":
            python:
                gd_choice = gdrink[2]
            #image drink_gift = "[gd_choice].png" 
            gm "현대인의 필수 영양소! 카페인 채우자. 마침 1+1이니 난희 줘야겠다."

        "[gdrink[3]]":
            python:
                gd_choice = gdrink[3]
            #image drink_gift = "[gd_choice].png" 
            gm "이거 새로 나온거잖아! 마침 1+1이니 난희 줘야겠다."

    play music "audio/yujin/웅성웅성.mp3" fadeout 0.5
    scene gschool_morning
    gm "어! 난희다. "
    ga "어떻게 인사할까요?"
    
    menu:
        "조용히 다가가서 놀래킨다. ":
            play music "audio/yujin/놀람_남자.mp3" noloop
            gm "...........왁!!!!!!!!!!! "
            gw "아잇!!!!!!!!!!!!!!!!!!!! 깜짝이야. "
            ga "호감도 + 0 "
            $hogam += 0
        

        "타타닥 달려가서 인사한다. ":
            gw "어? 승철아~ 반가워. "
            ga "호감도 + 0 "
            $hogam += 0

            

        "지금 위치에서 우렁차게 \"이난희!\"하고 부른다. ":
            play music "audio/yujin/놀람_남자2.mp3" noloop
            gm "이!!!!!!난!!!!!!!!!!!!희!!!!!!!!!"
            gp1 "뭐야 쟤 승철이아니야? 아침부터 우렁차네."
            gw angry ".............."
            gw angry "..............빨리 가자."
            ga "호감도 - 10 "
            gm "어어 어디가!! 같이 가!"
            $hogam += -10

            

    if gd_choice == gdrink[0]:
    #show drink_gift
    #show gdrink_img[0]
    #show drink_gift
        show gdan
        gm "난희야 이거 선물이야. "
        gm "[gd_choice] 마셔. 1+1이더라고. 나 2개까지 못 마셔. "
        gw happy "[gd_choice]! 고마워 잘 마실게!"
        $hogam += 20

        jump d10
    

    elif gd_choice == gdrink[1]:
        #show gdrink_img[1]
        show goak
        #show drink_gift
        gm "난희야 이거 선물이야. "
        gm "[gd_choice] 마셔. 1+1이더라고. 나 2개까지 못 마셔. "
        gw angry "[gd_choice] 고마워."
        $hogam += -5

        jump d10

#고카페인

    elif gd_choice == gdrink[2]:
        #show gdrink_img[2]
        #show drink_gift
        show gcoff
        gm "난희야 이거 선물이야. "
        gm "[gd_choice] 마셔. 1+1이더라고. 나 2개까지 못 마셔. "
        gw "[gd_choice] 고마워 잘 마실게."
        $hogam += 5

        jump d10

    elif gd_choice == gdrink[3]:
        show gmang
        #show gdrink_img[3]
        #show drink_gift
        gm "난희야 이거 선물이야. "
        gm "[gd_choice] 마셔. 1+1이더라고. 나 2개까지 못 마셔. "
        gw angry "[gd_choice]! 고마워...."
        $hogam += -20

        jump d10


