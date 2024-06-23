label mk:
    scene hu_room2
    $pl = 0
    play sound "hu_breakingthings.ogg"volume 0.1
    pause 2.0
    menu:
        "무슨일이지?저쪽방에서 소리가 난건가?":
            scene hu_huntingmouse with fade
            "쥐새낀줄알았는데, 넌 또 뭐야." 
        "뭐야 무섭게...밖으로 도망쳐야하나..?":
            "으아...근데 왠지 문으로 나가기도 좀 무서운데.."
            pause(2.0)
            play sound "hu_dooropen.ogg"volume 1.0
            show hu_comein at right
            "너로구나 침입자가!"
        
    pp "?!"
    scene hu_room3
    show hu_intro1 at left
    ph "이몸은 르웨인 디카프리나 엘란트 휴! 마왕이니라."

    menu:
        "미친여자다":
            $pl=pl-10
            hide hu_intro1
            show hu_crying with move
            ph "마왕이라고!!"
            pp "어 응 네..." 
            hide hu_crying
        "마왕...?":
            hide hu_intro1            
            $pl=pl+25
            show hu_너그러움
            ph "그래. 그대는 어째서 나의 처소에 있는것이지?"
            $ptest=renpy.input('')
            hide hu_너그러움

    "[pl]"
        
    show hu_lighteye at left
    ph "!!!"
    ph "너로구나! 마신이 내린 짐의 하수인!"
    pp "제가요?"
    hide hu_lighteye
    show hu_withcat
    ph "응. 짐은 원래 마계를 이끌어갈 마왕의 자손이었다."
    play music "hu_magye.ogg"
    scene hu_magye
    with fade
    ph "마왕은 피에따라 계승되는것은 아니나\n강한자의 자식일수록 강한건 당연한것이라 "
    ph "짐이 다음 마왕을 물려받을 예정이었지."
    ph "짐은 유체들중에도 가장 강한 개체에 속했어."
    scene hu_magye1
    ph "허나 일순간 마계와 인간세계 사이에 균열이 생겼고"
    ph "짐은 눈 깜빡하니 인간세계에 떨어져있었다."
    ph "처음엔 인간들을 모두 죽여버릴까 했지만. 왜인지 인간세상에선 마력도 주술도 내 마음대로 되지 않더군."
    stop music
    scene hu_room2
    with dissolve 
    show hu_시무룩
    ph "그때 짐은 태어난지 2년된 유체였다네. 다시 차원문을 열어볼까했지만 그것또한 짐의 뜻대로 되지 않았다."
    ph "그대는 이름이 무엇인고?"
    $pname=renpy.input("내 이름은 ")
    $pl=pl+30
    "[pl]"


    show hu_handswithchest
    ph "그래 [pp]! 짐에게 인간세상을 알려다오!\n 짐이 화려하게 이 세상을 명망시켜보도록하겠다!"
    pp "아니 세상을 멸망시키면 나는 어떻ㄱ..."
    "시야가 흔들린다."
    hide hu_handssithchest
    scene black
    with fade
    ph "흠. 이정도로 기절하다니 인간이라 그런지 확실히 나약하구나.\n 짐은 너그러운 마왕이니 다음부턴 마력을 조정해보겠느니라!"
    jump mk1