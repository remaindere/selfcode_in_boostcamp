def myFunction2 (texts) : 
    hangul = "공영일이삼사오육칠팔구"
    num = '00123456789'
    phone_num_list = []
    for text in texts :
        word_list = text.split()
        last_word = word_list[-1]
        if last_word.find("공") != -1 :
            num_word = last_word[:-4]
            #print(num_word)
            phone_num = []
            for ch_num in num_word :
                phone_num.append(num[hangul.find(ch_num)])
            phone_num_list.append("".join(phone_num))
    #print(phone_num_list)
    # 저장된 전화번호 리스트를 리턴
    return phone_num_list
