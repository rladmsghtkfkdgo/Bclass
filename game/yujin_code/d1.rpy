# 동아리 홍보회
# 이미지 조절하기

label d1_first:
    scene crownd
    friend "야! 너 어디 가입할거야!"
    friend "난 농구부 가입할랜다. 역시 남자는 농구지. "
    p "저희 동아리 들어와요! 분위기 좋아요!"
    p "저희 동아리 들어와요! 분위기 더 더 더 좋아요!"
    p "저희 동아리 들어와요! 학교 지원금 빵빵 합니다!"
    
    m "뭐야.. 저 근육은?"
    m "산악회 재밌겠는데? 저기로 결정했다."
    sys "당신은 산악회에 가입했습니다."


label d1:
    scene classroom1
    p "자! 저희 산악자전거 동아리에 가입해주셔서 감사합니다."
    m "뭐?!?!?!?!??"
    m "산악.. 자전거??????????????!!!!!!!!!!!!!!"
    m "나 자전거 탈 줄 몰라 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 어떡하지..? 나가?"
    m "아 몰라 ! 여기서 배워! 어차피 맘에 드는 동아리 없었잖아. "
    #show image = "산악자전거 동아리 규칙과 운영방식"
    
    p "그러면 조 추첨을 진행할게요!"
    m "3조라.. 아 그때 그 사람은 몇 조일까.. 같은 조였으면 좋겠다. "
    #show image ="모여있는 사람들"
    m "역시 같은 조는 아니군. "
    m "저 사람한테 물어볼까..? 자전거 알려달라고 할까? "
    menu:
        "알려달라고 한다. ":
            m "그래 이러면서 친해지는 거지."
        "다른 사람에게 알려달라고 한다. ":
            m  "이러면서 친해지는 거지. 물어보자."
    sys "당신은 ???에게 말을 걸기로 결심했다. "

    m "저ㄱ ㅣ 욥 ..!"
    m "이름이 뭔가요. 몇 살이세요? 친해지고 싶어요."

    show main_w_top
    w "..........."
    w "???입니다..2학년.."
    m "오 ! 굉장히 이쁜이름. 말 편하게 할래요? 좋아요. 동갑이니까 편하게 부를게잉"
    m "???아 혹시 나 자전거 알려줄 수 있어 ?? 내가 산악자전거는 처음이라..."
    w "'확실히 산악 자전거는 접하기 어렵긴 해. 나도 선배한테 배웠으니까..'"
    w "아랐숴잉~ 알려줄게. "
    m "어! 고마워 !!!!!!! 아리갓또네 !!! 혼또니 !!! "

    jump d2_만나기_전
    jump d2_공원
    jump d2_저녁
    jump d2_집