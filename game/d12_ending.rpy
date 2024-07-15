label d12:
    $gday_count += 1
    $ renpy.notify('    어느날 저녁   ')
    play music "audio/yujin/전화음.mp3" noloop
    ga "전화가 울립니다."
    stop music
    gm "여보세요?"
    gw "나와! 저녁 자전거타기하자!"
    gm "지금? 알았어~"

    play music "audio/yujin/저녁_공원.mp3" fadeout 0.5
    $ renpy.notify('    공원   ')
    scene gpark_night
    show gbike
    gw "스으으응철~~~~~"
    gm "난희! "
    gw happy "일단 가볍게 세 바퀴 돌아볼까?"
    
    menu:
        "3바퀴? 날도 더운데 1바퀴만 돌자~":
            ga "호감도  -10"
            $hogam += -10
            gw "약한 소리 하지마~! 3바퀴 다 돌거야."

        "자 출발 ~":
            ga "호감도 + 10"
            $hogam += 10 

    $ renpy.notify('    다 돈 후   ')
    gm "크아악 힘들다. "
    gw happy "후 ~ 상쾌하다. "
    gw "자 물 마셔. 안 가지고 왔지?"
    gm "이런 간파당했다!"
    gm "............."
    gm "그... 있..잖아 난희야..."
    gw "어?"
    gm "난희야...."

    menu:
        "니가 좋다 이난희":
            if hogam >= 108:
                gw shy "나도 좋아. 너 내 남자친구해라. "
                jump ending_love

            elif (hogam >= -29) & (hogam < 108) : 
                gw "갑자기 뭐야. 징그러"
                jump ending_friend

            else : 
                gw "????"
                gw angry "우웩 이게 고백 공격 이런건가?"
                gw angry "좋게 봐주려고 했더니.. 안되겠다. 그냥 오늘 마지막으로 아는척하지 말자. "

                jump ending_bad
        
        "나랑 오래 친구하자.":
            if (hogam >= 108):
                gw "난 친구하기 싫은데? "
                gw shy "승철이 여자친구하고 싶어."
                jump ending_love

            elif (hogam >= -29) & (hogam < 108) : 
                gw "갑자기 뭐야? 뭐 잘못했니..?"
                jump ending_friend

            else : 
                gw "????"
                gw angry "사실 오늘 널 부른건 이제 마지막으로 같이 자전거 타자고 부른거야."
                gw happy "너 나랑 안 맞아. 우리 그냥 앞으로 아는척하지 말자."
                jump ending_bad


#엔딩
## 245 ~ 108
label ending_love:
    play music "audio/yujin/엔딩_러브.mp3" fadeout 0.5
    scene glove_end
    ga "당신은 이난희와 연인이 되었습니다. "
    
    return

## 107 ~ -29
label ending_friend:
    play music "audio/yujin/경쾌.mp3" fadeout 0.5
    scene gnormal_end
    ga "당신은 이난희와 우정을 기약했습니다. "


    return
    

## - 30 ~  그 이하 
label ending_bad:
    play music "audio/yujin/엔딩_베드.mp3" fadeout 0.5
    scene gbad_end
    ga "당신은 이난희에게 절교 당했습니다. "

    return
    