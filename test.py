import datetime

def get_name():
    name = input("이름을 입력해주세요: ").strip()
    return name

def get_birthday():
    bday = input("생일을 입력해주세요 (MM-DD): ").strip()
    try:
        month, day = map(int, bday.split('-'))
        return (month, day)
    except ValueError:
        return None

def time_based_greeting():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "좋은 아침입니다"
    elif current_hour < 18:
        return "안녕하세요"
    else:
        return "좋은 저녁입니다"

def is_birthday_today(month, day):
    today = datetime.datetime.now()
    return today.month == month and today.day == day

def user_info(name):
    initial = name[0] if name else '?'
    length = len(name)
    return f"이름 길이: {length}, 첫 글자: '{initial}'"

def main():
    print("🎉 환영합니다! 인사 프로그램을 시작합니다 🎉\n")
    
    name = get_name()
    bday = get_birthday()

    print(f"\n{time_based_greeting()}, {name}님!")

    if bday and is_birthday_today(*bday):
        print("🎂 오늘이 생일이시네요! 진심으로 축하드려요! 🎉")
    
    print("📋 사용자 정보:")
    print(user_info(name))

if __name__ == "__main__":
    main()