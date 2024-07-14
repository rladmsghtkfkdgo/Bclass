#캐릭터
define ga = Character('알람', window_left_padding = 200, color="#e70000", image='ga')  #시스템

#인물
define gm = Character('박승철(당신)', color="#000c92", window_left_padding = 200, image='gm') #주인공
define gw = Character('이난희', color="#cc4dcc", window_left_padding = 200, image='gw')
#define gw = Character('이난희', color="#cc4dcc", image='gw')
define gf = Character('이진', color="#62234a", window_left_padding = 200, image='gf') # 주인공의 친구 
define gp1= Character('강찬(동아리 회장)', color="#9c90a5", window_left_padding = 200, image='gp1')
define gp2 = Character('수진(동아리 부원)', color="#9c90a5", window_left_padding = 200, image='gp2')
define gn= Character('이름 모르는 사람', color="#9c90a5")

 

#인물 이미지
#image gw_main_top = "character/gw_main.png"
#image gw_main_shy = "character/gw_main_shy.png"  #shy 이미지 
##image gn = ""
#image gf = "character/gf.png"
#image gp1 = "character/gp1.png"
#image gp2 = "character/gp2.png"

## gw
image gw_main_all = "character/gw/gw_main_all.png"
image gw_main_top = im.FactorScale("character/gw/gw_main_top.png", 0.7)
image gw_side = "character/gw/gw_side.png"
image gw_angry = im.FactorScale("character/gw/gw_경멸.png", 0.46)
image gw_wow = "character/gw/gw_놀람.png"
image gw_wow_all = "character/gw/gw_놀람_all.png"
image gw_trainng = im.FactorScale("character/gw/gw_traninng.png", 0.4)
#image gw_black = "character/gw/gw_main_black.png"

## tmp 이미지
image tmp = im.FactorScale("character/tmp.png", 0.34)
image tmp_back = "background/tmp_back.png"


image gw_main_all = im.FactorScale("character/gw/gw_main_all.png", 0.5)

image side gm = im.FactorScale("character/gm1.png", 0.7, 0.7) 
image side gw  = im.FactorScale("character/gw/gw_side.png", 0.74, 0.74)
image side gw happy = im.FactorScale("character/gw/gw_side_happy.png", 0.74, 0.74)
image side gw angry  = im.FactorScale("character/gw/gw_side_angry.png", 0.74, 0.74)
#image side gw  = im.FactorScale("character/gw/gw_side.png", 0.74, 0.74)
image side gw shy = im.FactorScale("character/gw/gw_main_shy2.png", 0.74, 0.74)
image side gw shy2 = im.FactorScale("character/gw/gw_side_shy.png", 0.74, 0.74)
image side gf  = im.FactorScale("character/gf.png", 0.7, 0.7)
image side gp1 = im.FactorScale("character/gp1.png", 0.44, 0.44)
image side gp2 = im.FactorScale("character/gp2.png", 0.4, 0.4)
image side ga = im.FactorScale("character/bell.png", 0.6, 0.6)


#음식 
## d4
image gdiner_jju = im.FactorScale("food/쭈꾸미볶음.png", 1.5)   #쭈꾸미
image gdiner_hawai = im.FactorScale("food/하와이안 피자.png", 1.4) # 하와이안 피자
image gdiner_mara = im.FactorScale("food/마라탕.png", 1.4)  # 마라
image gdiner_ttok = im.FactorScale("food/떡볶이.png", 1.4)  # 떡볶이 

## d8
image grice =im.FactorScale("food/김치볶음밥.png", 1.0)
image gsandwitch =im.FactorScale("food/샌드위치.png", 1.0)
image gsandwitch2 ="food/샌드위치.jpg"
image gkimbab =im.FactorScale("food/김밥.png", 1.0)
image gzzanmbbong =im.FactorScale("food/불향 가득 짬뽕밥.png", 1.0)

#편의점 음료
image gdan ="food/단백질쉐이크.png"
image goak = im.FactorScale("food/옥수수 수염차.png", 1.5)
image gcoff =im.FactorScale("food/달달한 커피.png", 1.2)
image gmang =im.FactorScale("food/신상 고농축 망고 주스.png", 1.5)


# 배경 이미지
#image test = color="#000000"

## 학교 관련
image gdong =im.FactorScale("background/대중.jpg", 1.2)

image gclassroom1 =im.FactorScale("background/교실1.jpg", 1.2 )
image gclassroom2 =im.FactorScale("background/교실2.jpg", 0.4)
image gstudent1 =im.FactorScale("background/고등학생들1.png", 0.75)
image gstudent2 =im.FactorScale("background/고등학생들2.png", 0.75)
image gschool_morning = im.FactorScale("background/아침학교.png", 1.34)

#image gstreet1 = ""
#image gstreet2 ="background/길거리2.jpg"

## 일상 관련 
image groom ="background/방1.png"
image gblack = "background/검정.png"   #화면 전환시 사용
image gpark =im.FactorScale("background/공원.png", 1.5 )
image gpark_night =im.FactorScale("background/공원_밤.png", 1.5 )
image gride_bike = im.FactorScale("background/자전거배우기.png", 0.75)
image gm_ride_bike1 = im.FactorScale("background/자전거타는남주1.png", 5.0)
image gm_ride_bike2 = im.FactorScale("background/자전거타는남주2.png", 2.0) #height=1920, width=1020
image gm_ride_bike3 = im.FactorScale("background/자전거타는남주3.png", 1.45)
image gmarket = im.FactorScale("background/음료냉장고.png", 1.5)
image gstreet =im.FactorScale("background/길거리.png", 1.45)
image gbike = im.FactorScale("background/자전거.png", 0.8)
image gforest = "background/산속.jpg"

#image gpark_biy ="background/자전거와 공원.jpg"
#image gpark_biy2 ="background/자전거와 공원2.jpg"
#image ghangang =im.FactorScale("background/한강자전거길.jpg", 0.2)
#image gbeach ="background/해변자전거길.jpg"


#파이썬 변수
init python:
    hogam = 0;     #호감
    gday_count = 0;

    str_question ="오늘 운동을 갈까요?"

screen hello_world():
    tag example
    zorder 1
    modal False
    text "Hello, World."


#문법
#$ renpy.notify('test') --> 왼쪽 상단에 작게 알림 띄우기
 