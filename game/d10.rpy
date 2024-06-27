# 캐릭터 시트 보고 반응 추가하기 
#단백질 
label d10_1 : 
    $gday_count += 1
    show gw_p
    gm "난희야 이거 선물이야. "
    gm "[gd_choice] 마셔. 1+1이더라고. 나 2개까지 못 마셔. "
    ga "[gd_choice]! 고마워 잘 마실게!"
    $hogam += 20

    jump d11
    
#오렌지
label d10_2 : 
    $gday_count += 1
    show gw_p
    gm "난희야 이거 선물이야. "
    gm "[gd_choice] 마셔. 1+1이더라고. 나 2개까지 못 마셔. "
    ga "[gd_choice] 고마워."
    $hogam += -5

    jump d11

#고카페인
label d10_3 : 
    $gday_count += 1
    show gw_p
    gm "난희야 이거 선물이야. "
    gm "[gd_choice] 마셔. 1+1이더라고. 나 2개까지 못 마셔. "
    ga "[gd_choice] 고마워 잘 마실게."
    $hogam += 5

    jump d11

#신상 망고 샤인
label d10_4 : 
    $gday_count += 1
    show gw_p
    gm "난희야 이거 선물이야. "
    gm "[gd_choice] 마셔. 1+1이더라고. 나 2개까지 못 마셔. "
    ga "[gd_choice]! 고마워...."
    $hogam += -20

    jump d11

