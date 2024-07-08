label mk2:
    scene black 
    with fade            
    $ renpy.notify('다음날')
    pause 2.0        
    if pB:
        show hu_withcat at right
        ph "[pp]! 일어나라! 먹을것을 구해왔느니!"
        "일어나니 아침이 차려져있다."
        scene hu_breakfast
        menu:
            "음,맛있네. 휴가 한거야?":
                $pl=pl+5
                show 뿌듯해하는휴 at right
                ph "후후 요리또한 마왕의 덕목이니라. 휴는 못하는게 없지!"
                pp "하하.역시 마왕님 대단하네."
                ph "이런것쯤이야 별거 아니니라. 다음에 또 먹고싶다면 내게 말하거라!"
                pp "그래 다음에 또 해줘."
                hide 뿌듯해하는휴
            "고마워.다음엔 내가 해줄게.":
                $pl=pl+10
                show 눈감고생각하는휴
                ph "휴는 아이스크림이 좋아. 신선한 아이스크림으로 잡아오도록."
                pp "휴. 아이스크림은 살아있는게 아니야...식사대용도 아니고..."
                hide 눈감고생각하는휴
                show 가소롭다는듯이 눈을 붉게 빛내는 휴
                ph "인간. 나는 마왕. 인간따위의 식사를 한다고 기력이 차지 않는다. 허면 내 기력을 채울만한 싱싱한 인간을 여럿 잡아오겠느냐?"
                pp "생각해보니 신선한 아이스크림 좋은거같아. 응 그렇고말고"
                hide 가소롭다는듯이 눈을 붉게 빛내는 휴
            "웩. 어디서 사온거야. 상한거같은데":
                $pl=pl-10
                show hu_anger
                ph "먹지 않아도 되느니. 하등한 인간놈이 뭘 알겠느냐."
                pp "하등....;다음부터 그냥 요리는 내가 할게."
                ph "기가 차는구나. 짐이 네놈따위를 위해 아침을 또 차려줄 줄 알았느냐?"
                pp "..."
                hide hu_anger
            "와. 너.무.맛.있.어.":
                $pl=pl-30
                show hu_anger
                ph "인간. 감히 짐을 앞에두고 거짓을 고하는구나. 내가 그것하나 간파하지 못할것같으냐?"
                pp "아..아니 정말 맛있어서...."
                ph "닥치거라.짐은 바람 좀 쐬고 오겠다."
                "휴는 단단히 화가난것같다."
                jump mk3
    else:
        ph "어이 인간. 일어나라. 참으로 게으르구나.쯧"
    scene hu_room
    show hu_talking at left
    ph "그래, 오늘은 짐에게 무엇을 경험시켜주겠느냐?"
    menu:
        "공연보러가기":
            ph "공연! 길가에서 인간들이 떠드는것을 들었다!"
            pp "응 그거 맞아요. 가죠."
            scene black
            with fade
            pause 2.0
            $ renpy.notify('공연이 끝나고 난 후')
            pause 2.0
            scene hu_theater2 
            play sound "hu_clapping.ogg"        
            show hu_crying2 at left
            with Dissolve(1.0)
            ph "우,,,으 마왕은 울지 않아... 이것은 짐의 땀이니라..."
            pp "ㅋㅋㅋㅋ그래그래 밥이나 먹으러 가자"
            hide hu_crying2
            show hu_happy at left
            ph "휴에게 특별한 경험을 또 안겨주었으니. 저녁은 휴가 줄게!공원으로 가자꾸나!"
            scene park_evening
            show hu_intro1
            ph "mach Essen!"
            play sound "hu_bubble.wav"
            show hu_intro1 at left with move
            show hu_parkdinner
            pp "이게뭐야!!!"
            hide hu_intro1
            show hu_happy at left
            ph "양껏 들거라. 짐이 준비한 만찬이니라."
            pp "휴. 인간은 이걸 다 먹지 못해..."
            hide hu_happy
            show 깔보기휴 at left
            ph "쯧쯔.. 그러니 인간들이 나약한것이다!"
            hide 깔보기휴
            scene hu_withcat_park
            play sound "hu_catsound.ogg"
            ph "야옹!"
            menu:
                "털날려 내려놔":
                    scene hu_park
                    $pl-=20
                    show hu_withcat1 at right
                    ph "네놈. 여전히 깨닫는게 없는거같구나."
                    pp "아니 밥먹는데 털날리잖"
                    hide hu_withcat1
                    show hu_intro2 at right
                    ph "Wechseln Sie zu Katze"
                    "[pp]는 고양이로 변했다"
                    hide hu_intro2
                    show hu_anger at left
                    ph "오만한 인간이여.짐이 보기엔 인간은 짐승과 다를바가 없거늘, 버릇없음이 하늘을 찌르는구나."
                    pp "먁 미약(아니 진짜 어이없네 마법 풀어봐요)"
                    ph "그 마법은 12시간동안 지속될것이니 그동안 오만한 마음을 바로잡고 그들이 인간과 다름없을 깨닫도록하라."
                    pp "므먀미악 므아오..?먁먀오!!!(아니잠깐만 진짜로..? 풀어줘 이 마왕아!!)"
                    scene hu_room2
                    with fade
                    "휴의 마법에 [pp]는 고양이인채로 집 카펫위에서 잠이들었다."
                    jump mk3
                ".....으휴 밥먹자 마왕님.":
                    $pl+=15
                    scene hu_park
                    show hu_withcat at left
                    ph "응!! 야옹이도 배고프다고 했다. 같이 먹을것이니라!"
                    pp "그래그래"
                    #show hu_withcat_eating
                    pp "휴 다먹었어? 디저트가게 갈까?"
                    ph "오랜만에 마음이 통하는 인간이로고! 안내해라!"
               
        "피시방가기":
            ph "피시방....기계들이 널려있는 그곳말이냐? 인간들은 도무지 이해할 수가 없군...굳이 지하에 갇혀서 짜여진 마력을 보며 좋아하다니."
            pp "휴...내가 아는 피시방이 맞다면 그곳은 마력으로 돌아가는게 아니야.."
            ph "헹 그럴리가 없느니! 마력이 아닌데 그렇게 돌아갈수는 없느니라"
            #scene hu_pcroom
            #show 2시간후
            show hu_happy at left
            ph "[pp]!!! 이거 아주 재미있구나! 인간들이 왜 이 기계만 찾아다니는지 알것도 같다!"
            pp "저녁은 여기서 해결할까? 여기 음식도 맛있어."
            hide hu_happy
            show hu_lighteye at left
            ph "이곳은 음식도 대령한단말이냐? 으음 쾌락으로 인간들 모두를 가둬두려는 속셈이로고.."
            pp "다 놀았어? 나가서 아이스크림먹을까요?"
        "공방가기":
            ph "공방..? 공방전을 말하는것이냐?"
            pp "음 그게 아니라 무언가를 만드는 장소를 공방이라고해요. 휴는 뭐 만들어보고싶은거 없어?"
            ph "아이스크림!"
            pp "흠...비슷한곳을 알아. 가자."
            #scene 임실치즈마을st.아이스크림이랑 치즈만드는곳
            ph "인간! 특별히 니놈이 만든 아이스크림을 내게 진상할 수 있는 기회를 주지."
            menu:
                "그럼 우리 바꿔먹어볼까?":
                    $pl+=10
                    ph "좋다! 이 휴님이 만든것을 맛볼 기회를 주마"

                "아냐 휴 각자꺼 먹자 그냥..ㅎ":
                    $pl-=5
                    h "네놈은 목숨이 여러개인가보구나. 감히 짐의 말에 토를 다는걸 보아하니. 어디 네놈이 아이스크림이 되는게 빠를지 곱게 니놈의 아이스크림을 내놓는게 빠를지 겨뤄보겠느냐."
                    p "아뇨 가져가세요..."
    scene hu_street
    show hu_icecream at left
    ph "[pp]. 오늘 덕분에 즐거웠느니. 네놈에게 마신의 가호가 있기를 바라마."
    menu:
        "휴는 왜 세상을 멸망시키려는거야?":
            $pl-=5
            ph "그야 이몸은 마왕이니까. 세상을 지배해서 마계로 만들어 군림하는것이 이몸의 숙명이니라."
            pp "그렇게 되면 나와 이렇게 놀 수 없는데도?"
            ph "...[pp]. 인간은 언젠가 죽지. 너 하나로 포기할만큼 내 숙명은 하찮은것이 아니야."
            pp "...그래"
        "그래그래 얼른 집이나 가자 마왕님.":
            $pl+=10
            ph "오냐! 오늘은 기분이 좋으니 이몸의 마법으로 이동시켜주마!"
            #show hu_magic_happy
            pp "아뇨 괜찮은데요.마법을 써서 제가 안전하다는 보장이..."
            ph "לך הביתה!!"
            pp "아 제발."
            scene black
            with fade

    jump mk3
    