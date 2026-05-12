# 快速开始指南

## ⚠️ 前置条件

**此 skill 需要 RAGFlow 服务才能使用。**

- ✅ **已有 RAGFlow**：联系管理员获取 API Key 和 Chat ID
- ❌ **没有 RAGFlow**：请先阅读 [RAGFLOW_SETUP.md](RAGFLOW_SETUP.md) 进行配置

## 5 分钟快速上手

### 步骤 1: 安装依赖

```bash
pip install -r requirements.txt
```

### 步骤 2: 配置环境变量

**推荐使用配置向导（最简单）：**

```bash
python setup_config.py
```

按照向导提示输入：
1. RAGFlow API URL
2. API Key（会隐藏显示）
3. Chat ID

向导会自动测试连接并保存配置。

---

**或者手动配置：**

**Windows (PowerShell):**
```powershell
copy .env.example .env
notepad .env
```

**Linux/Mac:**
```bash
cp .env.example .env
nano .env
```

编辑 `.env` 文件，填入你的实际配置：
```env
RAGFLOW_API_URL=https://79gb288606hs.vicp.fun
RAGFLOW_API_KEY=你的实际API密钥
RAGFLOW_CHAT_ID=e4f3a7de397911f1ab5cc5a32a377c21
```

### 步骤 3: 测试运行

```bash
python query_tax.py "最新的增值税优惠政策是什么？"
```

如果看到返回的答案，说明配置成功！✅

## 常见问题

### Q: 如何获取 RAGFLOW_API_KEY？
A: 登录 RAGFlow 后台，在设置或 API 管理页面找到你的 API Key。

### Q: 如何获取 RAGFLOW_CHAT_ID？
A: 在 RAGFlow 中创建对话助手后，助手的 ID 就是 CHAT_ID。

### Q: 提示 "ModuleNotFoundError"？
A: 运行 `pip install -r requirements.txt` 安装依赖。

### Q: 提示 "请配置环境变量"？
A: 确保 `.env` 文件存在且配置正确，或者在系统中设置环境变量。

## 下一步

- 查看 [README.md](README.md) 了解详细功能
- 查看 [SKILL.md](SKILL.md) 了解技能使用说明
- 在 OpenClaw 中安装并使用此 skill

## 需要帮助？

如遇问题，请检查：
1. 网络连接是否正常
2. RAGFlow 服务是否可访问
3. 环境变量配置是否正确
4. 查看错误信息并参考 README.md 的故障排除部分
