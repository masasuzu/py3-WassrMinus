===============================
WassrMinus for Python3000
===============================

What's this
-------------------------------

WassrMinus is poor Wassr clie...(ry

Python Hack-a-thonでネタで作ったモジュールです。
ホントは、setup.pyとかちゃんと整備してかっくいく作るつもりだったんですが、
文字コードの問題とか、Pythonの文法自体を忘れかけていたので、この様です。

Windows環境だとコンソールにprintする時に問題があるかも知れません。

How to use
-------------------------------

:
    import wassr_minus

    wassr = wassr_minus.WassrMinus(user='USER', password='PASS')
    wassr.update('comment')

    json_obj = wassr.public_timeline()
    json_obj = wassr.friends_timeline()
    json_obj = wassr.replies()
    json_obj = wassr.user_timeline()   # or  wassr.user_timeline(id='USER')
    json_obj = wassr.show()            # or  wassr.show(id='USER')

    for status in json_obj:
        print(status['login_user_id'])
        print(status['html'])