label mk1:
    $ renpy.notify('다음날')
    pause 2.0   
    play sound "hu_birdsound.ogg"
    ph "일어나라 인간! 심심하다!"
    show hu_looking
    ph "오늘은 짐에게 무엇을 가르쳐주겠느냐?"

    menu:
        "공원에 나가볼까?":
            $pl=pl+10
            hide hu_looking
            show hu_happy at left
            ph "좋다! 당장 놀러가가게 채비하거라!"
            scene hu_park
            play sound "hu_catsound.ogg"
            ph "와!! 고양이!!"
            hide hu_happy
            show hu_withcat
            menu:
                "털날려 내려놔":
                    $pl=pl-20
                    hide hu_withcat
                    show hu_withcat_anger at right
                    ph "뭐? 언행을 조심하도록 하여라. 이 조그마한것이 털이 날려봤자 니놈의 머리털과 몸 털에 비하면 귀여운 수준일것이니라."
                    pp "인간은 털이 많이 날리지 않아. "
                    ph "인간 주제에 말이 많구나. 털이 많이 빠져도 이몸이 마법으로 치우면 그만이니라. 그러니 그 입 다물라!"
                "고양이 좋아해?":
                    $pl=pl+15
                    hide hu_withcat
                    show hu_withcat2
                    ph "응!"
                    ph "이녀석들은 인간과 달리 아주 귀여운 구석이 많다! 일단 시끄럽지 않지! 그리고 인간과 달리 조금 먹고 쓸때없이 싸우지 않느니라. 그리고 생긴것부터가 아주 귀엽지 않느냐! 아마 이녀석도 마족의 후예일 것이다! ... ..."
            "휴는 그 뒤로 한참동안 고양이 얘기를 떠들었다."        
            
        "그냥 집에 있으면 안될까....":
            $pl=pl-5
            hide hu_looking
            show hu_look한심 at right
            ph "게으른것.\n마침 짐의 옷이 다 떨어졌느니! 사러 나가자꾸나!"
            pp '아 진짜 손 많이가는 꼬맹이네...'
            scene dresssalon
            show 으스대는 휴
            ph "그거 아느냐? 짐은 마왕. 돈을 만드는것쯤은 일도 아니니라. 마음껏 골라보거라!  "
            menu:
                "마왕님 옷부터 고르죠. 이리와보세요.":
                    $pl=pl+20
                    hide 으스대는 휴
                    show hu_happy at left
                    ph "응! 짐은 이런옷이 좋다."
                    "휴는 마법으로 이옷저옷 갈아입으며 꺄르륵웃었다."
                "오 저 옷 내스타일인데?":
                    $pl=pl-10
                    hide 으스대는 휴
                    show 시큰둥한 휴 at right
                    h "으음 짐에 눈에는 별로구나. 다른것을 들고와보거라"
                    "휴는 짜증이났는지 마력으로 옷을 이리저리 던져버렸다."
    scene street
    show 하품하는 휴
    ph "흐아암...짐은 배가 고프구나.이제 어디로 갈것이냐?"

    menu:
        "비싼 레스토랑":
            hide 하품하는 휴
            $pl=pl+20
            show hu_lighteye
            ph "짐이 요리 잘하는곳을 알아! 따라오거라!"
            scene 레스토랑
            ph "주인장!!!"
            scene 만찬이 차려진 레스토랑
            $ renpy.notify('밥 먹고 난 후')
            pause 2.0
            jump firstgnight
        "길거리 장터":
            hide 하품하는 휴
            $pl=pl-20
            show 가소로운표정의 휴
            ph "짐은 더러운 음식은 먹지 아니하느니라. 역시 하등한 인간다운 생각이로고."
            scene 야시장
            hide 가소로운표정의 휴
            show 아이스크림 가게 at right
            show hu_lighteye at left

            menu:
                "사줄까?":
                    $pl=pl+5
                    hide hu_lighteye
                    show hu_lookingfood
                    ph "마왕은 저런거 좋아하지 않아! 하지만 그대가 준 성의를 봐서 먹어주도록 하겠어. 짐은 너그러운 마왕이니까..!"
                    hide hu_lookingfood
                    $ renpy.notify('밥 먹고 난 후')
                    pause 2.0
                    jump firstgnight
                "ㅋ길거리 음식 싫어한다면서":
                    $pl=pl-10
                    hide hu_lighteye
                    show 정색한 휴 at left
                    ph "뭔가 큰 오해를 하고 있구나.짐은 이딴 인간들의 음식따위 줘도 먹지 않는다."
                    hide 정색한 휴
                    jump firstbnight