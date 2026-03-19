#python -m pip install flet
#python python\UpDaownGame_GUI.py
import random
import flet as ft

def main(page = ft.Page):
    page.title = "업다운 게임"

    answer = random.randint(1, 100)
    count = 0

    title = ft.Text("업다운 게임", size=30)
    guide = ft.Text("1부터 100 사이 숫자를 입력하세요")
    result = ft.Text("")
    count_text = ft.Text("시도 횟수: 0")

    input_box = ft.TextField(label="숫자 입력", width=200)

    def check_number(e):
        nonlocal count

        user_number = int(input_box.value)
        count += 1
        count_text.value = "시도 횟수: " + str(count)

        if user_number < answer:
            result.value = "UP"
        elif user_number > answer:
            result.value = "DOWN"
        else:
            result.value = "정답!"

        input_box.value = ""
        page.update()

    page.add(
        title,
        guide,
        input_box,
        ft.ElevatedButton("확인", on_click=check_number),
        result,
        count_text
    )

ft.run(main)