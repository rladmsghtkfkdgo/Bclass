label mk1:
    $l = 0
    play sound "breakingthings.ogg"
    " ?"
    menu:
        "무슨일이지?저쪽방에서 소리가 난건가?":
            scene hu_huntingmouse
            with fade
            " "
        "뭐야 무섭게...밖으로 도망쳐야하나..?":
            play sound "dooropen.ogg"
            show hu_comein at right
            "너로구나 침입자가!"
        
    p "?!"
    scene room3
    #show hu_comein at right
    show hu_intro1 at right
    h "이몸은 르웨인 디카프리나 엘란트 휴! 마왕이시다!"

    menu:
        "미친여자다":
            hide hu_intro
            $l=l-10
            #show 울먹이는 휴 at right
            h "마왕이라고!!"
            p "어 응 네..." 
            #hide 울먹이는 휴 at right
        "마왕...?":
            #hide hu_intro            
            $l=l+25
            #show 어른휴 at right
            h "그래. 그대는 누구인데 나의 처소에 있는것이지?"
            $test=renpy.input('')
            #hide 어른휴 at right 



        
    #show 눈을 반짝이는 휴
    h "!! 너로구나! 마신이 내린 짐의 하수인!"
    p "제가요?"
    #hide 눈을 반짝이는 휴
    #show 고양이를 안고있는 휴
    h "응. 짐은 원래 마계를 이끌어갈 마왕의 자손이었다."
    #play music 마계
    #scene 마계
    h "마왕은 피에따라 계승되는것은 아니나\n강한자의 자식일수록 강한건 당연한것이라 "
    h "짐이 다음 마왕을 물려받을 예정이었지."
    h "허나 일순간 마계와 인간세계 사이에 균열이 생겼고,\n짐은 눈 깜빡하니 인간세계에 떨어져있었다."
    #stop music
    #scene room2
    #with dissolve 
    #show hu_시무룩
    h "그때 짐은 태어난지 2년된 유체였다네.\n자네의 이름은 무엇인고?"
    #"내 이름은" 이미지 그러나 ui 바꾸고싶은
    $name=renpy.input("")
    $l=l+30


    #show hu_hands with chest
    h "그래 [p]! 짐에게 인간세상을 알려다오!\n 짐이 화려하게 이 세상을 명망시켜보도록하겠다!"
    p "아니 세상을 멸망시키면 나는 어떻ㄱ..."
    "시야가 흔들린다."
    #hide 성인 휴 팔 벌리고 있는 포즈
    h "흠. 이정도로 기절하다니 인간이라 그런지 확실히 나약하구나.\n 짐은 너그러운 마왕이니 다음부턴 마력을 조정해보겠느니라!"