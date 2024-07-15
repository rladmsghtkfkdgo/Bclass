

# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"


# 여기에서부터 게임이 시작합니다.
# 프롤로그 
label yj:
   
    label alert:
        $ renpy.notify('시작입니다! \n즐거운 시간되세요.')
        ga "[gf]님이 메세지를 보냈습니다. "
        #show image = "카톡 이미지.png"

        gm main "아 맞다! 내일 동아리 홍보제구나. 어디 가입하지?"
        gm main ".. 모르겠다 ~ 내일 구경해보고 결정하자 ~ "


        #$ renpy.call_screen("popup", str="이봐 친구!!! 동아리 어디 가입할거야!!!")
        screen hello_world():
            tag example
            zorder 1
            modal False
            text "Hello, World."

        #$ renpy.call_screen("hello_world")

    #==========================================================
    # Day 1
    jump d1_1
    

    
