# Azure OpenAI 串流聊天範例

這是一個使用 Python 與 Azure OpenAI 的簡易命令列範例。程式會傳送預設的對話訊息，並以串流方式逐字顯示模型回覆。

## 需求

- 已安裝 Python
- 可使用的 Azure OpenAI 資源
- 已在該資源部署模型，並取得資源端點與 API 金鑰

## 安裝

在專案目錄中建立並啟用虛擬環境：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

安裝專案依賴：

```powershell
python -m pip install -r requirements.txt
```

## 設定

編輯 [main.py](./main.py)，將 `AzureOpenAI` 客戶端設定中的範例值換成自己的 Azure OpenAI 資訊：

- `azure_endpoint`：Azure OpenAI 資源端點
- `api_key`：該資源的 API 金鑰
- `model`：Azure OpenAI 中已部署的模型名稱（部署名稱）

請勿將真實 API 金鑰提交至版本控制或公開分享。

## 執行

```powershell
python main.py
```

程式會在終端機顯示串流回覆。要修改提問內容，可編輯 `main.py` 中的 `messages`。

## 專案檔案

- `main.py`：建立 Azure OpenAI 客戶端、送出對話並輸出串流回覆
- `requirements.txt`：Python 套件依賴
