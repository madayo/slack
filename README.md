# slack
slack関連のファイルいろいろ

## 環境設定  
`token`など環境に依存する情報はすべて`.env`に外出ししている。  
  
- `.env`
    - SLACK_API_TOKEN  
    [URL](https://api.slack.com/custom-integrations/legacy-tokens)で確認できた値を設定する。  
    - USER_ID  
    [URL](https://api.slack.com/methods/users.profile.get/test)の中段くらいにある、@foo 部分をクリックすると`USER`の値が textbox に反映されるのでその値を設定する。　　
    ```
    user Optional {textbox} @foo
    ```
