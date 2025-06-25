# J-QuantsApiAutorization
J-Quants APIから、IDトークンを取得するクライアント処理

## 使い方

### IDトークンの取得
- IDトークンの取得のため、以下の環境変数を事前に定義すること
    - JQUANTS_EMAIL
        - J-Quants APIアカウントのメールアドレス
    - JQUANTS_PASSWORD
        - J-Quants APIアカウントのパスワード

``` python
from j_quants_auth import JQuantsAuthorization
# メールアドレスとパスワードから、IDトークンを取得
j_quants_authorization = JQuantsAuthorization()
id_token = j_quants_authorization.id_token
```

## ユニットテスト
プロジェクトのルートディレクトリ（srcやtestsの親ディレクトリ）で下記を実行
```
PYTHONPATH=./src python3 -m unittest tests
```

