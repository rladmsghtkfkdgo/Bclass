label j_cv:
    show j_labe_zu
    " "
    hide j_labe_zu
    menu:
        "밖에 나가볼까?":
            jump j_vb
        "집이 최고지 집에 있자":
            jump j_bn
    label j_vb:
        "나가는김에 과자나 사러가야겠다."
        "고양이 있으려나?"
        "혹시 모르니 츄르도 가져가야지"
        show bg j_room_ca
    