
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
define kj3 = Character('호텔직원', color="#1B2A0A")
define kj4 = Character('남자1', color="#1B2A0A")
define kj5 = Character('장미', color="#de5837")
define kj6 = Character('몬스테라', color="#378147")
define kj7 = Character('장미와 몬스테라', color="#7e6e19")
define kk = Character('고양이', color="#879a26")

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
define kc = Character("[cat_name]")

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
image hongbo = "zabcho_instar.png"

# 여기에서부터 게임이 시작합니다.
label jw:

    kl "-거리-"
    play sound "zabcho_bg.wav" 
    scene kstreet
    ke "이세계의 거리.. 기대했는데 별거없잖아...?"

    ke "응? 이게뭐지"

    ke "잡초잖아? 웬 잡초가 혼자 덩그러니 있지? ...근데 뭔가 이 잡초는 특별해보여. 이세계의 잡초는 역시 뭔가 다른가? "

    ke "잡초... 뽑아갈까??"

    menu:
        "뽑자!":
            "집에가서 화분에 심어야지!"
            $b_plant = True
            
        "무시한다.":
            "에이 귀찮다!"
            $b_plant = False
            
    if b_plant:
        jump k_11
    else:
        jump k_10

    label k_11:
           
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
        scene kCS with fade 
        " "




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
                "호감도: +[k]"

            "수상한 사람이다 쫓아낸다":
            
                jump kfirst
                #$b_hear = False
                $k = -10
                "호감도: -[k]"
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
            ke "음.. 그럼 네 이름은 [zabcho_name](이)야."

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
            ke "내이름은 [man_name](이)야."

            kp "[man_name](이)구나 앞으로 잘부탁해!"
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
            kp "우와 진짜 개꿀이다!"

            km "그런 말은 어디서 배운거야?"

            kp "위튜브에서 요즘 유행하는 말이라고 알려주던데!!"

            km "위튜브를 끊어야되나.."

            kp "아무튼 그렇구나...."

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

            hide zabcho_smilet
            show hongbo
            show zabcho_smilet at right

            km "이거 보니까 방도 넓고 리뷰도 좋은거 같네."
            hide hongbo

            kp "기분 지존이다!!!"
            #호감도 +10

            km "...그것도 위튜브에서 배운거야?"

            kp "응! 위튜브는 정말 위대한거같아!"

            km "(역시 위튜브를 끊어야되나..)"

            km "아무튼 내일 가야되니까 얼른 짐싸자"

            kp "응! 알겠어"

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

            km "저기서 체크이나면 될거 같아"

            kj3 "안녕하세요. Green hotel입니다. 무엇을 도와드릴까요?"

            km "체크인하러 왔습니다."

            kj3 "예약자분 성함이 어떻게 되세요?"

            km "[man_name](으)로 예약했습니다."

            kj3 "고객님 죄송하지만 예약자 명단에 없습니다."

            km "예? 그럴리가요..."
            # 예약한 화면 핸드폰을 보여주며
            km "여기 예약했는데요?"

            kj3 "아.. 고객님 여기 보시면 앞에 친환경 이라고 적혀 있습니다."

            km "네?.. 헉 진짜네!"

            kj3 "종종 헷갈려서 오시는분들이 계시더라고요."

            kj3 "친환경 Green hotel은 여기서 Gu방향으로 5분 정도 걸어가시면 있습니다"

            km "아..넵 감사합니다."

            kp "여기 아니야?"

            km "아닌거 같아.. 여기서 조금만 더 가면 있다니까 가보자."

            kp "으응.."

            kl "-잠시후-"

            km "여기인가봐..."
            #허름한 여관같이 생긴 호텔 배경

            kp "와...여기도 괜찮다...!"
            #호감도 -5

            km "(어쩐지 마트에서 너무 좋은걸 준다 했어...)"

            km "일단 들어가자"
            #허름한 여관내부 프론트
            kj1 "어서오세요. 친환경 Green hotel입니다~"

            km "[man_name](으)로 예약했는데요"

            kj1 "아 예~ 201번방 가시면 됩니다~"

            km "네 감사합니다."

            km "201번이면.. 2층으로 가자"
            #삐걱삐걱 계단 올라가는 소리
            km "여기다"
            #생각보다 깔끔한 방 내부
            km "안은 생각보다 깨끗하네."

            kp "[man_name]! 나 저기 나가도 돼??"

            km "음.. 그럼 나는 짐정리 하고 있을테니까 너무 멀리가지 마!"

            kp "웅!"

            kl "-잠시후-"

            km "정리 다했다. [zabcho_name]은(는) 뭐하지?"

            #여관 앞 작은 뜰(한켠애 놓인 물뿌리개)

            kp "응 아~ 거기 알았어 고마워!"

            kp "어! [man_name]!"

            km "너 여기서 누구랑 뭐해?"

            kp "나 친구들이랑 대화하고 있었어!"

            km "친구들? 설마 거기있는 들꽃 말하는거야?"

            kp "응!"

            km "식물이랑 애기할 수 있어?"

            kp "응 되더라고"

            kp "들꽃이 핫플레이스 알려줬어"

            kp "밤에 저쪽 언덕은 꼭 가야된대!"

            km "그래? 그럼 오늘밤에 가보자."

            kp "좋아!"

            kp "그럼 우리 이제 뭐해?"

            km "간단하게 끼니를 좀 때우러 가자"

            menu:
                "Brunch.EN(브런치 카페)":
                    kp "카페 꼭 한번 가보고 싶었어"
                    #호감도 +5
                    jump k_1
                "술이 들깨 해장국":
                    kp "마침 배고팠는데 잘됐다!"
                    "[zabcho_name]은(는) 뼈해장국을 좋아합니다."
                    #호감도 +10
                    jump k_2
                "쿵떡쿵떡(떡볶이)":
                    kp "떡볶이..? 흠.. 우리 다른거 먹자..."
                    #호감도 -8
                    "[zabcho_name]은(는) 떡볶이를 그다지 좋아하지 않습니다."
                    kl "카페에 가서 간단히 먹기로 했다."
                    jump k_1

            label k_1:
                #카페 내부 사진
                km "나는 오므라이스 먹을래 너는?"

                kp "나도 오므라이스!"

                km "나 잠깐 화장실 좀 다녀올게."

                kp "엉~"

                kl "-잠시후-"

                km "후.. 시원하다!"

                km "응?"

                kj4 "저.. 너무 제 이상형이셔서 그런데 번호좀 주실 수 있을까요?"

                km "(어.. 안되는데)"

                km "얼른 가서 막아야겠다"

                kp "아니요. 저 남자친구 있어요."

                kj4 "아...넵"

                km "(헉!! 저런 박력있는 얼굴도 할 수 있던거였어? 멋있다..)"

                kl "[man_name]의 호감도가 50 증가했습니다(?)"

                kp "어! [man_name]~ 얼른와!!"

                kl "[zabcho_name]은(는) 당신과 있어 행복합니다"
                #호감도 +10

                km "으응..."
                jump k_3

            label k_2:
                kp "역시! 떡볶이 같은거 먹을바엔 든든하고 맛있는 해장국이지!"

                km "(... 집가면 위튜브를 끊어야겠다..)"
                jump k_3

            label k_3:
                kl "배를 채운 후 근처에 유명한 벽화마을을 구경했다."

                kp "너무 예쁜 그림들이었어.."

                km "그러게"

                km "(네가 더 예뻐)"

                km "슬슬 해도 질거 같은데 우리이제 그 언덕 가볼까?"

                kp "그래...."

                kp "어! 잠깐만 저기는 뭐하는 곳이야?"
                #작은 주점을 가리키며
                km "저기는 주점이야. 술을 파는곳이지."

                kp "술? 나그거 알아. 인간들은 그걸 마시면 행복해지는거지!"

                km "응?..흠 어느정도 맞긴한데"

                kp "저기 한번 가보면 안돼?"

                km "저기가 궁금해?"

                kp "궁금해! 술이라는것도 마셔보고 싶어."

                km "그럼 가보자(내가 있으니까 괜찮겠지...)"
                #주점 내부

                km "(무슨 주점이 이렇게 빤짝거리지..)"

                km "뭘 시킬까?"

                menu:
                    "거짓이슬":
                        jump k_4

                    "과일주":
                        jump k_5

                label k_4:
                    km "거짓이슬 하나 주세요."

                    kj1 "네 여기 있습니다."
                    #술따르는 효과음

                    km "한번 마셔봐"

                    kp "(꼴깍)"

                    kp "음~ 괜찮은데! 쓴맛이 매력적이야."

                    kl "[zabcho_name]은(는) 쓴맛을 좋아합니다."
                    #호감도 +5
                    jump k_6

                label k_5:
                    km "과일주 하나 주세요."

                    kj1 "네 여기 있습니다."
                    #술따르는 효과음

                    km "한번 마셔봐"

                    kp "(꼴깍)"

                    kp "음... 너무 단데.."

                    kl "[zabcho_name]은(는) 단맛을 싫어합니다."
                    #호감도 -10

                    km "그래? 그럼.."
                    jump k_4

                label k_6:
                    kl "-잠시후-"

                    km "으아.."

                    kp "너 괜찮아? 너무 많이 마신것 같은대?"

                    km "으응 갠차나ㅏ"

                    kp "안되겠다. 얼른 숙소로 돌아가자."

                    km "나 쥐짜 갠찬다니까!"

                    km "아 맞다 우리이이 언덕 가바야지이이"

                    kp "무슨 언덕이야. 언덕은 나중에 가고 일단 숙소로 돌아가자."

                    km "아니야아아 가야대애애"

                    km "가좌아아아"

                    kp "어엉??"

                    kl "계산을 하고 언덕으로 향했다"
                    #밤의 언덕사진

                    km "언덕 도차악!"

                    km "별이 반짝거려어어"

                    kp "이제 언덕 와봤으니까 숙소로 돌아가자."

                    kp "너 지금 많이 취했어"

                    km "으으으음. 조금만 이따가아아"

                    kp "그럼 조금만 있다 가는거야!"

                    km "그랭"

                    kp "그래도 경치는 좋네. 들꽃이 추천해준 이유가 있었어."

                    kp "별 예쁘다~"

                    kl "[man_name]이 [zabcho_name]을(를) 바라본다"

                    km "흐흐"

                    kp "??? 왜웃어?"

                    km "예쁘다"

                    kp "별이 예쁘지!"

                    km "아니이 너 예쁘다!"

                    kp "으응?"

                    km "zzzzz"

                    kp "뭐라고? [man_name]!!"

                    kl "-다음날-"

                    km "으윽 숙취..."

                    kp "이제 일어났어?"

                    km "으응.. 지금 몇시야?"

                    kp "벌써 점심 다 지났지 2시야"

                    km "뭐라고?!"

                    km "으윽 어제 너무 마셨나.."

                    km "미안 어제 나 데리고 오기 힘들었지?"

                    kp "별로.. 근데 어제 일 기억해?"

                    km "어제?..음 필름이 끊겼나봐.. 기억이 안나네.."

                    km "미안 어제 내가 이상한짓 했어?"

                    kp "흐음.. 몰라!"

                    km "???"

                    km "나 이상한짓 했구나?? 그치!"

                    kp "몰라! 해장이나 하러가!"

                    km "뭔데에에에!!!"

                    kl "[zabcho_name]은(는) 끝내 알려주지 않았다"

                    #술이 들깨 해장국집 사진 

                    kl "-술이 들깨 해장국 앞-"

                    km "여기 들깨 뼈다귀해장국 2개 주세요"

                    kj1 "예~ 여기 있습니다~"

                    km "오늘 여행 마지막날인데 어디 가고 싶어?"

                    kp "너 숙취 괜찮겠어? 힘들면 그냥 집 가도 돼!"

                    km "괜찮아 여행 마지막날인데 그냥 쉴수는 없지"

                    km "그럼 여기 어때?"

                    menu:
                        "식물원":
                            "1"
                            jump k_7
                        "수영장":
                            "!"
                            jump k_8
                        "공원산책":
                            "1"
                            #jump k_9

                    label k_7:
                        kp "식물원~ 나 친구들 보고 싶어!"

                        kl "[zabcho_name]은(는) 동족을 볼 기회에 기뻐합니다."
                        #호감도 +5

                        km "그래 알겠어"

                        kl "-식물원-"

                        kp "여기 내 친구들 많아!"

                        kp "저기 장미랑 몬스테라가 있어!"

                        kp "식물게의 스타지"

                        kp "안녕 얘들아!"

                        kj5 "멍청하게 생긴 인간이야"

                        kj6 "야 왜 그래~ 인간한테"

                        kj5 "뭐 어때 어차피 듣지도 못할텐데!"

                        kp "다들리거든?"

                        kj7 "?!?!?!"

                        kj6 "우리 목소리가 들려?"

                        kj7 "왜?? 왜 들려??"

                        kp "그것은 바로 나는 전직(?) 잡초였기 때문이지!"

                        kj7 "뭐라고?!"

                        kp "후훗!"

                        kj7 "어떻게 인간이 됐어? 우리도 알려줘!"

                        kp "그건 바로!"

                        kj7 "바로!"

                        kp "나도 모른다!"

                        kj7 "으잉?"

                        kp "나도 내가 왜 인간이 됐는지 몰라. 언젠가부터 눈떠보니 인간이 됐거든.."

                        kj6 "흠.. 그렇구나. 뭐 딱 보니까 얼마 안남았네~ 지금을 즐겨봐!"

                        kp "응? 그게 무슨소리야? ...얼마 안남았다니?"

                        kj5 "인간과 식물은 느껴지는 아우라 라고 해야되나? 파장이 달라"

                        kj5 "근데 너는 지금 거의 식물이야. "

                        kj5 "지금 말하고 있는 이 순간에도 조금씩 식물로 바뀌고 있었는데... 설마 몰랐어?"

                        kp "......"

                        km "[zancho_name]! 거기서 뭐해?"

                        kp "아.. [man_name]"

                        kp "나 장미랑 몬스테라한테 인사하고 있었어."

                        km "그래? 그럼 하던 얘기 마저 해"

                        kp "아니야.. 우리 이제 그만 가자"

                        km "으응? 친구들이랑 더 얘기 안해봐도 되겠어?"

                        kp "응 괜찮아"

                        kp "숙소로 돌아가자"

                        km "...그래"
                        jump k_12

                    label k_8:
                        kp "수영장? 좋아 인간이된다면 수영이란거 해 보고 싶었어"

                        kl "[zabcho_name]은(는) 처음가보는 수영장에대한 기대감이 생깁니다"
                        #호감도 +3
                        
                        kl "-실내 수영장-"
                        #실내 수영장 사진

                        kp "우와 수영장 널다!"

                        km "여기가 이 근방에서 가장 유명한 수영장이래"

                        km "넓기도 넓은데 지어진지 얼마안되서 시설도 좋다고"

                        kp "그렇구나"

                        km "아 근데 너 수영복이 없지.."

                        kp "이런이런 나의 작은 어린양 그런 걱정은 하지마~"

                        km "또 그새 이상한거 배웠네.."

                        kp "내가 지금 입고 있는 이옷! 무려 소재를 바꿀 수 있다고"

                        kp "소재를 수영복소재로 바꾸면"

                        kp "따로 살 필요가 없지~"

                        km "편하네"

                        kp "후후 그렇지"

                        km "그래 나는 저기서 수영복 빌리고 올게"

                        kp "아항.. 빌리는 방법이 있었지 참!"

                        kl "-수영장 내부-"

                        km "이거봐 수영은 이렇게 하는거야"

                        kp "우와 잘한다~"

                        km "너도 한번 해봐"

                        kp "음... 이얍"

                        #물뿌리는 철벅 효과음

                        km "푸에엑"

                        km "뭐야! 콜록"

                        kp "ㅎㅎㅎㅎ ㅎㅎㅎ 재밌당"

                        km "이런 너 일로와!!"

                        kp "우헤헤헤헤헿"

                        kl "-잠시후-"

                        km "후.. 잘 놀았다 이제 그만 갈까?"

                        kp "으응.."

                        km "왜 그래? 어디 아파?"

                        kp "으음..약간 현기증이.. 으악"

                        kl "[zabcho_name]이 미끌어졌다"

                        km "조심해!!"

                        kp "(탁!)"

                        kp "괜찮아? 안 다쳤어?"

                        kp "(두근두근) 으응..."

                        km "갑자기 왜 그러지? 아까까지만 해도 별일 없었는데?"

                        kp "별일 아니겠지 그냥잠깐 현기증 난거야 조금 쉬면 괜찮아 질거 같아"

                        km "안되겠다.. 얼른 숙소로 돌아가자"

                        kp "안돼.. 여행 마지막날을 숙소에서 보내고 싶지 않아"

                        km "하지만 너 몸이!"

                        kp "아잇! 괜찮대두! 아 그렇지 아까 말한 식물원? 거기 가보고 싶어"

                        km "식물원? 너 정말 괜찮겠어>"

                        kp "그럼그럼 벌써 다 나은것 같은데?"

                        km "으음.."

                        jump k_7


                label k_12:
                    kl "-숙소-"

                    km "아까 짐은 다 싸놨으니까 이제 나가면 돼"

                    kp "응"

                    km "(아까 식물원에서부터 저기압이네..)"

                    km "무슨일 있어?"

                    kp "..어? 아니야 없어 얼른 가자~"

                    km "으음.."

                    kl "-친환경 Green hotel 프론트 앞-"

                    km "체크아웃하러 왔는데요"

                    kj1 "아 네~ 즐거운시간 보내셨나요?"

                    km "네~"

                    kj1 "즐거운시간 보내셨다니 다행입니다. 체크아웃 되셨습니다. 다음에 또 방문해 주세요."

                    kl "-숙소 문앞-"

                    kz "미야옹"

                    km "응? 무슨소리지?"

                    kl "담장위에 검은색 털과 오드아이 눈을 가진 고양이가 쳐다보고 있다"

                    km "엇 고양이네 여기선 처음보는 고양이인데?"

                    kl "고양이가 담장을 내려와 [man_name]의 다리에 머라를 부빈다"

                    kk "애옹"

                    km "간택 강했다.."

                    kk "목줄이 없는거 보니까 주인 없는 고양이 같은데.. 너 나를 간택한거니?"

                    kk "애애애옹"

                    km "그렇구나! [zabcho_name], 우리 이 고양이 데려가자"

                    kp "좋은 생각이야 이렇게 큐티뽀짝한 고양이가 우리를 선택한거니까 이건 운명이야."

                    km "좋아!"

                    km "그럼 고양이 이름을 정해주자"

                    kp "너가 정해줘!"

                    km "음.. 그럼 네 이름은"

                    $ cat_name = renpy.input("고양이의 이름을 입력해주세요.", length = 32)

                    km " 좋아 이제부터 네 이름은 [cat_name](이)야"

                    km "잘부탁해 [cat_name]!"

                    kp "잘부탁해~"

                    kc "애옹~"

                    kl "그렇게 우리의 짧은 여행은 뜻밖의 동료와 함께 끝났다"

                    kl "-집-"






    return

    label k_10:
            ke "집이나 가야지"
   
    return




    
    label kfirst:
        ke "(수상하다. 가슴에 비수가 날아와 꽂힌다. 얼른 내보내자)"

        ke "아니 됐고 내집에서 나가"

        kz "잠깐만 내 얘기 좀 들어줘.."

        ke "흠.. "
        jump ksec

    return        

   

