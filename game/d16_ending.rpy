
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

    # 산타는 이미지 
    

    # ==========
    gm "그.. 있잖아 난희야.. 할 말이 있어. "

    menu:
        "니가 좋다 이난희":
            if hogam>=200:
                gw "나도 좋아"
                jump ending_love

            else : 
                gw "갑자기 뭐야. 징그러"
                jump ending_friend
        
        "나랑 오래 친구하자.":
            if hogam>=200:
                gw "난 친구하기 싫은데? 승철이 여자친구 할게."
                jump ending_love

            else : 
                gw "갑자기 뭐야. 징그러"
                jump ending_friend
        
        

label ending_love:


label ending_friend:

    