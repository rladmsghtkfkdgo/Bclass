label d2_만나기_전: 
    $gday_count += 1
    scene gblack
    ga "오늘은 주말입니다. 당신은 [gw]의 자전거 스터디 강습을 나가야합니다. 당신은 늦잠을 잤습니다. "
    
    scene groom
    gm "맙소사! 맙소사! 맙 소사! 맙소사! 맙소사! 맙소사!"
    gm "시간이 왜이래!!!! 맙소사 맙소사!!!"

    gm "일단 [gw]이한테 늦을 것 같다고 연락해야겠다. 하.... "
    
    # 카톡 화면
    ga "뭐라고 연락을 보낼까?"
    menu:
        "큰일이야 [gw]! 나 갑자기 급똥!!!! 30분 정도 늦을 것 같아." :
            #image 답장 --> 급똥이슈는 ㅇㅈ이지. 
            ga "호감도 +5 ."
            $hogam +=5;

        "미안 지금 일어났어. 어제 수행평가 준비하다가 늦게잤더니.. 빨리 준비해서 갈게. 30분 정도 늦을 것 같아.":
            #image 답장 --> ㅎㅎ 그래 알았어~
            ga "호감도 -5"
            $hogam -=5;
    

        "미안 지금 일어났어. 어제 간만에 런닝 좀 했더니 피곤했나봐.. 빨리 준비해서 갈게. 30분 정도 늦을 것 같아.":
            #image 답장 --> 운동은 ㅇㅈ이지~
            ga "호감도 +5"
            $hogam +=5;


label d2_공원: 
    scene gpark
    show main_w_top
    gm "미안 늦어서! 오늘 저녁에 시간 돼? 내가 밥 살게."
    
    ga "메뉴는 ?"
    menu : 
        "제육 볶음":
            gw "늦은 걸 용서해주지."
            ga "호감도 +10"
            $hogam += 10

        "두부 가득 김치 찌개" :
            gw "늦은 걸 용서해주지. "
            ga "호감도 +15"
            $hogam += 15

        "파스타" :
            gw "...그래 알았어..."
            ga "호감도 -10"
            $hogam -= 10

        "햄버거" : 
            gw ".. 햄버거 무난하지.. "
            ga "호감도 +5"
            $hogam +=5

    gw "이제 본격적인 자전거 스터디를 시작해보자. [gm]! "
    gw "나 이제 손 놓을게. 자 타보자! "

    scene gride_bike
    gm "제발 안돼 ! 나 아직 무서워 ! "
    gw "사실 한참 전부터 놨었어. 만재야 성공이야! "
    gm "!!!!!!!!!!!"
    # 자전거를 성공적으로 타서 기쁜 둘 

label d2_저녁:
    scene gdark_park
    show main_w_top
    gm "그.. 자전거 알려줘서 고마워. 너 혹시 영화 좋아하니? 시간 괜찮으면 영화보러 가자. "
    ga "어떤 영화를 보자고 할까?"
    
    menu:
        "하나의 조각10. (소년만화 애니메이션)":
            gw "나 그거 시리즈 하나도 모르는데.."
            ga "호감도 -10"
            $hogam -= 10

        "용감한 페달 (스포츠 애니메이션)":
            gw "그거 재밌어 보이더라! "
            ga "호감도 +20"
            $hogam += 20

        "범죄시티7 - 범죄와의 종말 (액션)":
            gw "서석이 햄은 인정이지"
            ga "호감도 +10"
            $hogam += 10

        "타이타닉 재개봉 (로맨스 영화)":
            gw "나 로맨스 안 좋아해.. 차라리 용감한 페달볼래?"
            ga "호감도 -20"
            $hogam -= 20

label d2_집:
    scene groom
    gm "오늘  많은 일이 있었지.. "
    ga "[str_question]"

    menu:
        "간다":
            $hogam += 10

        "가지 않는다":
            $hogam += 0

jump d3