# shiht o --> 콘솔창

label d1_1:
    $gday_count += 1
    $ renpy.notify('    동아리 홍보회   ')
    scene gschool_morning
    play music "audio/yujin/웅성웅성.mp3" 

    gf main "야! [gm] 어디 가입할거야!"
    gf "난 농구부 가입할랜다. 역시 남자는 농구지. "
    scene gdong
    gn "저희 동아리 들어와요! 분위기 좋아요!"
    gn "저희 동아리 들어와요! 저희가 더 재밌어요."
    gn "저희 동아리 들어와요! 학교 지원금 빵빵 합니다!"
    
    gm "산악회 재밌겠는데? 저기로 결정했다."
    play music "audio/yujin/알람음.mp3" noloop
    ga "당신은 산악회에 가입했습니다."
    stop music

    $ renpy.notify('동아리실')
    scene gclassroom1
    play music "audio/yujin/경쾌_기본.mp3" 
    gp1 main "자! 저희 산악자전거 동아리에 가입해주셔서 감사합니다. 저는 회장 [gp1]입니다."

    gm "뭐?!?!?!?!??"
    gm "산악.. 자전거??????????????!!!!!!!!!!!!!!"
    gm "나 자전거 탈 줄 몰라 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 어떡하지..? 나가?"
    gm "모르겠다! 여기서 배워! 어차피 맘에 드는 동아리 없었잖아. "
    
    gp1 "그러면 조 추첨을 진행할게요!"
    gm "으아아아 ~ 몇 조가 나올까..."
    gm "3조라.. !  "
    gm "동아리 들어왔으니 새 친구를 사귀어볼까~"
    show gw_main_black
    gm "흠..저 사람한테 친구하자해볼까..? 자전거 알려달라고 할까? "

    menu:
        "알려달라고 한다. ":
            gm "그래 이러면서 친해지는 거지."

        "다른 사람에게 알려달라고 한다. ":
            gm  "이러면서 친해지는 거지. 물어보자."

    ga "당신은 ???에게 말을 걸기로 결심했다. "

    gm "저기 ..!"
    gm "이름이 뭔가요. 몇 학년이세요? 친해지고 싶어요."

    show gw_main_shy
    gw  "..........."
    gw "[gw]입니다..2학년.."
    gm "오! 굉장히 이름이 이쁘네~~! 동갑이니까 말 편하게 하자!"
    gm "[gw]아 혹시 나 자전거 알려줄 수 있어 ?? 내가 산악자전거는 처음이라..."
    gw happy "'확실히 산악 자전거는 접하기 어렵긴 해. 나도 선배한테 배웠으니까..'"
    gw "그래~ 알려줄게. "
    gm "어! 고마워 !! "
    stop music fadeout 0.5


    jump d2_만나기_전
    