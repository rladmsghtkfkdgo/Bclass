# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
#호감도 적용
define k = 0

#default k = Character(hogam(1), color="#d76d6d")
$k = Character(hogam(1), color="#d76d6d")
# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('주인공', color="#c8ffc8")
define z = Character('???', color="#008000")
define q = Character('잡초', color="#008000")
define g = Character('여주인공', color='#008000')
define l = Character()
define j = Character('마트 점원', color="#1B2A0A")
define j1 = Character('직원', color="#1B2A0A")
define j3 = Character('판매원1', color="#1B2A0A")
define j4 = Character('판매원2', color="#1B2A0A")
image zabcho_mung = "zabcho.png"
image zabcho_smile = "zabcho_smile.png"
image zabcho_sad = "zabcho_sad.png"
image zabcho_smilet = "zabcho_smilet.png"
image zabcho_sadt = "zabcho_sadt.png"
image sailer = "sailer.png"
image NG = "zabcho_NG.png"
image kitchen = "kitchen.png"
image Rb = "randome_box.png"
image zabcho_pain = "zabcho_pain.png"
image phone = "phone.png"
image phone_n = "phone_n.png"

define p = Character("[zabcho_name]")
define m = Character("[man_name]")

image home = "living_P.jpg" 
image home2 = "living_NP.png"   
image market = "mart_food.jpg"     
image market_sail = "mart_sail.jpg"
image CS = "cutscene.png"
image street = "street.png"
image bedroom = "bedroom.png"

