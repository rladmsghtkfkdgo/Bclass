# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
#호감도 적용
define k = 0

#default k = Character(hogam(1), color="#d76d6d")
$k = Character(hogam(1), color="#d76d6d")
# 게임에서 사용할 캐릭터를 정의합니다.
define ke = Character('주인공', color="#c8ffc8")
define kz = Character('???', color="#008000")
define kq = Character('잡초', color="#008000")
define kg = Character('여주인공', color='#008000')
define kl = Character()
define kj = Character('마트 점원', color="#1B2A0A")
define kj1 = Character('직원', color="#1B2A0A")
define kj3 = Character('판매원1', color="#1B2A0A")
define kj4 = Character('판매원2', color="#1B2A0A")
image zabcho_mung = "zabcho.png"
image zabcho_smile = "zabcho_smile.png"
image zabcho_sad = "zabcho_sad.png"
image zabcho_smilet = "zabcho_smilet.png"
image zabcho_sadt = "zabcho_sadt.png"
image ksailer = "zabcho_sailer.png"
image NG = "zabcho_NG.png"
image kkitchen = "zabcho_kitchen.png"
image kRb = "zabcho_randome_box.png"
image zabcho_pain = "zabcho_pain.png"
image kphone = "zabcho_phone.png"
image kphone_n = "zabcho_phone_n.png"

define kp = Character("[zabcho_name]")
define km = Character("[man_name]")

image khome = "zabcho_living_P.jpg" 
image khome2 = "zabcho_living_NP.png"   
image kmarket = "zabcho_mart_food.jpg"     
image kmarket_sail = "zabcho_mart_sail.jpg"
image kCS = "zabcho_cutscene.png"
image kstreet = "zabcho_street.png"
image kbedroom = "zabcho_bedroom.png"
image kdrive = "zabcho_drive.jpg"
image kswim = "zabcho_swim.jpg"
image kswim_CS = "zabcho_swim_CS.jpg"
image kwinebar = "zabcho_winebar.jpg"
image khotel = "zabcho_hotel.jpg"
image khotel_R = "zabcho_hotel_room.jpg"
image kzibab = "zabcho_front_door.jpg"

