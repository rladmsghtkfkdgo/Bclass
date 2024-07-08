label rps:
    menu:
        "가위 바위 보!"
        "가위":
            $pp_game="가위"
        "바위":
            $pp_game="바위"
        "보":
            $pp_game="보"          
    $ choice = renpy.random.choice(("가위","바위","보")) ## These are the events I want to have the code choose from.
    ph "[choice]" 
    if pp_game == choice:
        ph "비겼구나!, 다시하자!"
        jump rps
    elif (pp_game == "가위" and choice == "보") or (pp_game == "바위" and choice == "가위") or (pp_game == "보" and choice == "바위"):
        $hu_game=True
    else:
        $hu_game=False
    if hu_game:
        pp "이겼다!"
        "주변에 검은 안개가 피어오른다"
        ph "감히 인간따위에게 짐이 질리가 없다..."
        pp "아니 이런 미친, 게임이었잖아요."
        ph "건방진 인간. 네놈이 원하는게 집에서 있는것이었나? 허나 이 집의 주인은 짐. 짐이 친히 너를 이 집에 영원히 머물게 해주마."
        pp "예? 그게 무슨"
        ph "이 집에 초가 왜 많은줄 아느냐! 내 너를 이집의 촛불중 하나로 바꿔버릴것이다!!"
        pp "알겠어요 알겠다고요."
        pp "나가면 되잖아요 나가면."
        menu:
            "흠..(이곳에서 초로 변해버릴 것은 아니니 골라보자)"
            "바다 갈까?":
                jump h4_ocean
            "도서관 갈까?":
                jump hu_library
            "찜질방 갈까?":
                jump hu_shower
    else:
        ph "후후후. 어리석은 인간이여. 감히 짐을 이기려 드느냐."
        ph "벌을 줘야 하지만, 짐은 너그러운 마왕. 기회를 주마! 나를 데리고 동물원에 가도록."
        jump pzoo