# 여기에서부터 게임이 시작합니다.
label start:

    l "-거리-"
    play music "shinebgm.ogg"
    scene street
    e "이세계의 거리.. 기대했는데 별거없잖아...?"

    e "응? 이게뭐지"

    e "잡초잖아? 웬 잡초가 혼자 덩그러니 있지? ...근데 뭔가 이 잡초는 특별해보여. 이세계의 잡초는 역시 뭔가 다른가? "

    e "잡초... 뽑아갈까??"

    menu:
        "뽑자!":
            $b_pick = True
        "무시한다.":
            $b_pick = False

    if b_pick:
        "집에가져가서 화분에 심어야지!"         
    else:
        "에이 귀찮다!"
    stop music
    play sound "MBS.ogg"
    hide street
    l "-며칠 후-"
    stop music
    play sound "shinebgm.ogg"
 
    scene home    
    
    e "벌써 이렇게 많이 자랐네! 무럭무럭 자라라~"

    l "(유난히 오늘따라 잡초에 윤기가 난다.)"

    e "오늘은 어제보다 더 윤기가 나네 뭔가 점점 반질거리는 것 같은데..?"
    #음악끄기   
    #다음일차로 넘어가는 1~2초 정도의 BGM
    l "다음 날 저녁"
    #음악끄기
    #play sound "GB.OGG"
    hide home
    scene home2
    e "오늘도~ 잡초에~ 물을 주러 가보실게요옹~"
    #음악끄기
    e "...??? 엥? 어디갔지? 잡초가 사라졌다??? 뭐야 어디갔어ㅓㅓ"
    #
    e "(두리번 두리번)"

    menu:
        "잡초를 찾는다.":
            "구석을 잘 찾아보자"
            $b_find = True
        "잡초 찾는 걸 포기한다.":
            $b_find = False

    if b_find:
        "구석을 잘 찾아보자"
    else:
        "에잉 모르겠다."

    l "거실 구석을 살펴보니 처음보는 여자가 나를 쳐다보고 있다."
    hide home2
    scene CS
    
    e "!!"
    hide CS
    scene home2
    show zabcho_mung at right
    e "?!?!?!?!! 으악!!"
    hide zabcho_mung
    
    e "(뭐지 누구지 아니 근데 이게 뭐지 일단 말을 걸어봐야겠다.)"

    e "누..누구냐 넌?"
    show zabcho_mung at right
    z "아.. 나는"

    e "누군데 남의 집에 들어와 있는거야? 아니 애초에 어떻게 들어온거야?"
    hide zabcho_mung
    show zabcho_sadt at right
    z "나는 너가 키워주던 잡초야!"
    hide zabcho_sadt
    show zabcho_mung at right
    e "???(이상한 여자다!)" 
    
    e "뭔 개소...아 아니 뭔 말도 안되는 소리야?"
    hide zabcho_mung
    show zabcho_sadt at right
    z "잠깐만 내 얘기 좀 들어줘. 내가 다 설명할 수 있어!"

    e "(어떡하지?)"

    menu:
        "얘기를 들어본다":
            $b_hear = True
            $k = +10
        
        "수상한 사람이다 쫓아낸다":
        
            jump first
            #$b_hear = False
            $k = -10

    if b_hear:
        "그래 얘기는 들어보고 판단하자. 집에 들어온 경위도 알아내야 하니까."

    label sec:
        e "그래 일단 얘기는 해봐"
        hide zabcho_sadt
        show zabcho_smilet
        z "고마워. 일단 본론만 말하자면 나는 네가 키워준 잡초가 맞아. 그 증거로 너는 항상 나에게 물을 주러 오면서 말을 흥얼 거렸지."

        z "그리고 항상 나에게 무럭무럭 자라라며 얘기해 줬어."
        hide zabcho_smilet
        show zabcho_smile
        z "마지막으로 난 너의 비밀을 알아. 넌 다른 세계에서 왔어."
        hide zabcho_smile
        show zabcho_mung
        z "이정도면 믿어 줄래?"

        e "흠... 확실히 다른건 몰라도 내가 다른 세계에서 왔다는 건 누구에게도 말 안했지.."

        e "그럼 네가 진짜 그 잡초라고?"
        hide zabcho_mung
        show zabcho_smilet
        z "응!! 이제야 믿어주는 구나!"
 
        e "그렇다면 너는 갑자기 왜 인간으로 변한거야?"

        z "그 이유는..!!!"

        e "이유는?!!!!"

        z "나도 몰라!"

        e "으엥?"
    
        z "나도 오늘 눈 떴더니 갑자기 이런 모습이었어. 혼란스러웠는데 네가 나타나서 안심했어."

        e "아까 그 표정은 안심이었구나.."

        e "아무튼 그럼 이제 나가줄래?"
        hide zabcho_smilet
        show zabcho_sadt
        z "어...?"

        e "???"

        z "저.. 혹시 갈때가 없어서 그런데 나 여기서 지내면 안될까?"

        e "내집에??"

        z "안돼?...?"
        hide zabcho_sadt
        e "흠... (하긴 잡초였으면 집이고 뭐고 없을테니까..)"

        e "좋아. 허락할게 일단은 내가 키우던 잡초니까(?)"
        show zabcho_smilet
        z "고마워 진짜!!"

        l "그렇게 나와 잡초의 생활이 시작 됐다."

        e "그러고 보니 너를 뭐라고 부르면 좋을까?"
        hide zabcho_smilet
        show zabcho_mung
        z "응?"

        e "잡초라고 부르긴 너무 삭막하잖아. 지금은 사람모습인데.."

        z "어.. 그럼 네가 내 이름 지어줘"

        e "내가?"
        hide zabcho_mung
        show zabcho_smilet
        z "응! 너가 지어주면 좋을 것 같아. 너가 나를 주워왔으니까."

        e "흠... 그래 그럼 어디보자 네 이름은.."

        $ zabcho_name = renpy.input("잡초의 이름을 입력해주세요.", length = 32)
        e "음.. 그럼 네 이름은 [zabcho_name]이야."

        p "[zabcho_name]!!"

        p "헤헷.."
        hide zabcho_smilet
        show zabcho_mung
        p "(빠안-히)"

        e "왜?"

        p "근데 네 이름은 뭐야?"

        p "아직 네 이름을 몰라!"

        e "내 이름?"

        e "내이름은.."

        $ man_name = renpy.input("주인공의 이름을 입력해주세요.", length = 32)
        e "내이름은 [man_name]이야."

        p "[man_name]이구나 앞으로 잘부탁해!"
        hide zabcho_mung
        show zabcho_smilet
        m "그래 잘 부탁해."

        m "음.. 오늘은 일단 시간이 늦었으니 저쪽방에서 자면 될 거 같아."

        m "(이 집 방이 많아서 다행이야..)"

        p "알겠어. 내일보자"
        hide zabcho_smilet
        hide home2
    
        l "2일차"
        scene bedroom
        l "너무 다사다난한 하루를 보내 잠을 설쳐서 늦잠잤다.."

        m "흐아.. 몇시야.."

        l "(치지직 부스럭부스럭)"

        m "뭔 소리지?"
        hide bedroom
        l "<거실>"
        scene home2
        show zabcho_smilet at right
        p "난나나"

        m "(왜 쓰레기를 모으고 있지?)"

        m "너 뭐해?"

        p "앗! 좋은 아침이야 아침밥을 차리고 있었어!"
        hide zabcho_smilet
        show zabcho_smile at right
        m "??? 이게 아침이라고?"
        hide zabcho_smile
        show zabcho_smilet at right
        p "응! 인간들은 항상 나한테 이런걸 주던데!"

        p "아침밥이야!"
        hide zabcho_smilet
        show zabcho_smile at right
        m "음.. (가르쳐야할게 많다..)"

        m "이건 밥이 아니야.. "
        hide zabcho_smile
        show zabcho_sadt at right
        p "아니라고?!!!"

        p "그럼 인간들은 이걸 왜 준거지...?"
        hide zabcho_sadt
        show zabcho_sad at right
        m "(인간이 미안해...)"

        m "아침은 내가 만들게."
        hide zabcho_sad
        m "(식물이니까 채소는 빼야겠지?)"
        hide home2
        scene kitchen
        l "채소가 안들어간 오므라이스를 만들었다."

        m "어때?"

        menu:
            "음식이 맛있다.":
                $b_taste = True
                $k = +15
            "음식이 맛없다.":
                $b_taste = False
                $k = -15

        if b_taste:
            p "너무 맛있다. 이런 건 처음이야!"
            show zabcho_smilet at right
            #호감도 +5
        else:
            p "음... ^^"
            show zabcho_sad at right
            #호감도 -5

        m "아 그러고보니 냉장고에 먹을게 별로 안남았던데 이따가 장보러 가야겠어."
        show zabcho_smilet at right
        p "나도 갈래!!"

        m "그래 너를 혼자 두기도 불안하니까."
        hide kitchen
        hide zabcho_smilet
        l "<마트>"
        show market
        m "음.. 어디보자 뭘 먼저 살까~"

        p "우와!! 저거 뭐야!"

        p "이것도 신기해!"

        p "오 저건 뭐지"

        m "[zabcho_name] 같이가..."

        l "-잠시 후-"

        m "...계란이랑, 우유.. 음! 다 골랐다."

        m "[zabcho_name]! 이제 계산하러 가자."

        l "[zabcho_name]의 양손에 시식코너 음식이 가득이다."
    
        p "웅 앙았엉 암냠"

        m "(좀.. 귀엽네..)"
        hide market
        show market_sail
        l "삑"
        show sailer at left
        j "115,000원 입니다."

        m "카드로 할게요."

        j "카드 받았습니다."

        j "고객님 저희 마트가 오픈 1주년을 맞이해 이벤트를 진행하고 있습니다." 
        show Rb at right
        j "10만원 이상 구매 손님은 영수증에 성함과 연락처 남기고 저기에 넣으면 추첨을 통해 여러 상품을 증정해 드리고 있습니다."
        hide Rb
        hide sailer
        m "어 정말요? 해봐야겠다."

        l "추첨통에 영수증을 넣고 마트에서 나왔다."
        hide market_sail
        scene street
        show zabcho_smilet at right
        p "저거 당첨되면 좋은거야?"
        hide zabcho_smilet
        show zabcho_smile at right
        m "좋지. 아까 보니까 무슨 호텔 숙박권도 있고, 온천여행권도 있던데."

        m "뭐 안될 확률이 높지만.."
        hide zabcho_smile
        show zabcho_mung at right
        p "그렇구나.."

        l "[zabcho_name]은 무언가 결심한 듯 보인다."
        hide zabcho_mung
        hide street
        l "-저녁-"
        scene home2
        m "그럼 잘자~"
        show zabcho_smilet
        p "응 너두~~"

        p "좋아 한번 해보는 거야"

        p "으랴ㅏㅏㅏㅏ"
        hide home2
        hide zabcho_smilet
        l "-며칠 후-"
        scene home2
        play sound "Pling-Sound.ogg" 
        l "띠링~"

        m "뭐지"
        #핸드폰을 꺼내며
        show phone
        hide phone
        show phone_n
        m "!!!!"
        hide phone_n
        m "헉! 당첨 됐잖아!"

        m "어디보자 상품이!!" 

        m "Green Hotel 2박3일 숙박권이잖아!"

        m "나 원래 이런거 안걸리는데!!"

        p "당첨됐어?"
        show zabcho_pain at right
    
        m "어!! 당첨됐어 그것도 호텔 숙박권!"

        m "근데 너 요즘따라 많이 수척해진 것 같다?"
        hide zabcho_pain
        show zabcho_smilet at right
        p "으응? 아니야.. 그냥 기분탓이야."
        hide zabcho_smilet
        show zabcho_smile at right

        m "그런가...?"
        hide zabcho_smile
        show zabcho_smilet at right
        p "아무튼 좋겠네~ 잘 갔다와"
        hide zabcho_smilet
        show zabcho_smile at right
        m "으응? 무슨소리야"
        hide zabcho_smile
        show zabcho_smilet at right
        p "잘갔다오라구 호텔~"
        hide zabcho_smilet
        show zabcho_smile at right

        m "너도 같이 가야지!"
        hide zabcho_smile
        show zabcho_smilet at right
        p " 어! 정말 나도 가도돼?"
        hide zabcho_smilet
        show zabcho_smile at right
        m "당연하지. 널 두고 내가 어딜가?"

        m "게다가 숙박권 2인용인데 나는 이 세계에 아는 사람이 너뿐이잖아."

        m "가서 재밌게 놀고오자."
        hide zabcho_smile
        show zabcho_smilet at right
        p "좋아ㅏㅏㅏ"
        hide zabcho_smilet
        l "-다음날-"

        m "좋아 이제 가면 될 것 같아"
        "준비됐어?"

        p "준비됐어 가자!!"

        m "가는데 좀 걸리니까 자고 있어."

        p "안잘거야! 너 심심하잖아."

        l "-잠시 후-"

        p "zzzz"

        m "잘거면서 버티긴.."
        "근데 자는 모습도 예쁘네.. 어떻게 사람이 이렇게 생겼지?"
        "아 사람이 아니지 참.."
        "흠.. 다왔다."
        "[zabcho_name], 일어나~ 다왔어"

        p "흠냐.. 다왔어!!"
        "우와 호텔은 이렇게 생겼구나 신기해"
    

    return


    label first:
        e "(수상하다. 가슴에 비수가 날아와 꽂힌다. 얼른 내보내자)"

        e "아니 됐고 내집에서 나가"

        z "잠깐만 내 얘기 좀 들어줘.."

        e "흠.. "
        jump sec

    return        



