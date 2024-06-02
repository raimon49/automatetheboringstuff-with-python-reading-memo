#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8 ff=unix ft=python ts=4 sw=4 sts=4 si et

def main():
    import pyautogui, time

    name_field = (648, 319)
    submit_button = (651, 817)
    submit_button_color = (75, 141, 249)
    submit_anoter_link = (760, 224)

    form_data = [{'name': 'Alice', 'fear': 'eavedroppers', 'source': 'wand',
                  'robocop': 4, 'comments': 'Tell Bob I said hi>'},
                 {'name': 'Bob', 'fear': 'beers', 'source': 'amulet',
                  'robocop': 4, 'comments': 'N/A'},
                 {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
                  'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
                 ]

    pyautogui.PAUSE = 0.5

    for person in form_data:
        # ユーザーがスクリプトを中断する機会を与える
        print('>>> 5秒間、一時停止中。中断するにはCtrl-Cを推してください。<<<')
        time.sleep(5)

        # フォームページが読み込まれるのを待つ
        while not pyautogui.pixelMatchesColor(submit_button[0], submit_button[1], submit_button_color):
            time.sleep(5)

        print('{}の情報を入力中...'.format(person['name']))
        pyautogui.click(name_field[0], name_field[1])

        # Name欄を入力する
        pyautogui.typewrite(person['name'] + '\t')

        # Greatest Fear(s)欄を入力する
        pyautogui.typewrite(person['fear'] + '\t')

        # Source of Wizard Poewers欄を選択する
        if person['source'] == 'wand':
            pyautogui.typewrite(['down', '\t'])
        elif person['source'] == 'amulet':
            pyautogui.typewrite(['down', 'down', '\t'])
        elif person['source'] == 'crystal ball':
            pyautogui.typewrite(['down', 'down', 'down', '\t'])
        elif person['source'] == 'money':
            pyautogui.typewrite(['down', 'down', 'down', 'down', '\t'])


        if person['robocop'] == 1:
            pyautogui.typewrite([' ', '\t'])
        elif person['robocop'] == 2:
            pyautogui.typewrite(['right', '\t'])
        elif person['robocop'] == 3:
            pyautogui.typewrite(['right', 'right', '\t'])
        elif person['robocop'] == 4:
            pyautogui.typewrite(['right', 'right', 'right', '\t'])

    # TODO: RoboCop欄を選択する

    # TODO: Additional Comments欄を入力する

    # TODO: Submitをクリックする

    # TODO: 次のページが読み込まれるのを待つ

    # TODO: Submit another responseリンクをクリックする


if __name__ == '__main__':
    main()
