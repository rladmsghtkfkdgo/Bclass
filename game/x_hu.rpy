# 휴 변수파일
# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
image hu_magic="hu_magic.png"
image hu_huntingmouse="hu_huntingmouse.png"
image hu_looking="hu_looking.png"
image hu_crying="hu_crying.png"
image hu_intro="hu_intro.png"
image hu_intro1="hu_intro1.png"
image hu_comein="hu_comein.png"
image hu_room="hu_room.png"
image hu_room2="hu_room2.png"
image hu_room3="hu_room3.png"
# 게임에서 사용할 캐릭터를 정의합니다.

#변수 표현은 "[변수]"
define e = Character('푸리', color="#c8ffc8")
define pp = Character('pname',dynamic =True, color="#402fd6")
define pname= "???"
define pl=0
define fade =Fade(0.5,0.0,0.5)
#변수 표현은 "[변수]"
init python:

    def hogamm(pl):
        if (pl>=50):
            return "휴"
        elif(pl<=20):
            return "마왕"
        else:
            return "르웨인 디카프리나 엘란트 휴"

default ph =Character(hogamm(pl), color="#d53366")
