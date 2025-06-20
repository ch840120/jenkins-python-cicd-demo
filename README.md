# 👨‍💻 jenkins-python-cicd-demo

一個簡易的 FastAPI Python 應用範例，搭配完整的 Jenkins CI/CD 流水線，可自動：

1. 🐳 建置 Docker 映像  
2. 📥 推送到本地 Registry (`localhost:5000`)  
3. 🚀 部署容器（埠號 9001）  
4. 🧹 清理舊版映像  

## 📁 專案結構
```
.
├── Dockerfile # 建置 FastAPI 應用映像
├── Jenkinsfile # Declarative Pipeline for CI/CD
├── app.py # FastAPI 應用程式
├── pyproject.toml # Poetry 依賴管理
├── requirements.txt # pip 依賴清單
├── .gitignore
├── README.md
└── jenkins_build/ # Jenkins 環境與本地 Registry 設定
├── Dockerfile # 自製 Jenkins image（含 docker.io）
└── docker-compose.yml # 啟動 Jenkins + Registry 的 Compose 檔
```
## 🏗 建置 Jenkins (jenkins_build)

在專案根目錄下有一個 `jenkins_build` 資料夾，裡面包含兩個檔案用來快速建置一個可跑 Docker 的 Jenkins 環境：
```
jenkins_build/
├── Dockerfile # 自訂 Jenkins image：基於 jenkins/jenkins:lts，安裝 docker.io 並將 jenkins 使用者加入 Docker 群組 (GID=1001)
└── docker-compose.yml # 同時啟動 Jenkins + 本地 Registry 的 Compose 檔，並掛載必要的 Volume、Docker socket、SSH key
```
### 🚀 使用步驟

```bash
1. 📂 切換到 `jenkins_build` 資料夾    
cd jenkins_build
2. 🏗️ 建置自訂 Jenkins 映像
docker-compose build
3. ▶️ 背景啟動 Jenkins 與本地 Registry
docker-compose up -d
```
- Jenkins Web UI： http://localhost:8080
- 本地 Registry API： http://localhost:5000

## 🔑 創建 Credentials
![image](https://github.com/user-attachments/assets/52230645-5ce7-4da2-a112-840800bcb299)

## 🛠️ 創建 Jenkins Job 並 Build
![image](https://github.com/user-attachments/assets/b1d31ade-2049-4b0c-9e3b-3da319ccd43c)
![image](https://github.com/user-attachments/assets/182eb7c4-3a57-4067-8b54-6f202c725f53)

## 🎉 成果圖
![image](https://github.com/user-attachments/assets/4bdcee02-5766-453b-b2ac-d89cf94a0998)

