# J-QuantsApiAutorization
J-Quants APIから、IDトークンを取得するクライアント処理

## 使い方

### IDトークンの取得
``` python
from j_quants_auth import JQuantsAuthorization
# メールアドレスとパスワードから、IDトークンを取得
j_quants_authorization = JQuantsAuthorization(
  mail_address='your mail address',
  password='your password',
)
id_token = j_quants_authorization.get_id_token()

# 一度取得したIDトークンは、id_tokenから取得可能
j_quants_authorization.id_token
```
