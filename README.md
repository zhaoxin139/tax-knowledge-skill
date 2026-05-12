# TAX Knowledge Skill

基于 RAGFlow 的税务知识智能问答技能。

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 获取 RAGFlow 配置

联系你的 RAGFlow 管理员获取以下信息：

| 配置项 | 说明 | 获取方式 |
|--------|------|----------|
| **API URL** | RAGFlow 服务地址 | 询问管理员服务器地址 |
| **API Key** | API 访问密钥 | 登录 RAGFlow → 右上角头像 → API Keys → Create New Key |
| **Chat ID** | 对话助手 ID | 登录 RAGFlow → Chat 页面 → 查看助手详情 |

### 3. 配置环境变量

复制配置模板：

```bash
cp .env.example .env
```

编辑 `.env` 文件，填入获取的配置：

```env
RAGFLOW_API_URL=https://your-ragflow-server.com
RAGFLOW_API_KEY=ragflow-your-api-key
RAGFLOW_CHAT_ID=your-chat-id
```

### 4. 测试运行

```bash
python query_tax.py "增值税税率是多少？"
```

## 使用方法

在 OpenClaw 中安装此 skill 后，当用户提出税务相关问题时会自动调用知识库查询。

**示例问题：**
- "最新的增值税优惠政策是什么？"
- "企业所得税的扣除标准有哪些？"
- "个人所得税专项附加扣除包括哪些？"

## 常见问题

**Q: 在哪里找到 API Key？**  
A: 登录 RAGFlow → 点击右上角头像 → 选择 "API Keys" → 点击 "Create New Key" → 复制生成的密钥（格式：`ragflow-xxxxx`）

**Q: 在哪里找到 Chat ID？**  
A: 登录 RAGFlow → 进入 "Chat" 页面 → 找到税务知识助手 → 查看详情即可看到 Chat ID

**Q: 提示认证失败？**  
A: 检查 `.env` 文件中的 API Key 是否正确，确保没有多余空格。

**Q: 连接超时？**  
A: 确认 API URL 地址正确，且网络可以访问该地址。

## 联系方式

如有问题，请联系：zhao xin
