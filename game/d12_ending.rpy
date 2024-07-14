label d12:
    $gday_count += 1
    $ renpy.notify('    어느날 저녁   ')
    ga "전화가 울립니다."
    gm "여보세요?"
    gw "나와! 저녁 자전거타기하자!"
    gm "지금? 알았어~"

    $ renpy.notify('    공원   ')
    scene gpark_night
    show gbike
    gw "스으으응철~~~~~"
    gm "난희! "
    gw "일단 가볍게 세 바퀴 돌아볼까?"
    
    menu:
        "3바퀴? 날도 더운데 1바퀴만 돌자~":
            ga "호감도 += -10"
            $hogam += -10
            gw "약한 소리 하지마~! 3바퀴 다 돌거야."

        "자 출발 ~":
            ga "호감도 += 10"
            $hogam += 10

    $ renpy.notify('    다 돈 후   ')
    gm "크아악 힘들다. "
    gw "후 ~ 상쾌하다. "
    gw "자 물 마셔. 안 가지고 왔지?"
    gm "이런 간파당했다!"
    gm "............."
    gm "그... 있..잖아 난희야..."
    gw "어?"
    gm "난희야...."

    menu:
        "니가 좋다 이난희":
            if hogam>=200:
                gw "나도 좋아. 너 내 남자친구해라. "
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
    scene black
    ga "당신은 이난희와 연인이 되었습니다. "
    scene 러브

label ending_friend:
    scene black
    ga "당신은 이난희와 우정을 기약했습니다. "
    scene 친구
    