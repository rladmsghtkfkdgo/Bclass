
label d16:
    #단풍진 산.
    gw "와 경치 진짜 너무 끝내준다. "
    gm "그니까 ! 시야가 탁 트이는 느낌이야. "
    gm "난희야 너도 오늘 이쁜데?"



    if hogam>= 100 :
        show gw_shy
    else :
        show gw_p


    gw "뭐래는거야."
    gw " 스트레칭하고 출발이나 하자. "

    # 산 입구
    gw "저기..[gm].. 할 말이 있어. "

    if hogam>= 100 :
        jump d16_high

    elif hogam >= 70 :
        jump d16_mid

    elif hogam >= 20 :
        jump d16_low



label d16_high:
    gw "승철아 나 너 좋아해"

label d16_mid:
    gw "승철아 다음 단풍 구경은 어디로 갈까?"

label d16_low:
    gw "예전부터 줄곧 생각해왔는데, 너 참 성격 별로더라. 승철아 오늘 즐거웠고, 앞으로 아는척하지 마라. "

