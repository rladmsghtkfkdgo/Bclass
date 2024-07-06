
#호감도 적용
define kh = 0

#default k = Character(hogam(1), color="#d76d6d")
$k = Character(hogam(1), color="#d76d6d")
# 게임에서 사용할 캐릭터를 정의합니다.
define kz = Character('???', color="#011401")
define ke = Character('주인공', color="#000000")
define kq = Character('잡초', color="#008000")
define kl = Character()
define kj = Character('마트 점원', color="#1B2A0A")
define kj1 = Character('직원', color="#1B2A0A")
define kj3 = Character('호텔직원', color="#1B2A0A")
define kj4 = Character('남자1', color="#1B2A0A")
define kj5 = Character('장미', color="#de5837")
define kj6 = Character('몬스테라', color="#378147")
define kj7 = Character('장미와 몬스테라', color="#7e6e19")
define kk = Character('고양이', color="#879a26")
define kg = Character('데메르', color="#ae9007")
define kn = Character('간호사', color="#07ae7c")
define kd = Character('의사', color="#064733")

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
image kgod = "zabcho_god.png"
image kgodt = "zabcho_godt.png"
image knurse = "zabcho_nurse.png"
image kjicwon = "zabcho_jicwon.png"
image khunting = "zabcho_hunting.png"
image khuntingt = "zabcho_hunting.png"
image kFJ = "zabcho_FJ.png"
image kcat = "zabcho_cat.png"
image kreservation = "zabcho_reservation.png"
image zabcho_cute = "zabcho_cute.png"
image alchole1 = "zabcho_false.png"
image alchole2 = "zabcho_alchole.png"
image kpopcorn = "zabcho_popcorn.png"
image tumyeong = "zabcho_tumyeong.png"
image zabcho_sick = "zabcho_sick.png"
image zabcho_sickt = "zabcho_sickt.png"
image kcartoon1 = "zabcho_cartoon1.png"
image kcartoon2 = "zabcho_cartoon2.png"
image zabcho_happy = "zabcho_happy.png"
image zabcho_ft = "zabcho_ft.png"
image zabcho_f = "zabcho_f.png"
image weed = "zabcho_weed.png"
image zabcho_shy = "zabcho_shy.png"
image zabcho_shy_smile = "zabcho_shy_smile.png"
image zabcho_soulless = "zabcho_soulless.png"
image zabcho_soullesst = "zabcho_soullesst.png"
image zabcho_weeds = "zabcho_weeds.png"

define kp = Character("[zabcho_name]", color="#113219")
define km = Character("[man_name]", color="#151d3d")
define kc = Character("[cat_name]", color="#4e3a07")

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
image kgameover = "zabcho_gameover.png"
image kbrunch = "zabcho_brunch.jpg"
image kplanthouse = "zabcho_planthouse.jpg"
image krestaurant = "zabcho_restaurant.jpg"
image ksteak = "zabcho_steak.jpg"
image kblindgod = "zabcho_blindgod.png"
image kgodCS = "zabcho_god_CS.png"
image kzabcho = "zabcho_zabcho.png"
image kgoodby = "zabcho_goodby.png"
image kwinebar_out = "zabcho_winebar_out.png"
image ktheater = "zabcho_theater.png"
image kstar = "zabcho_star.png"
image kroom = "zabcho_room.png"
image kreality = "zabcho_reality.jpg"
image kporaloid = "zabcho_poraloid.png"
image kmiss = "zabcho_miss.png"
image khand = "zabcho_hand.jpg"
image khaejang = "zabcho_haejang.png"
image khaejangin = "zabcho_haejang_in.png"
image kecho_hotel = "zabcho_echo_hotel.png"
image kecho_hotel_in = "zabcho_echo_hotel_in.png"
image kdark = "zabcho_dark.png"
image kdamjang = "zabcho_cat_damjang.png"
image kbrunch = "zabcho_brunch.jpg"
image kbright = "zabcho_bright.png"
image khospital = "zabcho_hospital.png"
image knstreet = "zabcho_new_street.png"
image ndamjang = "zabcho_ndamjang.png"
image ktheater_loading = "theater_loading.png"
image zabcho_origin = "zabcho_origin.png"
image zabcho_happy_CS = "zabcho_happy_CS.png"
image zabcho_sick_CS = "zabcho_sick_CS.png"

