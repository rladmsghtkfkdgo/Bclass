# 8일차 부터



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


image side gm = im.FactorScale("character/gm.png", 0.4, 0.4) 
image side gw  = im.FactorScale("character/gw_main.png", 0.74, 0.74)
image side gw shy = "character/gw_main_shy.png" 
image side gf  = im.FactorScale("character/gf.png", 0.7, 0.7)
image side gp1 = im.FactorScale("character/gp1.png", 0.44, 0.44)
image side gp2 = im.FactorScale("character/gp2.png", 0.4, 0.4)
image side ga = im.FactorScale("character/bell.png", 0.6, 0.6)


#음식 
image gdiner_jju = "food/쭈꾸미.png"   #쭈꾸미
image gdiner_hawai = "food/하와이안 피자.png" # 하와이안 피자
#image gdiner_mara = "food/"  # 마라
image gdiner_ttok = "food/떡볶이.png"  # 떡볶이 
image grice ="background/김치볶음밥.jpg"
image gsandwitch ="background/샌드위치.jpg"
image gkimbab ="background/오이김밥.jfif"


# 배경 이미지
#image test = color="#000000"
image gdong =im.FactorScale("background/대중.jpg", 1.2)
image gpark =im.FactorScale("background/공원.png", 1.5 )
image gclassroom1 =im.FactorScale("background/교실1.jpg", 1.2 )
image gclassroom2 =im.FactorScale("background/교실2.jpg", 0.4)
image gstreet1 =im.FactorScale("background/고등학생들2.png", 0.75)
image gstreet2 ="background/길거리2.jpg"
image gcrownd ="background/대중.jpg"
image groom ="background/방1.png"
image gpark_biy ="background/자전거와 공원.jpg"
image gpark_biy2 ="background/자전거와 공원2.jpg"
image gdark_park ="background/자전거와 공원2_어두워.jpg"
#image ghangang =im.FactorScale("background/한강자전거길.jpg", 0.2)
#image gbeach ="background/해변자전거길.jpg"
image gd1_festival ="background/d1_축제이미지.jpg"
image gblack = "background/검정.png"   #화면 전환시 사용
image gride_bike = im.FactorScale("background/자전거배우기.png", 0.75)
image gm_ride_bike1 = im.FactorScale("background/자전거타는남주1.png", 10.0)
image gm_ride_bike2 = im.FactorScale("background/자전거타는남주2.png", 2.0) #height=1920, width=1020
image gschool_morning = im.FactorScale("background/등교.png", 1.34)
#image g = "background/"
#image g = "background/"


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
