#d10 --> 삭제
#label d10: 





#d11
label d11: 
    # 팝업창 --> 알람
    #편의점 음료 진열대 사진 
    init python:
        gdrink = ['단백질 쉐이크', '오렌지 주스', '달달한 커피', '신상 망고샤인 음료']
        gd_choice = " "
    scene black
    ga "학교가는 날입니다.편의점에 들려서 마실 것을 삽시다."

    #편의점 음료 진열대 이미지
    gm "오늘은 어떤 마실거를 살까.."

    ga "어떤 음료수를 살까요?"
    menu:
        "단백질 쉐이크":
            python:
                gd_choice = gdrink[0]
                # 호감도 + ?
            gm "근손실 오면 안돼. 마침 1+1이니 난희 줘야겠다."

        "오렌지 주스" :
            python:
                gd_choice = gdrink[1]
                # 호감도 + ?
            gm "아침엔 상쾌하게 오렌지 충전이지.마침 1+1이니 난희 줘야겠다."

        "달달한 커피":
            python:
                gd_choice = gdrink[2]
                # 호감도 + ?
            gm "현대인의 필수 영양소! 카페인 채우자. 마침 1+1이니 난희 줘야겠다."

        "신상 망고샤인머스켓 주스":
            python:
                gd_choice = gdrink[3]
                # 호감도 + ?
            gm "현대인의 필수 영양소! 마침 1+1이니 난희 줘야겠다."


    #학교 등교하는 이미지 
    gm "어! 난희다. "
    ga "어떻게 인사할까요?"
    
    menu:
        "조용히 다가가서 놀래킨다. ":
            gm "...........왁!!!!!!!!!!! "
            gw "아잇!!!!!!!!!!!!!!!!!!!! 깜짝이야. "
            ga "호감도 + 0 "
            $hogam += 0
        
            jump d11_1

        "타타닥 달려가서 인사한다. ":
            gw "어? 승철아~ 반가워. "
            ga "호감도 + 0 "
            $hogam += 0

            jump d11_2

        "지금 위치에서 우렁차게 \"이난희!\"하고 부른다. ":
            gm "이!!!!!!난!!!!!!!!!!!!희!!!!!!!!!"
            gp1 "뭐야 쟤 승철이아니야? 아침부터 우렁차네."
            gw ".............."
            gw "..............빨리 가자."
            ga "호감도 - 10 "
            gm "어어 어디가!! 같이 가!"
            $hogam += -10

            jump d11_3


# 캐릭터 시트 보고 반응 추가하기 
#단백질 
label d11_1 : 
    show gw_p
    gm "난희야 이거 선물이야. "
    gm "[gd_choice] 마셔. 1+1이더라고. 나 2개까지 못 마셔. "
    ga "[gd_choice]! 고마워 잘 마실게!"
    $hogam += 20

    jump d12
    
#오렌지
label d11_2 : 
    show gw_p
    gm "난희야 이거 선물이야. "
    gm "[gd_choice] 마셔. 1+1이더라고. 나 2개까지 못 마셔. "
    ga "[gd_choice] 고마워."
    $hogam += -5

    jump d12

#고카페인
label d11_3 : 
    show gw_p
    gm "난희야 이거 선물이야. "
    gm "[gd_choice] 마셔. 1+1이더라고. 나 2개까지 못 마셔. "
    ga "[gd_choice] 고마워 잘 마실게."
    $hogam += 5

    jump d12

#신상 망고 샤인
label d11_4 : 
    show gw_p
    gm "난희야 이거 선물이야. "
    gm "[gd_choice] 마셔. 1+1이더라고. 나 2개까지 못 마셔. "
    ga "[gd_choice]! 고마워...."
    $hogam += -20

    jump d12

label d12:
    scene black
    ga "몇 주후 방학이 되었습니다."
    
    gf ""

    jump d13