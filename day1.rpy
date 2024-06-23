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

    #게임오버
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