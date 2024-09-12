# 게임에서 사용할 캐릭터를 정의합니다.
define jw = Character('플레이어', color="#344e90")
define jd = Character('옆집사람', color="#cf9dcf")
define js = Character('서서윤', color="#cf9dcf")
define jq = Character()
define jplayer_name = "플레이어"
define jp = Character("jplayer_name",dynamic = True, color="#344e90")
define jhh = Character('헬스 트레이너', color="#0f4d6d")
define jco = Character('편의점 점원', color="#453709")
define jg = Character('경찰', color="#1c1c4a")
define jg1 = Character('경찰1', color="#22226e")
define jg2 = Character('경찰2', color="#15152e")
define fade = Fade(0.5,0.0,0.5)

image bg j_room1 = "j_room1.jpg" #거실
image bg j_room01 = "j_room01.png" #거실 어두운
image bg j_room02 = "j_room02.png" #거실 더 어두운
image bg j_room03 = "j_room03.png" #거실 까만
image bg j_room_bo = "j_room_bo.png" #아파트 복도
image bg j_room_bo1 = "j_room_bo1.png" #뿌얀 아파트 복도 
image bg j_room_bo2 = "j_room_bo2.png" #폴리스 아파트 복도
image bg j_room_bo3 = "j_room_bo3.png" #어두운 폴리스 아파트 복도
image bg j_room_h = "j_room_h.png" #헬스장
image bg j_room_k = "j_room_k.png" #부엌
image bg j_room_na = "j_room_na.png" #냉장고
image bg j_room_co = "j_room_co.png" #편의점
image bg j_room_co2 = "j_room_co2.png" #편의점 벤치
image bg j_room_ca1 = "j_room_ca1.png" #고양이 담벼락
image bg j_room_ca2 = "j_room_ca2.png" #고양이 담벼락 없이
image bg j_room_caca = "j_room_caca.png" #고양이 카페
image bg j_room_sa = "j_room_sa.png" #산책로
image bg j_room_sand = "j_room_san.png" #샌드위치 가게
image bg j_room_we = "j_room_we.png" #웨딩 드레스
image bg j_room_ser = "j_room_ser.png" #설거지 그릇
image bg j_room_en = "j_room_en.png" #엔딩 카페
image bg j_white = "j_white.png"

image bg j_end_01 = "j_end_01.png"
image bg j_end_02 = "j_end_02.png"
image bg j_end_03 = "j_end_03.png"
image bg j_end_04 = "j_end_04.png"
image bg j_end_05 = "j_end_05.png"

image bg j_ending_03 = "j_ending_03.png"
image bg j_ending_04 = "j_ending_04.png"
image bg j_ending_05 = "j_ending_05.png"

image bg j_trash = "j_trash.png" #쓰레기

image j_food_pa = "j_food_pa.png" #파스타
image j_food_so = "j_food_so.png" #스프
image j_food_dak = "j_food_dak.png" #닭가슴살
image j_food_papa = "j_food_papa.png" #파스타2

image j_labe_2 = "j_labe_2.png" #2시간 후
image j_labe_3 = "j_labe_3.png" #3시간 후
image j_labe_za = "j_labe_za.png" #잠시 후
image j_labe_da = "j_labe_da.png" #다음날 아침
image j_labe_ge = "j_labe_ge.png" #몇 개월 후
image j_labe_zu = "j_labe_zu.png" #한가로운 주말 아침
image j_labe_me = "j_labe_me.png" #며칠 뒤

image j_mes_1 = "j_mes_1.png" #메시지
image j_mes_2 = "j_mes_2.png" #메시지 Yes
image j_mes_ti = "j_mes_ti.png" #메시지 띠링

image j_hand = "j_hand_b.png" #핸드폰 검은 화면
image j_hand_t = "j_hand.png" #핸드폰 빈 화면
image j_hand_u = "j_hand_u.png" #유튜브 시작 화면
image j_hand_sf = "j_hand_sf.png" #유튜브 쇼츠 욕 화면
image j_hand_df = "j_hand_df.png" #유튜브 영상 욕 화면
image j_alm = "j_utb_1.png" #유튜브 알람
image j_upi_1 = "j_upi_1.png" #유피아 쇼츠
image j_su1 = "j_su1.png" #무표정
image j_su2 = "j_su2.png" #미소
image j_su3 = "j_su3.png" #웃음
image j_su4 = "j_su4.png" #놀람
image j_su5 = "j_su7.png" #곤란
image j_su6 = "j_su8.png" #곤란&빗금
image j_su7 = "j_su5.png" #곤란 입
image j_su8 = "j_su6.png" #곤란&빗금 입

image j_dream_su = "j_dream_su.png" #서윤 꿈
image j_dream_ca = "j_dream_ca.png" #고양이 꿈

image j_hh_1 = "j_hh_1.png" #헬스 트레이너
image j_co_1 = "j_co_1.png" #편의점 점원
image j_pol = "j_pol.png" #경찰


define ju = 0 #호감도