# 여기에서부터 게임이 시작합니다.
label jw:

    kl "-거리-"
    play sound "test_zabcho_bg.ogg"
    scene kstreet
    ke "이세계의 거리.. 기대했는데 별거없잖아...?"

    ke "응? 이게뭐지"

    ke "잡초잖아? 웬 잡초가 혼자 덩그러니 있지? ...근데 뭔가 이 잡초는 특별해보여. 이세계의 잡초는 역시 뭔가 다른가? "

    ke "잡초... 뽑아갈까??"

    menu:
        "뽑자!":
            $b_pick = True
        "무시한다.":
            $b_pick = False

    if b_pick:
        "집에가져가서 화분에 심어야지!"         
    else:
        "에이 귀찮다!"
   
    
    hide kstreet
    kl "-며칠 후-"
    
    
 
    scene khome    
    
    ke "벌써 이렇게 많이 자랐네! 무럭무럭 자라라~"

    kl "(유난히 오늘따라 잡초에 윤기가 난다.)"

    ke "오늘은 어제보다 더 윤기가 나네 뭔가 점점 반질거리는 것 같은데..?"
    #음악끄기   
    #다음일차로 넘어가는 1~2초 정도의 BGM
    kl "다음 날 저녁"
    #음악끄기

    hide khome
    scene khome2
    ke "오늘도~ 잡초에~ 물을 주러 가보실게요옹~"
    #음악끄기
    ke "...??? 엥? 어디갔지? 잡초가 사라졌다??? 뭐야 어디갔어ㅓㅓ"
    
    ke "(두리번 두리번)"

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

    kl "거실 구석을 살펴보니 처음보는 여자가 나를 쳐다보고 있다."
    hide khome2
    scene kCS
    
    ke "!!"
    hide kCS
    scene khome2
    show zabcho_mung at right
    ke "?!?!?!?!! 으악!!"
    hide zabcho_mung
    
    ke "(뭐지 누구지 아니 근데 이게 뭐지 일단 말을 걸어봐야겠다.)"

    ke "누..누구냐 넌?"
    show zabcho_mung at right
    kz "아.. 나는"

    ke "누군데 남의 집에 들어와 있는거야? 아니 애초에 어떻게 들어온거야?"
    hide zabcho_mung
    show zabcho_sadt at right
    kz "나는 너가 키워주던 잡초야!"
    hide zabcho_sadt
    show zabcho_mung at right
    ke "???(이상한 여자다!)" 
    
    ke "뭔 개소...아 아니 뭔 말도 안되는 소리야?"
    hide zabcho_mung
    show zabcho_sadt at right
    kz "잠깐만 내 얘기 좀 들어줘. 내가 다 설명할 수 있어!"

    ke "(어떡하지?)"

    menu:
        "얘기를 들어본다":
            $b_hear = True
            $k = +10
        
        "수상한 사람이다 쫓아낸다":
        
            jump kfirst
            #$b_hear = False
            $k = -10

    if b_hear:
        "그래 얘기는 들어보고 판단하자. 집에 들어온 경위도 알아내야 하니까."

    label ksec:
        ke "그래 일단 얘기는 해봐"
        hide zabcho_sadt
        show zabcho_smilet
        kz "고마워. 일단 본론만 말하자면 나는 네가 키워준 잡초가 맞아. 그 증거로 너는 항상 나에게 물을 주러 오면서 말을 흥얼 거렸지."

        kz "그리고 항상 나에게 무럭무럭 자라라며 얘기해 줬어."
        hide zabcho_smilet
        show zabcho_smile
        kz "마지막으로 난 너의 비밀을 알아. 넌 다른 세계에서 왔어."
        hide zabcho_smile
        show zabcho_mung
        kz "이정도면 믿어 줄래?"

        ke "흠... 확실히 다른건 몰라도 내가 다른 세계에서 왔다는 건 누구에게도 말 안했지.."

        ke "그럼 네가 진짜 그 잡초라고?"
        hide zabcho_mung
        show zabcho_smilet
        kz "응!! 이제야 믿어주는 구나!"
 
        ke "그렇다면 너는 갑자기 왜 인간으로 변한거야?"

        kz "그 이유는..!!!"

        ke "이유는?!!!!"

        kz "나도 몰라!"

        ke "으엥?"
    
        kz "나도 오늘 눈 떴더니 갑자기 이런 모습이었어. 혼란스러웠는데 네가 나타나서 안심했어."

        ke "아까 그 표정은 안심이었구나.."

        ke "아무튼 그럼 이제 나가줄래?"
        hide zabcho_smilet
        show zabcho_sadt
        kz "어...?"

        ke "???"

        kz "저.. 혹시 갈때가 없어서 그런데 나 여기서 지내면 안될까?"

        ke "내집에??"

        kz "안돼?...?"
        hide zabcho_sadt
        ke "흠... (하긴 잡초였으면 집이고 뭐고 없을테니까..)"

        ke "좋아. 허락할게 일단은 내가 키우던 잡초니까(?)"
        show zabcho_smilet
        kz "고마워 진짜!!"

        kl "그렇게 나와 잡초의 생활이 시작 됐다."

        ke "그러고 보니 너를 뭐라고 부르면 좋을까?"
        hide zabcho_smilet
        show zabcho_mung
        kz "응?"

        ke "잡초라고 부르긴 너무 삭막하잖아. 지금은 사람모습인데.."

        kz "어.. 그럼 네가 내 이름 지어줘"

        ke "내가?"
        hide zabcho_mung
        show zabcho_smilet
        kz "응! 너가 지어주면 좋을 것 같아. 너가 나를 주워왔으니까."

        ke "흠... 그래 그럼 어디보자 네 이름은.."

        $ zabcho_name = renpy.input("잡초의 이름을 입력해주세요.", length = 32)
        ke "음.. 그럼 네 이름은 [zabcho_name]이야."

        kp "[zabcho_name]!!"

        kp "헤헷.."
        hide zabcho_smilet
        show zabcho_mung
        kp "(빠안-히)"

        ke "왜?"

        kp "근데 네 이름은 뭐야?"

        kp "아직 네 이름을 몰라!"

        ke "내 이름?"

        ke "내이름은.."

        $ man_name = renpy.input("주인공의 이름을 입력해주세요.", length = 32)
        ke "내이름은 [man_name]이야."

        kp "[man_name]이구나 앞으로 잘부탁해!"
        hide zabcho_mung
        show zabcho_smilet
        km "그래 잘 부탁해."

        km "음.. 오늘은 일단 시간이 늦었으니 저쪽방에서 자면 될 거 같아."

        km "(이 집 방이 많아서 다행이야..)"

        kp "알겠어. 내일보자"
        hide zabcho_smilet
        hide khome2
    
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
        play music "zabcho_bg.ogg"
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
        kp "잘갔다오라구 호텔~"
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
        hide zabcho_smilet
        kl "-다음날-"
        scene kzibab
        km "좋아 이제 가면 될 것 같아"
        "준비됐어?"

        kp "준비됐어 가자!!"
        hide kzibab
        scene kdrive
        km "가는데 좀 걸리니까 자고 있어."

        kp "안잘거야! 너 심심하잖아."

        kl "-잠시 후-"

        kp "zzzz"

        km "잘거면서 버티긴.."

        km "(근데 자는 모습도 예쁘네.. 어떻게 사람이 이렇게 생겼지?)"

        km "(아 사람이 아니지 참..)"

        km "흠.. 다왔다."

        km "[zabcho_name], 일어나~ 다왔어"

        kp "흠냐.. 다왔어!!"
        hide kdrive
        scene khotel
        km "우와 호텔은 이렇게 생겼구나 신기해"
    
    return



    label kfirst:
        ke "(수상하다. 가슴에 비수가 날아와 꽂힌다. 얼른 내보내자)"

        ke "아니 됐고 내집에서 나가"

        kz "잠깐만 내 얘기 좀 들어줘.."

        ke "흠.. "
        jump ksec

    return        