# 여기에서부터 게임이 시작합니다.
label jw:

    kl "-거리-"
    play sound "zabcho_bg.wav" 
    scene kstreet
    ke "이세계의 거리.. 기대했는데 별거없잖아...?"

    ke "응? 이게뭐지"
    show zabcho_weeds

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
        hide zabcho_weeds
        jump k_11
    else:
        hide zabcho_weeds
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
        ke "잡초에 물 주러 가야지"
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
            jump k_10


        kl "거실 구석을 살펴보니 처음보는 여자가 나를 쳐다보고 있다."
        hide khome2
        scene kCS with fade
        pause 2.0
        hide image_name with dissolve

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
                $kh +=10
                "호감도: +[kh]"

            "수상한 사람이다 쫓아낸다":
            
                jump kfirst
                #$b_hear = False
                $kh -=10
                "호감도: -[kh]"
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

            kl "다음날"
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
                    $kh +=15
                "음식이 맛없다.":
                    $b_taste = False
                    $kh -=15

            if b_taste:
                kp "너무 맛있다. 이런 건 처음이야!"
                show zabcho_smilet at right
                
            else:
                kp "음... ^^"
                show zabcho_sad at right
                

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
            hide zabcho_smilet

            km "이렇게!"

            show hongbo
            

            km "이거 보니까 방도 넓고 리뷰도 좋은거 같네."
            hide hongbo
            show zabcho_smilet at right

            kp "기분 지존이다!!!"
            $kh +=10
            hide zabcho_smilet
            show zabcho_smile at right

            km "...그것도 위튜브에서 배운거야?"
            hide zabcho_smile
            show zabcho_happy at right

            kp "응! 위튜브는 정말 위대한거같아!"
            hide zabcho_happy

            km "(역시 위튜브를 끊어야되나..)"

            km "아무튼 내일 가야되니까 얼른 짐싸자"
            show zabcho_smilet

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
            hide kdrive
            scene kdark

            kl "-잠시 후-"
            hide kdark
            scene kdrive

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
            show kFJ
            kj3 "안녕하세요. Green hotel입니다. 무엇을 도와드릴까요?"
            hide kFJ
            km "체크인하러 왔습니다."
            show kFJ
            kj3 "예약자분 성함이 어떻게 되세요?"
            hide kFJ
            km "[man_name](으)로 예약했습니다."
            show kFJ
            kj3 "고객님 죄송하지만 예약자 명단에 없습니다."
            hide kFJ
            km "예? 그럴리가요..."
            show kreservation

            km "여기 예약했는데요?"
            hide kreservation
            show kFJ
            kj3 "아.. 고객님 여기 보시면 앞에 친환경 이라고 적혀 있습니다."
            hide kFJ
            km "네?.. 헉 진짜네!"
            show kFJ
            kj3 "종종 헷갈려서 오시는분들이 계시더라고요."

            kj3 "친환경 Green hotel은 여기서 Gu방향으로 5분 정도 걸어가시면 있습니다"
            hide kFJ
            km "아..넵 감사합니다."
            show zabcho_sadt at right

            kp "여기 아니야?"
            hide zabcho_sadt
            show zabcho_sad at right

            km "아닌거 같아.. 여기서 조금만 더 가면 있다니까 가보자."
            hide zabcho_sad
            show zabcho_sadt at right

            kp "으응.."
            hide zabcho_sadt
            hide khotel 
            scene kdark
            kl "-잠시후-"
            hide kdark
            km "여기인가봐..."
            scene kecho_hotel

            kp "와...여기도 괜찮다...!"
            $kh -=5

            km "(어쩐지 마트에서 너무 좋은걸 준다 했어...)"

            km "일단 들어가자"
            hide kecho_hotel
            scene kecho_hotel_in
            show kjicwon
            kj1 "어서오세요. 친환경 Green hotel입니다~"
            hide kjicwon
            km "[man_name](으)로 예약했는데요"
            show kjicwon
            kj1 "아 예~ 201번방 가시면 됩니다~"
            hide kjicwon
            km "네 감사합니다."

            km "201번이면.. 2층으로 가자"
            scene kdark
            kl " "
            #삐걱삐걱 계단 올라가는 소리
            
            km "여기다"
            hide kdark
            scene kroom
            km "안은 생각보다 깨끗하네."
            show zabcho_smilet at right

            kp "[man_name]! 나 저기 나가도 돼??"
            hide zabcho_smilet
            show zabcho_smile at right

            km "음.. 그럼 나는 짐정리 하고 있을테니까 너무 멀리가지 마!"
            hide zabcho_smile
            show zabcho_happy at right

            kp "웅!"
            hide zabcho_happy
            hide kroom
            scene kdark

            kl "-잠시후-"
            hide kdark
            scene kroom

            km "정리 다했다. [zabcho_name]은(는) 뭐하지?"
            hide kroom
            scene kecho_hotel
            show zabcho_happy at right

            kp "응 아~ 거기 알았어 고마워!"
            hide zabcho_happy
            show zabcho_smilet at right

            kp "어! [man_name]!"
            hide zabcho_smilet
            show zabcho_smile at right

            km "너 여기서 누구랑 뭐해?"
            hide zabcho_smile
            show zabcho_smilet at right

            kp "나 친구들이랑 대화하고 있었어!"
            hide zabcho_smilet
            show zabcho_smile at right

            km "친구들? 설마 거기있는 들꽃 말하는거야?"
            hide zabcho_smile
            show zabcho_smilet at right

            kp "응!"
            hide zabcho_smilet
            show zabcho_smile at right

            km "식물이랑 애기할 수 있어?"
            hide zabcho_smile
            show zabcho_smilet at right

            kp "응 되더라고"

            kp "들꽃이 핫플레이스 알려줬어"
            hide zabcho_smilet
            show zabcho_happy at right

            kp "밤에 저쪽 언덕은 꼭 가야된대!"
            hide zabcho_happy
            show zabcho_smile at right

            km "그래? 그럼 오늘밤에 가보자."
            hide zabcho_smile
            show zabcho_smilet at right

            kp "좋아!"

            kp "그럼 우리 이제 뭐해?"
            hide zabcho_smilet
            show zabcho_smile at right

            km "간단하게 끼니를 좀 때우러 가자"
            hide zabcho_smile

            menu:
                "Brunch.EN(브런치 카페)":
                    show zabcho_happy at right
                    kp "카페 꼭 한번 가보고 싶었어"
                    $kh +=5
                    jump k_1
                "술이 들깨 해장국":
                    show zabcho_smilet at right
                    kp "마침 배고팠는데 잘됐다!"
                    "[zabcho_name]은(는) 뼈해장국을 좋아합니다."
                    $kh +=10
                    jump k_2
                "쿵떡쿵떡(떡볶이)":
                    show zabcho_sadt at right
                    kp "떡볶이..? 흠.. 우리 다른거 먹자..."
                    $kh -=8
                    "[zabcho_name]은(는) 떡볶이를 그다지 좋아하지 않습니다."
                    
                    kl "떡볶이를 대충 먹었다."
                    hide kecho_hotel
                    scene kdark
                    jump k_3

            label k_1:
                hide zabcho_happy
                hide kecho_hotel
                scene kbrunch
                km "나는 오므라이스 먹을래 너는?"
                hide zabcho_happy
                show zabcho_smilet at right

                kp "나도 오므라이스!"
                hide zabcho_smilet
                show zabcho_smile at right

                km "나 잠깐 화장실 좀 다녀올게."
                hide zabcho_smile
                show zabcho_smilet at right

                kp "엉~"
                hide zabcho_smilet
                hide kbrunch
                scene kdark

                kl "-잠시후-"
                hide kdark
                show kbrunch

                km "후.. 시원하다!"

                km "응?"
                show zabcho_soulless at right
                show zabcho_huntingt at left

                kj4 "저.. 너무 제 이상형이셔서 그런데 번호좀 주실 수 있을까요?"

                km "(어.. 안되는데)"
                hide zabcho_soulless
                hide zabcho_huntingt
                show zabcho_soullesst at right
                show zabcho_hunting at left

                kp "아니요. 저 남자친구 있어요."
                hide zabcho_soullesst
                hide zabcho_hunting
                show zabcho_soulless at right
                show zabcho_huntingt

                kj4 "아...넵"
                hide zabcho_huntingt

                km "(헉!! 저런 박력있는 얼굴도 할 수 있는거였어? 멋있다..)"

                kl "[man_name]의 호감도가 50 증가했습니다(?)"
                hide zabcho_soulless
                show zabcho_smilet at right

                kp "어! [man_name]~ 얼른와!!"

                kl "[zabcho_name]은(는) 당신과 있어 행복합니다"
                $kh +=10

                km "으응!!"
                hide zabcho_smilet
                hide kbrunch
                scene kdark
                jump k_3

            label k_2:
                hide kecho_hotel
                scene zabcho_haejang_in
                
                kp "역시! 떡볶이 같은거 먹을바엔 든든하고 맛있는 해장국이지!"
                hide zabcho_smilet

                km "(... 집가면 위튜브를 끊어야겠다..)"
                hide zabcho_haejang_in
                scene kdark
                jump k_3

            label k_3:
                kl "배를 채운 후 근처에 유명한 벽화마을을 구경했다."
                hide kdark
                scene knstreet
                show zabcho_smilet at right

                kp "너무 예쁜 그림들이었어.."
                hide zabcho_smilet
                show zabcho_smile at right

                km "그러게"

                km "(네가 더 예뻐)"

                km "슬슬 해도 질거 같은데 우리이제 그 언덕 가볼까?"
                hide zabcho_smile
                show zabcho_smilet at right

                kp "그래...."

                kp "어! 잠깐만 저기는 뭐하는 곳이야?"
                hide zabcho_smilet
                hide knstreet
                scene kwinebar_out
                pause 2.0
                hide image_name with dissolve
                scene knstreet

                km "저기는 주점이야. 술을 파는곳이지."
                show zabcho_smilet at right

                kp "술? 나그거 알아. 인간들은 그걸 마시면 행복해지는거지!"
                hide zabcho_smilet
                show zabcho_smile at right

                km "응?..흠 어느정도 맞긴한데"
                hide zabcho_smile
                show zabcho_smilet at right

                kp "저기 한번 가보면 안돼?"
                hide zabcho_smilet
                show zabcho_smile at right

                km "저기가 궁금해?"
                hide zabcho_smile
                show zabcho_smilet at right

                kp "궁금해! 술이라는것도 마셔보고 싶어."
                hide zabcho_smilet
                show zabcho_smile at right

                km "그럼 가보자(내가 있으니까 괜찮겠지...)"
                hide zabcho_smile
                hide knstreet
                scene kwinebar
                km "(무슨 주점이 이렇게 빤짝거리지..)"

                km "뭘 시킬까?"

                menu:
                    "거짓이슬":
                        jump k_4

                    "과일주":
                        jump k_5

                label k_4:
                    km "거짓이슬 하나 주세요."
                    show alchole1 at left
                    kj1 "네 여기 있습니다."
                    hide alchole1
                    #술따르는 효과음

                    km "한번 마셔봐"

                    kp "(꼴깍)"
                    show zabcho_smilet at right

                    kp "음~ 괜찮은데! 쓴맛이 매력적이야."

                    kl "[zabcho_name]은(는) 쓴맛을 좋아합니다."
                    $kh +=5
                    hide zabcho_smilet
                    hide kwinebar
                    scene kdark
                    jump k_6

                label k_5:
                    km "과일주 하나 주세요."
                    show alchole2 at left
                    kj1 "네 여기 있습니다."
                    hide alchole2
                    #술따르는 효과음

                    km "한번 마셔봐"

                    kp "(꼴깍)"
                    show zabcho_sadt at right

                    kp "음... 너무 단데.."

                    kl "[zabcho_name]은(는) 단맛을 싫어합니다."
                    $kh -=10

                    km "그래? 그럼.."
                    hide zabcho_sadt
                    jump k_4

                label k_6:
                    kl "-잠시후-"
                    hide kdark
                    scene kwinebar

                    km "으아.."
                    show zabcho_sadt at right

                    kp "너 괜찮아? 너무 많이 마신것 같은대?"
                    hide zabcho_sadt
                    show zabcho_sad at right    

                    km "으응 갠차나ㅏ"
                    hide zabcho_sad
                    show zabcho_sadt at right

                    kp "안되겠다. 얼른 숙소로 돌아가자."
                    hide zabcho_sadt
                    hide kwinebar
                    scene kwinebar_out

                    km "나 쥐짜 갠찬다니까!"

                    km "아 맞다 우리이이 언덕 가바야지이이"
                    show zabcho_sadt at right

                    kp "무슨 언덕이야. 언덕은 나중에 가고 일단 숙소로 돌아가자."
                    hide zabcho_sadt
                    show zabcho_sad at right

                    km "아니야아아 가야대애애"

                    km "가좌아아아"
                    hide zabcho_sad

                    kp "어엉??"
                    hide kwinebar_out
                    scene kdark

                    kl "잠시후"
                    hide kdark
                    scene kstar

                    km "언덕 도차악!"

                    km "별이 반짝거려어어"
                    show zabcho_sadt at right

                    kp "이제 언덕 와봤으니까 숙소로 돌아가자."

                    kp "너 지금 많이 취했어"
                    hide zabcho_sadt
                    show zabcho_sad at right

                    km "으으으음. 조금만 이따가아아"
                    hide zabcho_sad
                    show zabcho_sadt at right

                    kp "그럼 조금만 있다 가는거야!"
                    hide zabcho_sadt
                    show zabcho_sad at right

                    km "그랭"
                    hide zabcho_sad
                    show zabcho_smilet at right

                    kp "그래도 경치는 좋네. 들꽃이 추천해준 이유가 있었어."
                    hide zabcho_smilet
                    show zabcho_happy at right

                    kp "별 예쁘다~"
                    hide zabcho_happy
                    show zabcho_smile at right

                    km "흐흐"
                    hide zabcho_smile
                    show zabcho_smilet at right

                    kp "??? 왜웃어?"
                    hide zabcho_smilet
                    show zabcho_smile at right

                    km "예쁘다"
                    hide zabcho_smile
                    show zabcho_smilet at right

                    kp "응 별이 예쁘네~"
                    hide zabcho_smilet
                    show zabcho_smile at right

                    km "아니이 너 예쁘다!"
                    hide zabcho_smile
                    show zabcho_shy at right

                    kp "으응?"
                    hide zabcho_shy

                    km "zzzzz"
                    show zabcho_shy at right

                    kp "뭐라고? [man_name]!!"
                    hide zabcho_shy
                    hide kstar
                    scene kdark

                    kl "-다음날-"
                    hide kdark
                    scene kroom
                    km "으윽 숙취..."
                    show zabcho_smilet at right

                    kp "이제 일어났어?"
                    hide zabcho_smilet
                    show zabcho_smile at right

                    km "으응.. 지금 몇시야?"
                    hide zabcho_smile
                    show zabcho_smilet at right

                    kp "벌써 점심 다 지났지 2시야"
                    hide zabcho_smilet
                    show zabcho_smile at right

                    km "뭐라고?!"

                    km "으윽 어제 너무 마셨나.."

                    km "미안 어제 나 데리고 오기 힘들었지?"
                    hide zabcho_smile
                    show zabcho_smilet at right

                    kp "별로.. 근데 어제 일 기억해?"
                    hide zabcho_smilet
                    show zabcho_smile at right

                    km "어제?..음 필름이 끊겼나봐.. 기억이 안나네.."

                    km "미안 어제 내가 이상한짓 했어?"
                    hide zabcho_smile
                    show zabcho_smilet at right

                    kp "흐음.. 몰라!"
                    hide zabcho_smilet
                    show zabcho_smile at right

                    km "???"

                    km "나 이상한짓 했구나?? 그치!"
                    hide zabcho_smile
                    show zabcho_smilet at right

                    kp "몰라! 해장이나 하러가!"

                    km "뭔데에에에!!!"

                    kl "[zabcho_name]은(는) 끝내 알려주지 않았다"
                    hide zabcho_smilet
                    hide kroom

                    scene khaejangin

                    kl "-술이 들깨 해장국-"

                    km "여기 들깨 뼈다귀해장국 2개 주세요"

                    kj1 "예~ 여기 있습니다~"

                    km "오늘 여행 마지막날인데 어디 가고 싶어?"
                    show zabcho_sadt at right

                    kp "너 숙취 괜찮겠어? 힘들면 그냥 쉬어도 돼!"
                    hide zabcho_sadt
                    show zabcho_sad at right

                    km "괜찮아 여행 마지막날인데 그냥 쉴수는 없지"
                    hide zabcho_sad

                    km "여기 어때?"

                    menu:
                        "식물원":                            
                            jump k_7
                        "수영장":
                            jump k_8
                        "공원산책":
                            jump k_9

                    label k_7:
                        show zabcho_happy at right
                        kp "식물원~ 나 친구들 보고 싶어!"

                        kl "[zabcho_name]은(는) 동족을 볼 기회에 기뻐합니다."
                        $kh +=5
                        hide zabcho_happy

                        km "그래 알겠어"
                        hide khaejangin
                        scene kdark
                        
                        kl "-식물원-"
                        hide kdark
                        scene kplanthouse
                        show zabcho_smilet at right

                        kp "여기 내 친구들 많아!"

                        kp "저기 장미랑 몬스테라가 있어!"

                        kp "안녕 얘들아!"
                        hide zabcho_smilet

                        kj5 "멍청하게 생긴 인간이야"

                        kj6 "야 왜 그래~ 인간한테"

                        kj5 "뭐 어때 어차피 듣지도 못할텐데!"
                        show zabcho_soullesst at right

                        kp "다들리거든?"
                        hide zabcho_soullesst

                        kj7 "?!?!?!"

                        kj6 "우리 목소리가 들려?"

                        kj7 "왜?? 왜 들려??"
                        show zabcho_smilet at right

                        kp "그것은 바로 나는 전직(?) 잡초였기 때문이지!"
                        hide zabcho_smilet
                        show zabcho_smile at right

                        kj7 "뭐라고?!"
                        hide zabcho_smile
                        show zabcho_smilet at right

                        kp "후훗!"
                        hide zabcho_smilet
                        show zabcho_smile at right

                        kj7 "어떻게 인간이 됐어? 우리도 알려줘!"
                        hide zabcho_smile
                        show zabcho_smilet at right

                        kp "그건 바로!"

                        kj7 "바로!"

                        kp "나도 모른다!"
                        hide zabcho_smilet
                        show zabcho_smile at right

                        kj7 "으잉?"
                        hide zabcho_smile
                        show zabcho_smilet at right

                        kp "나도 내가 왜 인간이 됐는지 몰라. 언젠가부터 눈떠보니 인간이 됐거든.."
                        hide zabcho_smilet
                        show zabcho_smile at right

                        kj6 "흠.. 그렇구나. 뭐 딱 보니까 얼마 안남았네~ 지금을 즐겨봐!"
                        hide zabcho_smile
                        show zabcho_sadt at right

                        kp "응? 그게 무슨소리야? ...얼마 안남았다니?"
                        hide zabcho_sadt

                        kj5 "인간이랑 식물이랑 느껴지는 파장이라고 해야할까? 그게 달라"

                        kj5 "아까는 인간의 파장이 느껴졌어"

                        kj5 "근데 지금의 너에게는 식물의 파장이 크게 느껴져 "

                        kj5 "점점 식물의 파장이 커지고 있어."
                        show zabcho_soulless at right

                        kp "......"
                        hide zabcho_soulless

                        km "[zabcho_name]! 거기서 뭐해?"
                        hide zabcho_soulless
                        show zabcho_soullesst at right

                        kp "아.. [man_name]"
                        hide zabcho_soullesst
                        show zabcho_smilet at right

                        kp "나 장미랑 몬스테라한테 인사하고 있었어."
                        hide zabcho_smilet
                        show zabcho_smile at right

                        km "그래? 그럼 하던 얘기 마저 해"
                        hide zabcho_smile
                        show zabcho_smilet at right

                        kp "아니야.. 우리 이제 그만 가자"
                        hide zabcho_smilet
                        show zabcho_smile at right

                        km "으응? 친구들이랑 더 얘기 안해봐도 되겠어?"
                        hide zabcho_smile
                        show zabcho_smilet at right

                        kp "응 괜찮아"

                        kp "숙소로 돌아가자"
                        hide zabcho_smilet

                        km "...그래"
                        hide kplanthouse
                        scene kdark
                        jump k_12

                    label k_8:
                        show zabcho_smilet at right
                        kp "수영장? 좋아 인간이된다면 수영이란거 해 보고 싶었어"

                        kl "[zabcho_name]은(는) 처음가보는 수영장에대한 기대감이 생깁니다"
                        $kh +=3
                        hide zabcho_smilet
                        hide khaejang
                        scene kdark
                        
                        kl "-실내 수영장-"
                        hide kdark
                        scene kswim
                        show zabcho_smilet at right

                        kp "우와 수영장 넓다!"
                        hide zabcho_smilet
                        hide kswim
                        scene kswim_CS
                        pause 2.0
                        hide image_name with dissolve
                        scene kswim

                        km "이거봐 수영은 이렇게 하는거야"
                        show zabcho_smilet at right

                        kp "잘한다~"
                        hide zabcho_smilet
                        show zabcho_smile at right

                        km "너도 한번 해봐"
                        hide zabcho_smile
                        show zabcho_smilet at right

                        kp "음..."

                        #물뿌리는 철벅 효과음
                        hide zabcho_smilet
                        show zabcho_happy at right

                        km "푸에엑"

                        km "뭐야! 콜록"

                        kp "ㅎㅎㅎㅎ ㅎㅎㅎ 재밌당"
                        hide zabcho_happy

                        km "이런 너 일로와!!"
                        show zabcho_happy at right

                        kp "하하할"
                        hide zabcho_happy
                        hide zabcho_swim
                        scene kdark

                        kl "-잠시후-"
                        scene zabcho_swim

                        km "후.. 잘 놀았다 이제 그만 갈까?"
                        show zabcho_sickt at right

                        kp "으응.."
                        hide zabcho_sickt
                        show zabcho_sick at right

                        km "왜 그래? 어디 아파?"
                        hide zabcho_sick
                        show zabcho_sickt at right

                        kp "으음..약간 현기증이.. 으악"
                        hide zabcho_sickt

                        kl "[zabcho_name]이 미끌어졌다"

                        km "조심해!!"

                        kl "[man_name]이(가) [zabcho_name]을(를) 붙잡았다!"

                        km "괜찮아? 안 다쳤어?"
                        show zabcho_shy at right

                        kp "(두근두근) 으응..."

                        km "갑자기 왜 그러지? 아까까지만 해도 별일 없었는데?"
                        hide zabcho_shy
                        show zabcho_shy_smile at right

                        kp "별일 아니겠지 그냥잠깐 현기증 난거야 조금 쉬면 괜찮아 질거 같아"

                        km "안되겠다.. 얼른 숙소로 돌아가자"
                        hide zabcho_shy_smile
                        show zabcho_sadt at right

                        kp "안돼.. 여행 마지막날을 숙소에서 보내고 싶지 않아"
                        hide zabcho_sadt
                        show zabcho_sad at right

                        km "하지만 너 몸이!"
                        hide zabcho_sad
                        show zabcho_smilet at right

                        kp "아잇! 괜찮대두! 아 그렇지 아까 말한 식물원? 거기 가보고 싶어"
                        hide zabcho_smilet
                        show zabcho_smile at right

                        km "식물원? 너 정말 괜찮겠어?"
                        hide zabcho_smile
                        show zabcho_smilet at right

                        kp "그럼그럼 벌써 다 나은것 같은데?"
                        hide zabcho_smilet

                        km "으음.."
                        hide kswim
                        scene kdark
                        jump k_7

                    label k_9:
                        show zabcho_sadt at right
                        
                        kp "공원산책...?"

                        kp "그거는.. 집근처에서도 할 수 있는건데.."

                        kl "[zabcho_name]은(는) 특별한게 하고 싶다."
                        $kh -=8
                        hide zabcho_sadt

                        km "그래? 그럼.. 식물원 가볼까?"
                        show zabcho_smilet at right

                        kp "응! 너무 좋은데!"
                        hide zabcho_smilet
                        hide khaejangin
                        scene kdark
                        jump k_7

                        
                label k_12:
                    kl "-숙소-"
                    hide kdark
                    scene kroom

                    km "아까 짐은 다 싸놨으니까 이제 나가면 돼"
                    show zabcho_sadt at right

                    kp "응"
                    hide zabcho_sadt
                    show zabcho_sad at right

                    km "(아까 식물원에서부터 저기압이네..)"

                    km "무슨일 있어?"
                    hide zabcho_sad
                    show zabcho_sadt at right

                    kp "..어? 아니야 없어 얼른 가자~"
                    hide zabcho_sadt

                    km "으음.."
                    hide kroom
                    scene kecho_hotel_in

                    km "체크아웃하러 왔는데요"
                    show kjicwon 

                    kj1 "아 네~ 즐거운시간 보내셨나요?"
                    hide kjicwon

                    km "네~"
                    show kjicwon

                    kj1 "즐거운시간 보내셨다니 다행입니다. 체크아웃 되셨습니다. 다음에 또 방문해 주세요."
                    hide kjicwon
                    hide kecho_hotel_in
                    scene kdark

                    kz "미야옹"
                    hide kdark
                    scene kdamjang

                    km "응? 무슨소리지?"

                    kl "담장위에 검은색 털과 오드아이 눈을 가진 고양이가 쳐다보고 있다"

                    km "엇 고양이네 여기선 처음보는 고양이인데?"
                    hide kdamjang
                    scene ndamjang
                    kl "고양이가 담장을 내려와 [man_name]의 다리에 머리를 부빈다"
                    show kcat at left
                    kk "애옹"
                    hide kcat
                    km "간택 강했다.."

                    km "목줄이 없는거 보니까 주인 없는 고양이 같은데.. 너 나를 간택한거니?"
                    show kcat at left
                    kk "애애애옹"
                    hide kcat
                    km "그렇구나! [zabcho_name], 우리 이 고양이 데려가자"
                    show zabcho_smilet at right
                    
                    kp "좋은 생각이야 이렇게 큐티뽀짝한 고양이가 우리를 선택한거니까 이건 운명이야."

                    km "좋아!"
                    hide zabcho_smilet
                    show kcat

                    km "그럼 고양이 이름을 정해주자"
                    show zabcho_smilet at right

                    kp "네가 정해줘!"
                    hide zabcho_smilet

                    km "음.. 그럼 네 이름은"

                    $ cat_name = renpy.input("고양이의 이름을 입력해주세요.", length = 32)

                    km " 좋아 이제부터 네 이름은 [cat_name](이)야"

                    km "잘부탁해 [cat_name]!"
                    hide kcat
                    show zabcho_smilet at right

                    kp "잘부탁해~"
                    show kcat

                    kc "애옹~"
                    hide zabcho_smilet
                    hide kcat
                    hide ndamjang
                    scene kdark

                    kl "그렇게 우리의 짧은 여행은 뜻밖의 동료와 함께 끝났다"

                    kl "-한달후-"
                    hide kdark
                    scene kbright

                    km "음.. 여긴 어디지? 아 꿈속이구나"

                    km "무슨 꿈이지 아무것도 없네.."

                    kz "....ㅇ이를 ㄷ와즈..."

                    km "음? 어디서 소리가 들리는데?"
                    hide kbright
                    scene kblindgod

                    kz "그 아ㅇ를 ..잡ㅊ를 도ㅇㅈ..."

                    km "누구세요?"

                    kz "ㅈ초를!!!"
                    hide kblindgod
                    scene kdark

                    km "헉!"
                    hide kdark
                    scene kbedroom

                    km "하...하..."

                    km "이게 무슨 꿈이지..?"
                    show zabcho_smilet at right

                    kp "[man_name]! 아침먹... 너 왜 이렇게 식은땀을 흘려?"
                    hide zabcho_smilet

                    km "어? 내가? 진짜네..."

                    km "꿈자리가 사나웠나봐.. 별일 아니야"
                    show zabcho_sadt at right

                    kp "꿈? 무슨꿈이었는데?"
                    hide zabcho_sadt
                    show zabcho_sad at right

                    km "그게.. 기억이 안나네"
                    hide zabcho_sad
                    show zabcho_sadt at right

                    kp "흠.. 어디 아픈건 아니지?"
                    hide zabcho_sadt
                    show zabcho_sad at right

                    km "응 괜찮아 아 참 아침 먹으라고? 그럼 나 씻고 갈게 땀을 좀 많이 흘려서.."
                    hide zabcho_sad
                    show zabcho_sadt at right

                    kp "알겠어"
                    hide zabcho_sadt

                    km "하.. 그게 무슨 꿈이었지? 잡초라고 했던것 같은데... 도저히 기억이 나지 않아"

                    km "설마 그 잡초인가?...."

                    km "아니다.. 그저 꿈일뿐이야.....그래도 [zabcho_name]을 더 신경쓰는게 낫겠다.."

                    km "한달전부터 묘하게 다운된것 같기도 하니까"
                    
                    km "밥이나 먹으러 가자"
                    hide kbedroom
                    scene kkitchen
                    show zabcho_smilet at right

                    kp "어서와 오늘은 오므라이스야!"
                    hide zabcho_smailet
                    show zabcho_smile at right

                    km "맛있겠다"
                    hide zabcho_smile
                    show zabcho_smilet at right

                    kp "히히 먹어봐"
                    hide zabcho_smailet
                    show zabcho_smile at right

                    km "음~ 점점 발전하는데? 너무 맛있어"
                    hide zabcho_smile
                    show zabcho_smilet at right

                    kp "맛있지!"
                    hide kkitchen
                    hide zabcho_smilet
                    scene kdark
                    
                    kl "잠시후"
                    hide kdark
                    scene kkitchen
                    show zabcho_smilet at right

                    kp "우리 오늘은 뭐할까?"
                    hide zabcho_smilet
                    show zabcho_smile at right

                    km "음.. 오늘은 안가본데 가보자"
                    hide zabcho_smile
                    show zabcho_smilet at right

                    kp "오오 어디?"
                    hide zabcho_smilet
                    show zabcho_smile at right

                    km "영화관 어떼? 요즘 영화 개봉한것도 많으니까"
                    hide zabcho_smile
                    show zabcho_smilet at right

                    kp "좋아!!"
                    hide zabcho_smilet

                    km "그럼 미리 예매하고 가자 뭐로보지.."

                    menu:
                        "빨간풍선(호러)":
                            jump k_13
                        "내 남친이었던 그와함께(로맨스)":
                            jump k_14
                        "윈카: 마법의 사탕을 찾아서(판타지)":
                            jump k_15
                        "나의 사랑하는 봉순(개그)":
                            jump k_16

                    label k_13:
                        show zabcho_smilet
                        kp "공포물? 재밌을 것 같아!"
                        

                        kl "[zabcho_name]은(는) 공포물을 좋아한다."
                        $kh +=10
                        hide zabcho_smilet
                        jump k_17

                    label k_14:
                        show zabcho_smilet
                        kp "로맨스물? 로맨스를 보다보면... 너랑..ㅎㅎ"
                    
                        kl "[zabcho_name]은(는) 주인공과의 망상에 빠졌다."
                        $kh +=15
                        hide zabcho_smilet
                        jump k_17

                    label k_15:
                        show zabcho_sadt
                        kp "판타지? 지금 나한테 일어난일만큼 판타지가 있을까?"

                        kl "[zabcho_name]은(는) 판타지가 지루한 것 같다"
                        $kh -=10
                        hide zabcho_sadt
                        jump k_17

                    label k_16:
                        show zabcho_sadt
                        kp "개그물...? 흠.. 요즘 개그는  나랑 안 맞더라고"

                        kl "[zabcho_name]은(는) 개그에 흥미가 없다."
                        $kh -=15
                        hide zabcho_sadt
                        jump k_17

                    label k_17:

                        km "2시 30분걸로 예매했어. 이거 먹고가면 되겠다"
                        show zabcho_smilet at right

                        kp "웅"
                        hide zabcho_smilet
                        hide kkitchen
                        scene kdark

                        kl "-영화관-"
                        hide kdark
                        scene ktheater

                        km "표는 여기있고 영화관 왔으니까 팝콘 먹어야지. 저기가서 사올게"

                        km "뭘로 시키지?"

                        menu:
                            "플레인 팝콘":
                                kl "가장 기본적인 맛이지 고소한맛이 일품이다"
                                jump k_18
                                
                            "캬라멜 팝콘":
                                kl "캬라멜 팝콘은 달콤한 맛이다"
                                jump k_19

                        label k_18:
                            
                            km "플레인 팝콘으로 사왔어"
                            show zabcho_popcorn at left
                            show zabcho_smilet at right

                            kp "음~ 고소해 맛있다 너무 달지 않아서 좋아"
                            $kh +=5
                            kl "[zabcho_name]은(는) 고소한 맛이 마음에 든다."
                            hide zabcho_popcorn
                            hide zabcho_smilet
                            jump k_20

                        label k_19:

                            km "캬라멜 팝콘으로 사왔어"
                            show zabcho_popcorn at left
                            show zabcho_sadt at right

                            kp "음.. 너무 달아.."
                            $kh -=5
                            kl "[zabcho_name]은(는) 단맛을 싫어한다."
                            hide zabcho_popcorn
                            hide zabcho_sadt
                            jump k_20

                        label k_20:
                            km "이제 영화시간 다 됐다 가자"
                            show zabcho_mung at right

                            kp "응"
                            hide zabcho_mung

                            hide zabcho_theater
                            scene zabcho_theater_loading
                            pause 2.0
                            hide image_name with dissolve
                            scene zabcho_theater

                            show zabcho_smilet at right

                            kp "생각보다 더 재밌었어"
                            hide zabcho_smilet
                            show zabcho_smile at right

                            km "다행이다"

                            km "나온김에 저녁먹고 들어가자"
                            hide zabcho_smile
                            show zabcho_smilet at right

                            kp "그랭"
                            hide zabcho_smilet
                            hide zabcho_theater
                            scene kdark

                            kl "-인프론트 스테이크 하우스-"
                            hide kdark
                            scene krestaurant

                            km "뭐로 먹지? 음.. 일단 기본 2인세트로 시키자"
                            show zabcho_smilet at right

                            kp "좋아요~"
                            hide zabcho_smilet

                            kj1 "주문 도와드리겠습니다."

                            km "저희 2인세트로 주세요. 굽기는 미디움웰던으로 부탁드립니다."

                            kj1 "알겠습니다. 그렇게 준비하도록 하겠습니다."

                            km "여기가 리뷰가 좋더라고 너랑 와보고 싶었어."
                            show zabcho_sickt
                            
                            kp "응..."
                            hide zabcho_sickt
                            show zabcho_sick at right

                            km "(흠.. 오늘따라 [zabcho_name](이)가 좀 피곤해보이네.."
                            hide zabcho_sick

                            kj1 "2인세트 나왔습니다."

                            km "가운데에 놔주세요"
                            hide krestaurant
                            scene ksteak

                            kp "와 스테이크 영롱해 얼른 먹자"

                            km "맛있게 먹어"
                            hide ksteak
                            scene krestaurant

                            kj1 "손님" 
                        
                            km "네?"

                            kj1 "저희가 사진 찍어주는 이벤트를 하고 있는데 한장 찍으시겠어요?"

                            km "사진이요? 어때?"
                            show zabcho_happy at right


                            kp "나는 좋아. 너랑 추억 하나라도 더 쌓고싶어"
                            hide zabcho_happy

                            km "그럼 찍어주시겠어요?"

                            kj1 "네 찍겠습니다. 웃으세요~ 하나, 둘, 셋"
                            show zabcho_smile at right
                            #찰칵소리

                            kl "찰칵"
                            hide zabcho_smile

                            kj1 "네 되셨어요. 여기 있습니다. 맛있게 드세요."

                            km "감사합니다~"

                            kl "-잠시후-"

                            km "배부르다 맛있었어"

                            km "이제 집에 갈까?"
                            show zabcho_sadt at right

                            kp "으응.."
                            hide zabcho_sadt
                            show zabcho_sad at right

                            kl "[zabcho_name]의 상태가 별로 안좋아 보인다."

                            km "안되겠다... 얼른 집에가자"
                            hide zabcho_sad 
                            hide krestaurant
                            scene kdark

                            kl "-집-"
                            hide kdark
                            #털썩하는 효과음

                            scene zabcho_sick_CS
                            pause 2.0
                            hide image_name with dissolve

                            km "!!! [zabcho_name]!!"
                            scene khome2

                            km "너 왜그래 갑자기 왜 어.... 아니..."
                            show zabcho_ft at right

                            kp "하하... 이제 우리 헤어져야할 때가 온것같네.."
                            hide zabcho_ft
                            show zabcho_f at right

                            km "그게 갑자기 무슨소리야.... 왜.. 아니 얼른 119를.."
                            hide khome2
                            scene khand
                            pause 2.0
                            hide image_name with dissolve
                            scene khome2
                            hide zabcho_f
                            show zabcho_ft at right

                            kp "너랑 만날 수 있어서 너무 행복했어..."

                            kp "다른 인간들은 하찮은 잡초따위 밟고 지나가는 존재였을 뿐이었는데"

                            kp "너는 달랐지.. 나 사실.."
                            hide zabcho_ft
                            show zabcho_f at right

                            km "아니야.. 말하지마 더이상.... 아니... 이렇게는 못헤어져"

                            km "분명 방법이 있을거야.. 방법이..."

                            kp "너랑 함께했던 시간 더 없이 벅차고 좋았어.."
                            hide zabcho_f
                            show zabcho_ft at right

                            kp "너 덕분에 나는 나의 시간을 살 수 있었어.. 그러니.."

                            kp "너도 이제 너의 시간을.. 삶을 살길 바래.."

                            kp "널 좋아했어.."
                            hide zabcho_ft 
                            show zabcho_f at right      

                            km "흐흑"
                            hide zabcho_f
                            show zabcho_ft at right

                            kp "와 나 진짜 이기적다.. 그치? 이제와서 고백을 하네.."

                            kp "그치만 꼭 하고 싶던 말이었어"
                            hide zabcho_ft
                            show tumyeong at right

                            kp "이런 울지마 나 사라지는거 아니야.. 그저 너가 아껴주었던 잡초의 모습으로 돌아가는 것 뿐이야"

                            kp "나는 그 모습으로 언제까지나 너의 곁에 있을거야.. 그러니 제발..."
                            scene kcartoon1
                            pause 1.5
                            hide image_name with dissolve
                            scene khome2

                            kp "울지마..."

                            km "[zabcho_name]...."

                            km "나도 사실 널..."
                            hide tumyeong
                            scene kbright
                            pause 2.0
                            hide image_name with dissolve
                            scene khome2
                            show weed at right

                        if kh >= 60:
                            jump kjin_ending
                        elif 0 <= kh <= 59:
                            jump kbad_ending
                        else:
                            jump khospital_ending

                        label kjin_ending:
                            km "아.. 안돼.."

                            km "........."
                            hide weed

                            kz "그대 울지 말거라."
                            scene kbright

                            km "..누구세요..? 여기는 어디지?"
                            scene kgodCS

                            kz "본좌는 너에게 잡초를 보내준 풀의 여신 데메르이니라."
                            hide kgodCS
                            scene kbright

                            km "...예?"
                            show zabcho_godt

                            kg "본 모습을 보이기 위해 잠시 임의의 공간으로 바꿨다."
                            hide zabcho_godt
                            show zabcho_god

                            km "......예?"
                            hide zabcho_god
                            show zabcho_godt
                            
                            kg "그래 내가 왜 네 앞에 나타났는지 궁금하겠지?"

                            kg "나의 갸륵한 아이가 나에게 소원을 빌었단다."

                            kg "'그가 행복했으면 좋겠어요'라고.."

                            kg "아주 귀엽지 않느냐?"

                            kg "그 작은아이가 그대 같은 먼지의 행복을 빈다는 것이"

                            kg "그 아이의 염원을 보고 싶었어"

                            kg "그래서 들어주었지 그아이의 소원을"

                            kg "그리고 본좌는 저 고양이의 몸을빌려 그대와 내 아이를 지켜보고 있었다."

                            kg "이것이 그대에게 내 아이가 간 이유이다."
                            hide zabcho_godt
                            show zabcho_god

                            km "그렇다면.. 당신이 [zabcho_name]을(를) 제게 보내준 신이라면.."

                            km "제발 [zabcho_name]을(를) 다시 제게 돌려주세요.. 제발"
                            hide zabcho_god
                            show zabcho_godt

                            kg "훗 재밌군.. 서로가 서로를 이렇게나 위하다니"

                            kg "좋다 들어주지 그 염원."

                            kg "다만 댓가가 있다"

                            km "그 무엇이든 드릴 수 있습니다."

                            kg "다시는 원래살던 세계로 돌아가지 못한다 하여도?"

                            km "[zabcho_name]이 없는 세계는 제게 의미가 없습니다."

                            kg "그 염원 잘 받았다."
                            hide zabcho_godt
                            scene zabcho_bright
                            pause 2.0
                            hide image_name with dissolve
                            show zabcho_smilet at right
                            scene khome2

                            kp "음.. 안녕?"
                            hide zabcho_smilet
                            show zabcho_smile

                            km "으아아아아 [zabcho_name]..."
                            hide zabcho_smile
                            show zabcho_smilet at right

                            kp "울지 말라니까 바보"
                            show zabcho_godt at left
                            hide zabcho_smilet
                            show zabcho_smile at right

                            kg "아이야"
                            hide zabcho_smile
                            hide zabcho_godt
                            show zabcho_smilet at right
                            show zabcho_god at left

                            kp "당신이었군요.. 저의 소원을 들어준 분이.. 정말 감사합니다"
                            hide zabcho_smilet
                            hide zabcho_god
                            show zabcho_smile at right
                            show zabcho_godt at left

                            kg "이것이 너의 염원이었느냐?"
                            hide zabcho_smile
                            hide zabcho_godt
                            show zabcho_smilet at right
                            show zabcho_god at left

                            kp "네.. 저 덧없이 행복해요"
                            hide zabcho_smilet
                            hide zabcho_god
                            show zabcho_smile at right
                            show zabcho_godt at left

                            kg "그래 그것이면 됐다. 귀여운 아이야"

                            kg "앞으로도 그 염원을 간직하거라."
                            hide zabcho_smile
                            hide zabcho_godt
                            show zabcho_smilet at right
                            show zabcho_god at left

                            kp "예!"
                            hide zabcho_smilet
                            hide zabcho_god
                            show zabcho_smilet at right
                            hide kbright
                            scene khome2

                            kp "울보야 울지말고 나를봐"
                            scene zabcho_happy_CS
                            pause 2.0
                            hide image_name with dissolve
                            scene khome2

                            kp "나 여기있잖아?"

                            km "널 잃는줄 알았어."
                            show zabcho_smile at right

                            km "널 좋아해"
                            hide zabcho_smile
                            show zabcho_shy at right

                            kp "!!"
                            hide zabcho_shy
                            show zabcho_shy_smile 

                            kp "나도 좋아해 너를"
                            hide zabcho_shy_smile
                            scene zabcho_poraloid

                            return
                        
                        label kbad_ending:
                            hide weed
                            km "아.. 안돼.. 좋아한다는 말을 못해줬는데.."

                            km "이럴수는 없어.."

                            km "아...아......"
                            hide khome2
                            scene kdark         

                            kl "며칠후"
                            hide kdark
                            scene kmiss

                            km "보고싶어.."
                            hide kmiss
                            scene kgoodby
                            pause 2.0
                            hide image_name with dissolve
                            
                            return

                        label khospital_ending:
                            km "아..안돼 가지마.."
                            hide weed

                            km "흐흑...."
                            hide khome2
                            scene kdark

                            kl "............."
 
                            kn "ㅎㅈㅏ분...."

                            km "[zabcho_name](이)야? 너 어딨어? 네가 안보여"

                            kn "환자분!!!"
                            hide kdark
                            scene zabcho_hospital

                            km "헉"
                            show zabcho_nurse at left

                            kn "환자분 정신이 드세요?"
                            hide zabcho_nurse

                            km "여기가..어디..."
                            show zabcho_nurse at left

                            kn "환자분 여기가 어딘지 아시겠어요? 여기는 OO정신병원 입니다."

                            kn "환자분 정신착란 증상 있으셔서 여기로 옮겼습니다. 기억 나세요?"
                            hide zabcho_nurse

                            km "아.. 그랬지.... 나는"

                            km "죄송합니다. 저 기억 있습니다..." 
                            show zabcho_nurse at left

                            kn "정신이 드셔서 다행이에요. 그럼 저는 의사 선생님 불러올게요."

                            kn "아 그리고 아끼시던 잡초화분은 저기 선반위에 올려두었어요."
                            hide zabcho_hospital
                            hide zabcho_nurse
                            scene zabcho_origin

                            km "아...네...."
                            hide zabcho_origin
                            scene zabcho_hospital
                            show zabcho_nurse

                            kn "그럼 저는 이만.."
                            hide zabcho_nurse

                            kl "밖에서 의사와 간호사가 하는 이야기가 들린다"

                            kd "환자분이 정신을 차리셨다고요?"

                            kn "네 전에 화분 끓어안고 [zabcho_name](이)라고 부르시던것도 없어지고 망상증세도 없어졌습니다."

                            km "아.. 돌아왔구나..."

                            km "현실..."
                            scene kzabcho
                            with fade
                            pause 2.0
                            hide image_name with dissolve


                            return



                            


    return

    label k_10:
            scene kgameover
            pause 2.0
            hide image_name with dissolve
   
    return




    
    label kfirst:
        ke "(수상하다. 가슴에 비수가 날아와 꽂힌다. 얼른 내보내자)"

        ke "아니 됐고 내집에서 나가"

        kz "잠깐만 내 얘기 좀 들어줘.."

        ke "흠.. "
        jump ksec

    return        

   

