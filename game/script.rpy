# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image hu_magic="hu_magic.png"
image hu_huntingmouse="hu_huntingmouse.png"
image hu_looking="hu_looking.png"
image hu_intro="hu_intro.png"
image hu_intro1="hu_intro1.png"
image hu_comein="hu_comein.png"
image room="room.png"
image room2="room2.png"
image room3="room3.png"
# 게임에서 사용할 캐릭터를 정의합니다.

define e = Character('푸리', color="#c8ffc8")
define p = Character('name',dynamic =True, color="#402fd6")
define name= "???"
define l=0
#변수 표현은 "[변수]"
init python:

    def hogamm(l):
        if (l>=50):
            return "휴"
        elif(l<=20):
            return "마왕"
        else:
            return "르웨인 디카프리나 엘란트 휴"

default h =Character(hogamm(l), color="#d53366")
#$h=Character(hogam(l), color="#d53366")
# 여기에서부터 게임이 시작합니다.
label start:
    #show 고양이캐릭터
    e "새로운 도전자냥?"
    #scene 모든캐릭터그림
    #hide 고양이캐릭터
    #show 고양이소개그림
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
            
    label jn:
        "제나"

    label yj:
        "유진"   

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

    label jw:
        "지우"   
        

    return
