# 휴 변수파일
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