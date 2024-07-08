label pzoo:
    scene hu_street
    menu:
        ph "[pp],이 세계의 동물원에 가봤는가?"
        "네":
            show hu_anger
            ph "거짓. 나를 화나게 할 셈이더냐?"
            return 
        "아뇨":
            ph "잘 되었구나. 짐이 첫 동행인것이니!"            
        
    ph "이 세계의 동물들은 마계의 생물들과 많이 닮았다. 하여 종종 어릴때가 생각나면 이곳에 들르곤 했지."
    pp "하지만 동물원에는 고양이가 없지 않아?"
    ph "응. 마계에도 고양이는 없었다. 고양이는 이몸이 인간계에 떨어지고 처음으로 정을 붙인 생명체다."
    scene hu_zoowall
    ph "자 길을 열어줄테니 들어와라."
    "휴가 손을대자 철조망으로 막혀있던 벽이 스르륵 녹아내렸다."
    pp "??그래도 되는거에요?"
    ph "ㅋ짐은 마왕. 물론 마왕도 세계의 질서를 무너뜨리면 안된다. 하지만 그렇게 따지면 짐이 어떻게 화폐를 만들어낼것같은가?"
    menu:
        "그야 가짜돈인줄알았다":
            $pl-=5
            show 찡그린 휴
            ph "짐은 거짓말따위 하지않아. 그럴필요가 없기때문이다"
        
        "....사기꾼":
            $pl+=10
            ph "하하! 극찬이로구나. 상대를 속이고 기만하는것이 마족의 특성! 마왕인 짐에게 이정도는 기본이니라."
    scene hu_zoo
    show hu_뿌듯 at left
    ph "그거 아느냐? 짐은 어떤 생명체든 소통이 가능하느니라."
    pp "엥 진짜요? 마법안쓰고도요?"
    hide hu_뿌듯
    show hu_smile at left
    ph "응. 애초에 네놈이 지금 듣고 있는 이 말이 무슨언어인지 알고있느냐?"
    pp "한국어 아닌가..?"
    ph "한국어? 그게 무엇인지는 모르겠지만 짐은 인간의 언어를 모른다. 그저 짐의 울음소리가 네놈의 뇌에 익숙한 언어로 들리는것 뿐이지."
    pp "아..? 그럼 저기있는 저 동물이랑도 얘기할 수 있어요?"
    menu:
        "저기에 보이는 동물은.."

        "코끼리":
            scene hu_elephantcage
            show hu_elephant
            ph "뿌우"
        "뱀":
            scene hu_snakecage
            show hu_snake
            ph "스스스스슷"
        "호랑이":
            scene hu_tigercage
            show hu_tiger
            ph "크앙"
    pp "오.. 소통을 할땐 그렇게 변하는거야?"
    ph "아니?"
    hide hu_elephant
    hide hu_snake
    hide hu_tiger
    show hu_talking at left
    pp "..?"
    ph "이건 약간의...너를 위한 서비스 같은것이다! 짐의 귀여운 모습을 볼 수 있으니 말이지."
    pp "아...하.."
    ph "흠흠.."
    ph "이제 집에 가서 저녁이나 먹자꾸나"
    jump mk4


