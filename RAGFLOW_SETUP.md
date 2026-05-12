# RAGFlow 配置指南

本指南将帮助你设置 RAGFlow 环境，以便使用 TAX Knowledge Skill。

## 📋 前置要求

在使用此 skill 之前，你需要：
1. 一个运行中的 RAGFlow 实例
2. API Key（用于认证）
3. Chat ID（对话助手 ID）
4. 已上传的税务知识文档

---

## 🚀 方案选择

### 方案 A：使用现有的 RAGFlow 服务（最快）

如果你所在的公司或组织已经部署了 RAGFlow：

1. **联系管理员**获取以下信息：
   - RAGFlow 服务器地址（URL）
   - 你的 API Key
   - 税务知识库的 Chat ID

2. **配置 `.env` 文件**：
   ```env
   RAGFLOW_API_URL=https://your-company-ragflow.com
   RAGFLOW_API_KEY=your-api-key-here
   RAGFLOW_CHAT_ID=your-chat-id-here
   ```

3. **开始使用** ✅

---

### 方案 B：自行部署 RAGFlow（完整控制）

如果你想完全控制自己的 RAGFlow 环境，可以按照以下步骤部署。

#### 步骤 1：系统要求

**最低配置：**
- CPU: 4 核
- 内存: 8 GB
- 磁盘: 50 GB
- Docker 和 Docker Compose

**推荐配置：**
- CPU: 8 核
- 内存: 16 GB
- 磁盘: 100 GB SSD
- GPU（可选，用于加速 embeddings）

#### 步骤 2：安装 Docker

**Windows:**
1. 下载 Docker Desktop: https://www.docker.com/products/docker-desktop
2. 安装并启动 Docker Desktop
3. 验证安装：
   ```bash
   docker --version
   docker-compose --version
   ```

**Linux (Ubuntu):**
```bash
# 安装 Docker
sudo apt-get update
sudo apt-get install docker.io docker-compose

# 启动 Docker
sudo systemctl start docker
sudo systemctl enable docker

# 验证安装
docker --version
docker-compose --version
```

**macOS:**
1. 下载 Docker Desktop for Mac
2. 安装并启动
3. 验证安装

#### 步骤 3：部署 RAGFlow

```bash
# 1. 克隆 RAGFlow 仓库
git clone https://github.com/infiniflow/ragflow.git
cd ragflow

# 2. 启动 RAGFlow
docker-compose up -d

# 3. 等待服务启动（约 2-5 分钟）
docker-compose ps

# 4. 访问 RAGFlow Web 界面
# 浏览器打开: http://localhost:80
```

#### 步骤 4：初始化配置

1. **首次访问** `http://localhost:80`
2. **创建管理员账户**
   - 用户名：admin
   - 密码：设置强密码
   - 邮箱：你的邮箱

3. **登录系统**

#### 步骤 5：创建知识库

1. **进入 "Knowledge Base" 页面**

2. **创建新的知识库**：
   - 点击 "Create Dataset"
   - 名称：`Tax Knowledge Base`
   - 描述：`税务政策与法规知识库`
   - 语言：中文
   - 解析方法：选择 "General" 或 "Q&A"

3. **上传税务文档**：
   
   准备以下类型的文档：
   - PDF：税法条文、政策解读
   - Word：内部税务手册
   - Excel：税率表、申报表模板
   - TXT：常见问题解答
   
   **推荐上传的文档：**
   ```
   - 中华人民共和国增值税法.pdf
   - 企业所得税法实施条例.pdf
   - 个人所得税专项附加扣除暂行办法.pdf
   - 税收优惠政策汇编.pdf
   - 税务申报操作指南.docx
   ```

4. **等待文档解析完成**
   - 状态变为 "Ready" 表示解析完成
   - 可以在 "Chunks" 标签页查看解析结果

#### 步骤 6：创建对话助手

1. **进入 "Chat" 页面**

2. **创建新的对话助手**：
   - 点击 "Create Assistant"
   - 名称：`Tax Assistant`
   - 描述：`税务知识问答助手`
   - 关联知识库：选择刚才创建的 `Tax Knowledge Base`
   - 模型：选择可用的模型（如 deepseek-chat, qwen 等）
   - 温度：0.7（平衡创造性和准确性）
   - 最大令牌：2000

3. **保存并测试**：
   - 在聊天窗口测试提问
   - 例如："增值税税率是多少？"
   - 确认回答基于知识库内容

#### 步骤 7：获取 API Key 和 Chat ID

1. **获取 API Key**：
   - 点击右上角用户头像
   - 选择 "API Keys"
   - 点击 "Create New Key"
   - 复制生成的 API Key（格式：`ragflow-xxxxxxxx`）
   - ⚠️ **妥善保存，只显示一次**

2. **获取 Chat ID**：
   - 回到 "Chat" 页面
   - 找到你创建的 `Tax Assistant`
   - 点击查看详情
   - 复制 Chat ID（格式：`e4f3a7de397911f1ab5cc5a32a377c21`）

#### 步骤 8：配置 Skill

1. **创建 `.env` 文件**：
   ```bash
   cp .env.example .env
   ```

2. **编辑 `.env` 文件**：
   ```env
   RAGFLOW_API_URL=http://localhost
   RAGFLOW_API_KEY=ragflow-你的实际API密钥
   RAGFLOW_CHAT_ID=你的实际Chat_ID
   ```

