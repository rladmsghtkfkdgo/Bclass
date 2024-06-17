# 이 파일에 게임 스크립트를 입력합니다.

# 여기에서부터 게임이 시작합니다.
label start:
    #play music "movie.ogg"
    #show 고양이캐릭터 영화 사자 그거마냥 움짤 되나 이거 확인해야하는디
    #유진언니 와압
    #hide 고양이캐릭터 영화 사자 그거마냥 움짤 되나 이거 확인해야하는디
    #with blinds
    
    #play music "opening.ogg"
    e "새로운 도전자냥?"
    #scene 모든캐릭터그림
    #hide 고양이캐릭터
    #show 고양이소개그림 at left
    e"이 게임은 카사노바프로젝트! 네가 어떻게 하냐에 따라 여러가지 엔딩을 만나 볼 수 있다냥."

    e "두가지 세계가 있다냥.\n잘 생각하고 결정해라냥!"

    menu first:
        #hide 고양이소개그림
        "너의 선택을 존중한다냥"
        "현대사회":
            jump world1
        "판타지사회":
            jump world2
            
        
    label world1:
        #scene room
        "으 머리야..."
        #폰이울리는 효과음

        menu sc1:
            "핸드폰 알림이 왔다. 어떤 알림이 왔는지 확인해보자."
            "유튜브 추천 방송":
                jump jn
            "산악 자전거 커뮤니티 추천":
                jump yj   

    label world2:
        with Pause(3.0)
        
        scene room2
        p "으 머리야..."

        p "여기가...판타지세계라고?"

        menu:
            "뭐...일단 밖에 나가볼까?":
                jump jw
            "집도 완전 좋아보이잖아..?집구경이나 해볼까?":
                jump mk1

    return
