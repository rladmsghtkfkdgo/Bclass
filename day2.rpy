kl "2일차"
        scene kbedroom
        kl "너무 다사다난한 하루를 보내 잠을 설쳐서 늦잠잤다.."

        km "흐아.. 몇시야.."

        kl "(치지직 부스럭부스럭)"

        km "뭔 소리지?"
        hide kbedroom
        kl "<거실>"
        scene khome2
        show zabcho_smilet at right
        kp "난나나"

        km "(왜 쓰레기를 모으고 있지?)"

        km "너 뭐해?"

        kp "앗! 좋은 아침이야 아침밥을 차리고 있었어!"
        hide zabcho_smilet
        show zabcho_smile at right
        km "??? 이게 아침이라고?"
        hide zabcho_smile
        show zabcho_smilet at right
        kp "응! 인간들은 항상 나한테 이런걸 주던데!"

        kp "아침밥이야!"
        hide zabcho_smilet
        show zabcho_smile at right
        km "음.. (가르쳐야할게 많다..)"

        km "이건 밥이 아니야.. "
        hide zabcho_smile
        show zabcho_sadt at right
        kp "아니라고?!!!"

        kp "그럼 인간들은 이걸 왜 준거지...?"
        hide zabcho_sadt
        show zabcho_sad at right
        km "(인간이 미안해...)"

        km "아침은 내가 만들게."
        hide zabcho_sad
        km "(식물이니까 채소는 빼야겠지?)"
        hide khome2
        scene kkitchen
        kl "채소가 안들어간 오므라이스를 만들었다."

        km "어때?"

        menu:
            "음식이 맛있다.":
                $b_taste = True
                $k = +15
            "음식이 맛없다.":
                $b_taste = False
                $k = -15

        if b_taste:
            kp "너무 맛있다. 이런 건 처음이야!"
            show zabcho_smilet at right
            #호감도 +5
        else:
            kp "음... ^^"
            show zabcho_sad at right
            #호감도 -5

        km "아 그러고보니 냉장고에 먹을게 별로 안남았던데 이따가 장보러 가야겠어."
        show zabcho_smilet at right
        kp "나도 갈래!!"

        km "그래 너를 혼자 두기도 불안하니까."
        hide kkitchen
        hide kzabcho_smilet
        kl "<마트>"
        scene kmarket
        km "음.. 어디보자 뭘 먼저 살까~"

        kp "우와!! 저거 뭐야!"

        kp "이것도 신기해!"

        kp "오 저건 뭐지"

        km "[zabcho_name] 같이가..."

        kl "-잠시 후-"

        km "...계란이랑, 우유.. 음! 다 골랐다."

        km "[zabcho_name]! 이제 계산하러 가자."

        kl "[zabcho_name]의 양손에 시식코너 음식이 가득이다."
    
        kp "웅 앙았엉 암냠"

        km "(좀.. 귀엽네..)"
        hide kmarket
        show kmarket_sail
        kl "삑"
        show ksailer at left
        kj "115,000원 입니다."

        km "카드로 할게요."

        kj "카드 받았습니다."

        kj "고객님 저희 마트가 오픈 1주년을 맞이해 이벤트를 진행하고 있습니다." 
        show kRb at right
        kj "10만원 이상 구매 손님은 영수증에 성함과 연락처 남기고 저기에 넣으면 추첨을 통해 여러 상품을 증정해 드리고 있습니다."
        hide kRb
        hide ksailer
        km "어 정말요? 해봐야겠다."

        kl "추첨통에 영수증을 넣고 마트에서 나왔다."
        hide kmarket_sail
        scene kstreet
        show zabcho_smilet at right
        kp "저거 당첨되면 좋은거야?"
        hide zabcho_smilet
        show zabcho_smile at right
        km "좋지. 아까 보니까 무슨 호텔 숙박권도 있고, 온천여행권도 있던데."

        km "뭐 안될 확률이 높지만.."
        hide zabcho_smile
        show zabcho_mung at right
        kp "그렇구나.."

        kl "[zabcho_name]은 무언가 결심한 듯 보인다."
        hide zabcho_mung
        hide kstreet
        kl "-저녁-"
        scene khome2
        km "그럼 잘자~"
        show zabcho_smilet
        kp "응 너두~~"

        kp "좋아 한번 해보는 거야"

        kp "으랴ㅏㅏㅏㅏ"
        hide khome2
        hide zabcho_smilet
        kl "-며칠 후-"
        scene khome2
        play sound "zabcho_Pling-Sound.ogg" 
        kl "띠링~"
        play music "zabcho_bg.wav"
        km "뭐지"
        #핸드폰을 꺼내며
        show kphone
        hide kphone
        show kphone_n
        km "!!!!"
        hide kphone_n
        km "헉! 당첨 됐잖아!"

        km "어디보자 상품이!!" 

        km "Green Hotel 2박3일 숙박권이잖아!"

        km "나 원래 이런거 안걸리는데!!"

        kp "당첨됐어?"
        show zabcho_pain at right
    
        km "어!! 당첨됐어 그것도 호텔 숙박권!"

        km "근데 너 요즘따라 많이 수척해진 것 같다?"
        hide zabcho_pain
        show zabcho_smilet at right
        kp "으응? 아니야.. 그냥 기분탓이야."
        hide zabcho_smilet
        show zabcho_smile at right

        km "그런가...?"
        hide zabcho_smile
        show zabcho_smilet at right
        kp "아무튼 좋겠네~ 잘 갔다와"
        hide zabcho_smilet
        show zabcho_smile at right
        km "으응? 무슨소리야"
        hide zabcho_smile
        show zabcho_smilet at right
        kp "잘갔다오라고 호텔!"
        hide zabcho_smilet
        show zabcho_smile at right

        km "너도 같이 가야지!"
        hide zabcho_smile
        show zabcho_smilet at right
        kp " 어! 정말 나도 가도돼?"
        hide zabcho_smilet
        show zabcho_smile at right
        km "당연하지. 널 두고 내가 어딜가?"

        km "게다가 숙박권 2인용인데 나는 이 세계에 아는 사람이 너뿐이잖아."

        km "가서 재밌게 놀고오자."
        hide zabcho_smile
        show zabcho_smilet at right
        kp "좋아ㅏㅏㅏ"

        kp "호텔은 어떻게 생겼어?"

        km "이렇게!"

        #핸드폰에 띄운 호텔사진들

        km "이거 보니까 방도 넓고 리뷰도 좋은거 같네."

        kp "너무 기대돼!!!"
        #호감도 +10

        km "내일 가야되니까 얼른 짐싸자"

        kp "응! 알겠어"

        hide zabcho_smilet