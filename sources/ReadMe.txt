
このスクリプトは以下のライブラリを使用します。

PyCryptodome　https://www.pycryptodome.org/en/latest

pysha3　- https://github.com/tiran/pysha3

pyminizip - https://github.com/smihica/pyminizip

pyinstaller - http://www.pyinstaller.org/

pyperclip - https://github.com/asweigart/pyperclip

*********
上記の他に必要なライブラリがある場合があります。
(また、このリポジトリのMITライセンスはVailDEC.py本体のみに適応しライブラリ
pyinstallerを除く上記すべてのライブラリはスクリプトの実行に必須となっています。

実行ファイルにする場合、上記ライブラリをインストール後「compile.bat」を実行してください。

packディレクトリ内のkey.pyを書き換えると書換前のVailDECで暗号化したデータを復号化することができなくなり、
書き換えたVailDECで暗号化したデータはその暗号化を実行したVailDEC本体でないと復号化はできません。

key.py テンプレート
key1={"key1":"2225040938076260","key2":"x38fK9e4ckTIMzXb"}

(上記テンプレートを使用してpackディレクトリ内にkey.pyを作成してください)

