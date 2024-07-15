label d2_만나기_전: 
    $gday_count += 1
    $ renpy.notify('  어느 주말 아침  ')
    scene gblack
    ga "오늘은 주말입니다. 당신은 [gw]의 자전거 스터디 강습을 나가야합니다. 당신은 늦잠을 잤습니다. "
    
    scene groom
    gm "맙소사! 맙소사! 맙 소사! 맙소사! 맙소사! 맙소사!"
    gm "시간이 왜이래!!!! 맙소사 맙소사!!!"

    gm "일단 [gw]한테 늦을 것 같다고 연락해야겠다. 하.... "
    
    # 카톡 화면
    ga "뭐라고 연락을 보낼까?"
    menu:
        "큰일이야 [gw]! 나 갑자기 급똥!!!! \n30분 정도 늦을 것 같아." :
            scene gblack
            gw "흠.. 급똥은 어쩔 수 없지."
            gm "(휴.. 빨리 준비해서 나가자!!!)"
            ga "호감도 +0 ."
            $hogam +=0;

        "미안 지금 일어났어. 어제 수행평가 준비하다가 늦게잤더니.. \n빨리 준비해서 갈게. 30분 정도 늦을 것 같아.":
            scene gblack
            gw angry "그래 알았어 ~ (누구는 수행평가 준비 안하나?)"
            gm "(휴.. 빨리 준비해서 나가자!!!)"
            ga "호감도 -5"
            $hogam -=5;
    

        "미안 지금 일어났어. 어제 간만에 런닝 좀 했더니 피곤했나봐.. \n빨리 준비해서 갈게. 30분 정도 늦을 것 같아.":
            scene gblack
            gw "흠.. 운동하느라 늦게 일어났다고? \n피곤할만 하지.."
            gm "(휴.. 빨리 준비해서 나가자!!!)"
            ga "호감도 +5"
            $hogam +=5;

    jump d2_공원


label d2_공원: 
    scene gpark
    show gw_angry    
    gm "미안 늦어서! 오늘 저녁에 시간 돼? 내가 밥 살게."
    
    ga "메뉴는 ?"
    menu : 
        "제육 볶음":
            hide gw_angry
            show gw_main_top
            gw "늦은 걸 용서해주지."
            ga "호감도 +10"
            $hogam += 10
            hide gw_main_top

        "두부 가득 김치 찌개" :
            hide gw_angry
            show gw_main_top
            gw happy "늦은 걸 용서해주지. "
            ga "호감도 +15"
            $hogam += 15
            hide gw_main_top

        "파스타" :
            hide gw_angry
            show gw_angry
            gw angry "...그래 알았어..."
            ga "호감도 -10"
            $hogam -= 10
            hide gw_angry

        "햄버거" : 
            hide gw_angry
            show gw_main_top
            gw ".. 햄버거 무난하지.. "
            ga "호감도 +5"
            $hogam +=5
            hide gw_main_top

    show gw_main_top
    gw "이제 본격적인 자전거 스터디를 시작해보자. [gm]! "
    gm "후... 떨린다."
    gw "나 이제 손 놓을게. 자 타보자! "
    hide gw_main_top

    scene gblack
    gm "제발 안돼 ! 나 아직 무서워 ! "
    gw happy "사실 한참 전부터 놨었어. 이야~~ 성공이야! "
    gm "뭐라고?!!!!!!!!!!!"
    scene gride_bike    # 자전거 타는 그림 수정 

    ga "당신은 자전거를 배웠습니다."

label d2_저녁:
    scene gpark
    show gw_main_top
    gm "그.. 자전거 알려줘서 고마워. 너 혹시 영화 좋아하니? \n시간 괜찮으면 영화보러 가자. 내가 살게! "
    ga "어떤 영화를 보자고 할까?"
    
    menu:
        "하나의 조각10. (소년만화 애니메이션)":
            gw angry "나 그거 시리즈 하나도 모르는데.."
            ga "호감도 -10"
            $hogam -= 10

        "용감한 페달 (스포츠 애니메이션)":
            gw happy "그거 재밌어 보이더라! "
            ga "호감도 +20"
            $hogam += 20

        "범죄시티7 - 범죄와의 종말 (액션)":
            gw "서석이 햄은 인정이지"
            ga "호감도 +10"
            $hogam += 10

        "타이타닉 재개봉 (로맨스 영화)":
            gw angry "나 로맨스 안 좋아해.. 차라리 용감한 페달볼래?"
            ga "호감도 -20"
            $hogam -= 20

label d2_집:
    scene groom
    $ renpy.notify('  집  ')
    gm "오늘  많은 일이 있었지.. "
    ga "[str_question]"

    menu:
        "간다":
            $hogam += 5
            ga "좀 더 건강해진기분이 듭니다.."

        "가지 않는다":
            $hogam += 0

    jump d3