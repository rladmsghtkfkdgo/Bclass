label d10:
    $gday_count += 1
    scene black
    $ renpy.notify(' 여름 방학 ')
    play music "audio/yujin/알람음.mp3" noloop
    ga "몇 주후 방학이 되었습니다."
    
    $ renpy.notify(' 동아리 모임 ')
    scene gclassroom2
    play music "audio/yujin/경쾌_기본.mp3" fadeout 0.5
    gp1 "방학 때 특훈을 한번 가질까합니다. "
    gp1 "장소는 아직 미정이긴하나 아마 강원도로 갈 것 같습니다."
    gp1 "희망자는 다음주 월요일까지 저에게 개인 연락 주세요."
    gp1 "난이도가 좀 있는 곳으로 갈 예정이라 잘 고민해보세요. "
    gn "네 ~ "

    gp2 "어이! [gm]! 너 갈거야? 나는 당연히 갈거다! 가자!"
    gm "글쎄.. 난이도가 있다니까 고민이 되는데.."
    gm "[gw]는 가려나?"
    gp2 "[gw]? 걔가 갑자기 왜나와? 너 설마.... "
    gp2 "[gw]랑 최고의 친구가 된거냐?! "
    gm "부럽냐?"
    gp2 "살짝? 난희 이쁘잖아~ "
    gm "하하! 난희 이쁘긴하지."
    gm "[gw]~~~~ 너 특훈 갈거야? "

    gw happy "당연하지. 난 매 여름마다 특훈만을 기다리고 있었다구!"
    gw "넌 갈거야?"

    menu:
        "별 생각 없었는데, 난희가 간다니까 나도 갈래." :
            ga "호감도 + 20"
            $hogam += 20
            if hogam>=20:
                gw shy "좋아..!" 
            else :
                gw "좋아~"

        "방학에는 공부해야지.":
            ga "호감도 - 20"
            $hogam += -20
            gw angry "그래.. 공부 중요하지.."
            gm "하지만 ~ 특훈 며칠 정도는 참여하면 즐거운 경험일 것 같아. "
            gw angry "그래"

    scene gblack
    $ renpy.notify(' 어느날 저녁 ')
    play music "audio/yujin/경쾌_빠른.mp3" fadeout 0.5
    scene gstreet
    gf "너.. 갑자기 너네 동아리 특훈왜가?"
    gf "방학에는 무조건 피시방에 사는애가.. "
    gm "어. 원래 갈 생각 없었는데 난희가 간다니까~"
    gf "난희가 거기서 왜나오냐? 너.. 설마.. 난희를.."
    gm "아 ~ 조용히해 ~ "
    gf "해피엔딩이길 바란다. "

    scene gblack
    $ renpy.notify(' 동아리 특훈 ')
    play music "audio/yujin/알람음.mp3" noloop
    ga "동아리 특훈날입니다."

    play music "audio/yujin/숲속.mp3" fadeout 0.5
    scene gforest
    gp1 "여러분 다들 준비되었나요?"
    gn "네 ~~~~~~"
    gp1 "가장 중요한건 뭐다?"
    gn "안전~~~~~~~"
    gp1 "좋아요. 다들!! 출발!! " 

    gm "가자! 난희야!"
    gw "응 !"
    gw "(승철이 이제 혼자 잘타네.. 신규 부원도 가르칠 만큼 늘었어..)"
    gw "(뿌듯하네...)"

    play music "audio/yujin/쿵.mp3" noloop
    gw angry ".....어!! 아악 !!!!!"
    gm "난희야!!"
    gp1 "난희!!!!!!"
    gp1 "이게 무슨일이야. 실수 잘 안하는 애가..괜찮아? 계속 탈 수 있겠어? "
    gw angry "네.. 아... 죄송해요.. 아앗.. 못 탈 것 같아요. "
    gm "난희야.......... "
    gm "안되겠다.. 회장님 난희 데리고 제가 먼저 내려갈게요. "
    gw angry "아냐 승철아. 나 천천히 혼자 내려갈게. 너 갔다와. 특훈은 처음이잖아."
    
    menu :
        "특훈이 중요해? 지금 너가 다쳤는데, 어떻게 혼자두고 가.":
            gw shy "..승철아.. 감동이야. 미안.. 고마워.."
            ga "호감도 +30"
            $hogam += 30

            jump d10_1

        "...너가 그렇게 말하면.. 빨리 올라갔다 올게.":
            ga "응.. 경치 구경하며 있을게"
            ga "호감도 +0"
            $hogam += 0

            jump d10_2

label d10_1:
    play music "audio/yujin/숲속.mp3" fadeout 0.5
    gm "난희 얼마나 다친거야.. 많이 아파?"
    gw angry "모르겠어.. 걸을 순 있는데 걸으면 아파."
    gm "흠.. 엎혀. 내가 이 날을 위해 열심히 운동을 한 것 같네."
    gw shy "승철 .. 고마워 진짜."
    ga "호감도 +20"
    $hogam +=20
    

    jump d10_3

label d10_2:
    play music "audio/yujin/숲속.mp3" fadeout 0.5
    gm "헉헉 난희야.. 헉헉 타고 왔어."
    gw "푸화하하. 그래도 생각보다 엄청 빨리 왔네. 너가 제일 처음 내려왔어."
    menu:
        "네가 걱정되어서 빨리 내려왔어.":
            ga "호감도 +10"
            $hogam += 10
            gw happy "고마워 하하~"

        "특훈의 결과인가봐":
            ga "호감도 +10"
            $hogam +=10
            gw happy "내가 좀 잘 가르치긴 했지. "

    gm "자 천천히 같이 내려가보자. 조심하고."
    gw "응."
   

    jump d10_3

label d10_3: 
    play music "audio/yujin/숲속.mp3" fadeout 0.5
    gm "실수 잘안한다면서 왜 그런 실수를 했어?"
    gw "너가 혼자서 이제 잘 타길래.. 너 구경하다가.. "
    gm "내려가면 병원 먼저가자. 당분간은 자전거 타기 금지야."
    gw angry "... 흑흑.. "
    gm "대답 왜 없지?"
    gw angry "네........"

    $ renpy.notify(' 집 근처 ')
    scene gpark
    gm "오늘 고생 많았어. 집가서 푹 쉬고. 꼭 병원가."
    gw shy "응.. 도와줘서 고마워. 잘가 ! "

    jump d11