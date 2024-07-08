label firstgnight:
    scene 공원_밤
    show hu_smile at left
    ph "밤공기가 좋구나!"
    pp "그러게."
    hide hu_smile
    show hu_nug
    ph "짐에게 궁금한것이 있느냐?\n 지금 짐의 기분이 좋으니 하나쯤 대답해주도록하겠다!"
    menu:
        "휴는 뭘 좋아해?":
            $pl=pl+5
            $pB=True
            hide hu_nug
            show hu_happy at left
            ph "짐은 고양이를 좋아해! 그리고 아이스크림과 빨개지는 하늘을 좋아한다! 지금 이순간이 짐이 가장 좋아하는 순간이라 할 수 있지!"
        "내가 오기 전까지는 혼자지냈어?":
            $pl=pl+10
            $pB=False
            hide hu_nug
            show hu_talking at left
            ph "응...혼자였지... 하지만 마왕은 외로움따위 타지 않아! 인간 하나 있거나 없거나 달라지는건 없느니라!"
        "오늘 즐거웠어?":
            $pl=pl+20
            $pB=True
            hide hu_nug
            show hu_smile at left
            ph "응. 인간주제에 제법이더구나. [pp]. 내가 너의 이름정도는 기억해주겠다."
            hide hu_smile
            pp "그래. 너가 즐거웠다면 된거지."
            show hu_happy
            ph "하하 기특한 말을 하는구나! 상으로 내일 아침은 내가 구해다주도록하마. 어서 집에 가자!"
            jump mk2
        "조용히 집이나 가자":
            $pl=pl-20
            $pB=False
            hide hu_nug
            show hu_anger at left
            jump firstbnight
    scene hu_park_night
    pp "그렇구만..."
    show hu_happy at left
    ph "하지만 오늘 즐거웠어! 인간따위가 짐을 이렇게 기쁘게 만들다니! 칭찬해주겠다."
    "휴는 부끄러운지 총총 걸어갔다."

    jump mk2

label firstbnight:
    scene 휴가 고양이를 쓰다듬으며 걸어가는 뒷모습
    "휴는 혼자 집으로 가버렸다."
    scene black
    with fade
    $pB=False
    jump mk2