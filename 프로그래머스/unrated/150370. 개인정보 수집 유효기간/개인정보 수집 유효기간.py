def solution(today, terms, privacies):
    answer = []
    def get_days(date):
        today_num = 0
        year, month, day = 0,0,0
        year,month,day = date.split(".")
        today_num += int(year) * 12 * 28
        today_num += int(month) * 28
        today_num += int(day)

        return today_num
    
    
    terms_dict = {}

    for i in terms:
        term_type, term_dur = i.split(" ")
        terms_dict[term_type] = term_dur

    today_days = get_days(today)
    for num, priv in enumerate(privacies):
        priv_date, priv_type = priv.split(" ")
        expire = get_days(priv_date) + (int(terms_dict[priv_type])*28)
        if today_days >= expire:
            answer.append(num+1)
    
    return answer