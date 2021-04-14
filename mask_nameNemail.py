def myFunction (texts) : 
    new_texts = []
    for text in texts :
        new_text_list = []
        words = text.split()
        name = words[1]
        masked_name = name[0] + "*" + "*"
        #print(words)
        email = words[3]
        id = email[:email.find('@')]
        ch_list = []
        ch_list.append(id[0])
        for i in range(len(id)-1) :
            ch_list.append('*')
        masked_id = "".join(ch_list)
        masked_email = masked_id + email[email.find('@'):]
        new_text_list.append(words[0])
        new_text_list.append(masked_name)
        new_text_list.append(words[2])
        new_text_list.append(masked_email)
        new_text = " ".join(new_text_list)
        new_texts.append(new_text)
    
    return new_texts
