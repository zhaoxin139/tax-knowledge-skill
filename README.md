# TAX Knowledge Skill

一个用于查询 TAX 知识库的智能问答技能，基于 RAGFlow 实现企业私有知识的精准检索。

## 功能特性

- 🎯 基于 RAGFlow 的企业知识库问答
- 🔒 支持环境变量配置，保证 API 密钥安全
- 💬 支持多轮对话上下文
- ⚡ 快速响应，流式输出

## 安装步骤

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置环境变量

复制 `.env.example` 为 `.env` 文件：

```bash
cp .env.example .env
```

编辑 `.env` 文件，填入你的实际配置：

```env
RAGFLOW_API_URL=https://your-ragflow-instance.com
RAGFLOW_API_KEY=your-actual-api-key
RAGFLOW_CHAT_ID=your-chat-id
```

**配置说明：**
- `RAGFLOW_API_URL`: 你的 RAGFlow 实例地址
- `RAGFLOW_API_KEY`: 从 RAGFlow 后台获取的 API Key
- `RAGFLOW_CHAT_ID`: 你在 RAGFlow 中创建的对话助手 ID

### 3. 验证安装

运行安装验证脚本，确保所有配置正确：

```bash
python verify_installation.py
```

该脚本会检查：
- Python 版本是否符合要求
- 依赖包是否已安装
- 环境变量是否正确配置
- API 连接是否正常

### 4. 测试运行

```bash
python query_tax.py "最新的增值税优惠政策是什么？"
```

## 使用方法

### 在 OpenClaw 中使用

安装此 skill 后，当用户提出税务相关问题时，AI 会自动调用此技能查询 TAX 知识库。

**示例问题：**
- "最新的增值税优惠政策是什么？"
- "企业所得税的扣除标准有哪些？"
- "个人所得税专项附加扣除包括哪些项目？"

### 直接调用脚本

```bash
# 单次查询
python query_tax.py "你的问题"

# 多轮对话（需要传递 conversation_id）
python query_tax.py "第一个问题"
python query_tax.py "第二个问题" --conversation-id xxx
```

## 故障排除

### 问题 1: ModuleNotFoundError: No module named 'requests'

**解决方案：**
```bash
pip install requests
```

### 问题 2: API 请求失败或超时

**检查项：**
1. 确认 `RAGFLOW_API_URL` 地址是否正确且可访问
2. 确认网络连接正常
3. 检查防火墙设置

### 问题 3: 认证失败 (401 Unauthorized)

**解决方案：**
1. 检查 `RAGFLOW_API_KEY` 是否正确
2. 确认 API Key 未过期
3. 在 RAGFlow 后台重新生成 API Key

### 问题 4: 返回空答案或错误信息

**检查项：**
1. 确认 `RAGFLOW_CHAT_ID` 是否正确
2. 检查 RAGFlow 中是否已上传相关知识文档
3. 查看 RAGFlow 后台日志获取详细错误信息

## 技术架构

- **后端**: RAGFlow (RAG 引擎)
- **接口**: OpenAI 兼容 API
- **模型**: deepseek-chat (可配置)
- **通信**: HTTPS REST API

## 安全建议

1. **不要将 `.env` 文件提交到版本控制系统**
2. 定期轮换 API Key
3. 限制 API Key 的权限范围
4. 使用 HTTPS 确保传输安全

## 许可证

本项目仅供内部使用。

## 联系方式

如有问题，请联系：zhao xin

### 提交反馈

我们欢迎所有形式的反馈！如果你遇到问题或有建议，请通过以下方式联系我们：

1. **GitHub Issues**（推荐）：https://github.com/zhaoxin139/tax-knowledge-skill/issues
   - 🐛 [报告 Bug](https://github.com/zhaoxin139/tax-knowledge-skill/issues/new?template=bug_report.md)
   - 💡 [提出功能建议](https://github.com/zhaoxin139/tax-knowledge-skill/issues/new?template=feature_request.md)
   - ❓ [寻求配置帮助](https://github.com/zhaoxin139/tax-knowledge-skill/issues/new?template=config_help.md)

2. **直接联系**：发送邮件至 zhaoxin@example.com

在提交 issue 之前，请先搜索是否已有类似的问题，避免重复。
