#python -m pip install flet

import random
import flet as ft

def main(page: ft.Page):
    page.title = "업다운 게임"
    page.window_width = 400
    page.window_height = 500
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    answer = random.randint(1, 100)
    attempts = 0

    title = ft.Text("업다운 게임", size=28, weight=ft.FontWeight.BOLD)
    guide = ft.Text("1부터 100 사이 숫자를 맞혀보세요!", size=16)
    result_text = ft.Text("", size=18, weight=ft.FontWeight.BOLD)
    attempt_text = ft.Text("시도 횟수: 0", size=14)

    input_box = ft.TextField(
        label="숫자 입력",
        width=200,
        keyboard_type=ft.KeyboardType.NUMBER,
        text_align=ft.TextAlign.CENTER,
    )

    def check_number(e):
        nonlocal answer, attempts

        if not input_box.value:
            result_text.value = "숫자를 입력하세요."
            page.update()
            return

        try:
            user_num = int(input_box.value)
        except ValueError:
            result_text.value = "정수를 입력하세요."
            input_box.value = ""
            page.update()
            return

        if not (1 <= user_num <= 100):
            result_text.value = "1~100 사이 숫자만 입력하세요."
            input_box.value = ""
            page.update()
            return

        attempts += 1
        attempt_text.value = f"시도 횟수: {attempts}"

        if user_num < answer:
            result_text.value = "UP! 더 큰 숫자입니다."
        elif user_num > answer:
            result_text.value = "DOWN! 더 작은 숫자입니다."
        else:
            result_text.value = f"정답! 🎉 {attempts}번 만에 맞췄어요."

        input_box.value = ""
        page.update()

    def reset_game(e):
        nonlocal answer, attempts
        answer = random.randint(1, 100)
        attempts = 0
        input_box.value = ""
        result_text.value = "새 게임이 시작되었습니다!"
        attempt_text.value = "시도 횟수: 0"
        page.update()

    input_box.on_submit = check_number

    page.add(
        title,
        guide,
        input_box,
        ft.Row(
            [
                ft.ElevatedButton("확인", on_click=check_number),
                ft.OutlinedButton("다시 시작", on_click=reset_game),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        result_text,
        attempt_text,
    )

ft.run(main)