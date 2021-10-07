
このスクリプトは以下のライブラリを使用します。

PyCryptodome

pysha3

pyminizip

pyinstaller

pyperclip

*********

pyinstallerを除く上記すべてのライブラリはスクリプトの実行に必須となっています。

実行ファイルにする場合、上記ライブラリをインストール後「compile.bat」を実行してください。

packディレクトリ内のkey.pyを書き換えると書換前のVailDECで暗号化したデータを復号化することができなくなり、
書き換えたVailDECで暗号化したデータはその暗号化を実行したVailDEC本体でないと復号化はできません。