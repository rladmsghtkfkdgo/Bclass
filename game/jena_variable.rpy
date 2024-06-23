# 게임에서 사용할 캐릭터를 정의합니다.
define jw = Character('플레이어', color="#9fbaff")
define jd = Character('옆집사람', color="#cf9dcf")
define js = Character('서서윤', color="#cf9dcf")
define jq = Character()
define jplayer_name = "플레이어이름"
define jp = Character("jplayer_name",dynamic = True, color="#9fbaff")
define jhh = Character('헬스 트레이너', color="#9fdfff")
define jco = Character('편의점 점원', color="#ede8ab")
define fade = Fade(0.5,0.0,0.5)

image bg j_room1 = "j_room1.jpg" #거실
image bg j_room_bo = "j_room_bo.png" #아파트 복도
image bg j_room_h = "j_room_h.png" #헬스장
image bg j_room_k = "j_room_k.png" #부엌
image bg j_room_co = "j_room_co.png" #편의점
image bg j_room_co2 = "j_room_co2.png" #편의점 벤치
image bg j_room_ca1 = "j_room_ca1.png" #고양이 담벼락
image bg j_room_ca2 = "j_room_ca2.png" #고양이 담벼락 없이
image bg j_room_caca = "j_room_caca.png" #고양이 카페
image bg j_room_sa = "j_room_sa.png" #산책로
image bg j_room_sand = "j_room_san.png" #산책로
image bg j_zero = "j_zero.png"

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

image j_hand = "j_hand1.png" #핸드폰&손
image j_alm = "j_utb_1.png" #유튜브 알람
image j_utb = "j_utb_2.png" #유튜브 시작화면
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


define ju = 0 #호감도