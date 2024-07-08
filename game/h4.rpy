label mk3:
    scene black
    with fade
    $ renpy.notify('다음날')
    pause 2.0 
    play music "hu_birdsound.ogg"
    #play sound "옷뒤적거리는 소리"
    ph "인간은 잠도 많구나. 오늘은 짐이 가고싶은 곳이 있다. 따라오라."
    stop music
    scene hu_room2
    menu:
        "얌전히 따라간다":
            ph "동물원에 갈 것 이다!"
            jump pzoo
            
        "싫다.오늘은 꼭 집에서 쉬어야겠다.":
            show hu_한심하게보는휴 at left
            ph "정말 게으른 인간이로구나..."
            pp "집에서 할 수 있는 놀이도 많아"
            ph "예시를 들어보거라."
            pp "뭐, 가위바위보 라던가."
            ph "오냐 받아주지. 하지만 니놈이 이기지 못하면 벌을 받을 줄 알거라."
            jump rps



                