#캐릭터
define ga = Character('알람', color="#e70000")
#define gsys = Character('시스템', color="#273fdc")

define gm = Character('박승철(당신)', color="#000c92") #주인공
define  gw = Character('이난희', color="#cc4dcc", image='w_p')
define gf = Character('이진', color="#62234a") # 주인공의 친구 
define gp1= Character('종찬(동아리 회장)', color="#9c90a5")
define gp2 = Character('찬우(동아리 부원)', color="#9c90a5")
define gn= Character('이름 모르는 사람', color="#9c90a5")


image gw_p = "character/main_w_top.png"
#샤이 이미지 추가 
#image gw_shy = "character/main_w_top.png"


# 배경 이미지
image gdong =("background/d1_축제이미지.jpg")
image gpark =("background/공원_길거리.jpg")
image gclassroom1 ="background/교실1.jpg"
image gclassroom2 ="background/교실2.jpg"
image gstreet1 ="background/길거리1.jpg"
image gstreet2 ="background/길거리2.jpg"
image grice ="background/김치볶음밥.jpg"
image gcrownd ="background/대중.jpg"
image groom ="background/방 사진.jpg"
image gsandwitch ="background/샌드위치.jpg"
image gkimbab ="background/오이김밥.jfif"
image gpark_biy ="background/자전거와 공원.jpg"
image gpark_biy2 ="background/자전거와 공원2.jpg"
image gdark_park ="background/자전거와 공원2_어두워.jpg"
image ghangang ="background/한강자전거길.jpg"
image gbeach ="background/해변자전거길.jpg"
image gd1_festival ="background/d1_축제이미지.jpg"
image gblack = im.FactorScale("background/검정.png", 15.0)   #화면 전환시 사용
image gride_bike = "background/자전거배우기.png"
image gm_ride_bike1 = im.FactorScale("background/자전거타는남주1.png", 10.0)
image gm_ride_bike2 = im.FactorScale("background/자전거타는남주2.png", 2.0) #height=1920, width=1020
#image g = "background/"
#image g = "background/"
#image g = "background/"


init python:
    hogam = 0;     #호감
    gday_count = 0;

    str_question ="오늘 운동을 갈까요?"
