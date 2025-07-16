def get_name(prompt="이름을 입력해주세요: "):
    return input(prompt).strip()

def greet_user(name):
    print(f"\n✨ 반갑습니다, {name}님! 오늘도 좋은 하루 되세요! ✨")

def main():
    print("🌟 Welcome to the Greeting Program 🌟")
    name = get_name()
    if name:
        greet_user(name)
    else:
        print("\n😅 이름이 입력되지 않았어요. 다음엔 꼭 알려주세요!")

if __name__ == "__main__":
    main()