3. **验证配置**：
   ```bash
   python verify_installation.py
   ```

4. **测试查询**：
   ```bash
   python query_tax.py "最新的增值税优惠政策是什么？"
   ```

---

### 方案 C：使用云端 RAGFlow 服务（推荐新手）

如果不想自己部署，可以使用云端服务：

#### 选项 1：RAGFlow 官方云服务

1. 访问 RAGFlow 官方网站
2. 注册账号
3. 创建知识库和助手
4. 获取 API 凭证

#### 选项 2：其他云服务商

- **阿里云**：提供类似的知识库服务
- **腾讯云**：智能知识库平台
- **华为云**：AI 知识库服务

---

## 📚 准备税务知识库文档

### 推荐文档清单

为了让 skill 发挥最佳效果，建议准备以下文档：

#### 1. 法律法规类
- 《中华人民共和国增值税法》
- 《中华人民共和国企业所得税法》
- 《中华人民共和国个人所得税法》
- 《税收征收管理法》
- 各税种的实施条例

#### 2. 政策解读类
- 最新税收优惠政策汇编
- 增值税改革政策解读
- 个税专项附加扣除详解
- 小微企业税收优惠

#### 3. 操作指南类
- 税务申报操作流程
- 发票管理规定
- 税务登记指南
- 纳税信用等级评定

#### 4. 常见问题类
- 税务 FAQ 汇总
- 常见错误及解决方法
- 案例分析

### 文档格式建议

- **PDF**：适合正式的法律文本
- **Word (.docx)**：适合可编辑的操作指南
- **Markdown (.md)**：适合结构化的 FAQ
- **Excel (.xlsx)**：适合税率表、对照表

### 文档质量要求

✅ **好的文档特征：**
- 清晰的章节结构
- 准确的术语使用
- 最新的政策内容
- 完整的上下文信息

❌ **避免的问题：**
- 过时的政策（注意时效性）
- 模糊不清的表述
- 缺少关键信息
- 格式混乱

---

## 🔧 高级配置

### 优化知识库性能

1. **文档分块策略**：
   - 小文档（< 10页）：使用默认分块
   - 大文档（> 50页）：按章节分块
   - FAQ：使用 Q&A 模式

2. **Embedding 模型选择**：
   - 中文优先：bge-m3, text-embedding-ada-002
   - 多语言：multilingual-e5-large

3. **检索参数调整**：
   - Top K: 5-10（返回最相关的片段数）
   - Score Threshold: 0.5-0.7（相关性阈值）

### 安全建议

1. **API Key 管理**：
   - 不要硬编码在代码中
   - 使用环境变量或密钥管理服务
   - 定期轮换（每 90 天）

2. **访问控制**：
   - 限制 API Key 的权限范围
   - 设置 IP 白名单（如果支持）
   - 监控 API 使用日志

3. **数据隐私**：
   - 不要上传包含个人敏感信息的文档
   - 对内部文档进行脱敏处理
   - 定期审查上传的文档

---

## ❓ 常见问题

### Q1: RAGFlow 启动失败怎么办？

**检查项：**
```bash
# 查看日志
docker-compose logs -f

# 检查端口占用
netstat -ano | findstr :80

# 重启服务
docker-compose down
docker-compose up -d
```

### Q2: 文档解析很慢？

**优化建议：**
- 减少单次上传的文档数量
- 使用较小的文档（< 50MB）
- 增加服务器资源（CPU/内存）
- 检查网络连接

### Q3: 回答不准确？

**改进方法：**
1. 检查文档质量（是否清晰、完整）
2. 调整检索参数（Top K, Threshold）
3. 添加更多相关文档
4. 优化 Prompt 模板

### Q4: API 连接超时？

**排查步骤：**
1. 确认 RAGFlow 服务正在运行
2. 检查防火墙设置
3. 验证 URL 是否正确
4. 测试网络连通性：
   ```bash
   curl http://localhost/api/v1/system/version
   ```

### Q5: 如何更新知识库？

**操作步骤：**
1. 在 Web 界面删除旧文档
2. 上传新版本的文档
3. 等待解析完成
4. 测试查询效果

---

## 📞 获取帮助

### 官方资源

- **RAGFlow GitHub**: https://github.com/infiniflow/ragflow
- **官方文档**: https://ragflow.io/docs
- **社区论坛**: https://github.com/infiniflow/ragflow/discussions

### 本项目支持

- **Issues**: https://github.com/zhaoxin139/tax-knowledge-skill/issues
- **邮件**: zhaoxin@example.com

---

## 🎯 快速检查清单

在开始使用 skill 之前，确认：

- [ ] RAGFlow 服务正在运行
- [ ] 已创建知识库并上传文档
- [ ] 文档解析完成（状态为 Ready）
- [ ] 已创建对话助手
- [ ] 已获取 API Key
- [ ] 已获取 Chat ID
- [ ] `.env` 文件配置正确
- [ ] 运行 `verify_installation.py` 全部通过
- [ ] 测试查询返回合理答案

---

## 🚀 下一步

配置完成后，你就可以：

1. **开始使用 skill**：
   ```bash
   python query_tax.py "你的税务问题"
   ```

2. **集成到 OpenClaw**：
   - 按照 OpenClaw 的安装说明
   - 加载此 skill
   - 开始智能问答

3. **持续优化**：
   - 收集用户反馈
   - 补充更多文档
   - 调整参数以获得更好的效果

祝你使用愉快！🎉
