# 휴 변수파일
# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"
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
