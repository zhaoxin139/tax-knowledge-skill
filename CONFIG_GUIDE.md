# 快速配置指南 - 3 分钟完成设置

本指南将帮助你在 3 分钟内完成 TAX Knowledge Skill 的配置。

## 🚀 快速开始

### 前提条件

确保你已经：
- ✅ 安装了 Python 3.6+
- ✅ 安装了依赖：`pip install -r requirements.txt`
- ✅ 有一个 RAGFlow 环境（本地部署或云服务）

---

## ⚡ 方法 1：使用配置向导（推荐）

这是最简单的方式，只需运行一个命令！

### 步骤 1：运行配置向导

```bash
python setup_config.py
```

### 步骤 2：按照提示输入信息

向导会询问你三个问题：

1. **RAGFlow API URL**
   ```
   例如: http://localhost 或 https://your-ragflow.com
   ```

2. **API Key**（输入时会隐藏显示）
   ```
   格式: ragflow-xxxxxxxxxxxx
   ```

3. **Chat ID**
   ```
   格式: e4f3a7de397911f1ab5cc5a32a377c21
   ```

### 步骤 3：测试连接

向导会自动测试 API 连接，如果成功就配置完成了！

### 步骤 4：开始使用

```bash
python query_tax.py "增值税税率是多少？"
```

---

## 📝 方法 2：手动配置

如果你喜欢手动配置，可以按照以下步骤：

### 步骤 1：创建 .env 文件

**Windows:**
```powershell
copy .env.example .env
notepad .env
```

**Linux/Mac:**
```bash
cp .env.example .env
nano .env
```

### 步骤 2：编辑配置文件

在 `.env` 文件中填入你的实际配置：

```env
RAGFLOW_API_URL=http://localhost
RAGFLOW_API_KEY=ragflow-你的实际密钥
RAGFLOW_CHAT_ID=你的实际ChatID
```

### 步骤 3：验证配置

```bash
python verify_installation.py
```

### 步骤 4：测试使用

```bash
python query_tax.py "最新的税收优惠政策是什么？"
```

---

## 🔑 如何获取 API Key 和 Chat ID

如果你还不知道如何获取这些信息，请按照以下步骤：

### 1. 访问 RAGFlow Web 界面

打开浏览器，访问你的 RAGFlow 地址：
- 本地部署：`http://localhost`
- 远程部署：`https://your-ragflow-domain.com`

### 2. 获取 API Key

1. 点击右上角的用户头像
2. 选择 **"API Keys"**
3. 点击 **"Create New Key"**
4. 复制生成的 API Key（格式：`ragflow-xxxxxxxx`）

⚠️ **注意**：API Key 只显示一次，请妥善保存！

### 3. 获取 Chat ID

1. 进入 **"Chat"** 页面
2. 找到你创建的对话助手
3. 点击查看详细信息
4. 复制 Chat ID（格式：`e4f3a7de397911f1ab5cc5a32a377c21`）

---

## ❓ 还没有 RAGFlow 环境？

如果你还没有 RAGFlow 环境，有以下选择：

### 选项 A：联系管理员
如果你的公司或组织已经部署了 RAGFlow，联系管理员获取：
- API URL
- API Key
- Chat ID

### 选项 B：自行部署
参考 [RAGFLOW_SETUP.md](RAGFLOW_SETUP.md) 中的详细部署指南。

### 选项 C：使用云服务
考虑使用 RAGFlow 官方云服务或其他云服务商的知识库服务。

---

## 🔍 验证配置是否正确

运行验证脚本检查所有配置：

```bash
python verify_installation.py
```

你会看到类似这样的输出：

```
============================================================
TAX Knowledge Skill - 安装验证
============================================================
✓ 检查 Python 版本...
  ✓ Python 3.14.4 - 符合要求

✓ 检查依赖包...
  ✓ requests 2.33.1
  ✓ python-dotenv - 已安装

✓ 检查配置文件...
  ✓ .env 文件存在

✓ 检查环境变量...
  ✓ RAGFLOW_API_URL = http://localhost
  ✓ RAGFLOW_API_KEY = ragflow-...
  ✓ RAGFLOW_CHAT_ID = e4f3a7de397911f1ab5cc5a32a377c21

✓ 测试 API 连接...
  ✓ API 连接成功

============================================================
验证总结
============================================================
✓ 通过 - Python 版本
✓ 通过 - 依赖包
✓ 通过 - 配置文件
✓ 通过 - 环境变量
✓ 通过 - API 连接
============================================================

🎉 所有检查通过！Skill 已准备就绪。
```

---

## 🎯 常见问题

### Q1: 运行 setup_config.py 时提示找不到模块？

**解决方案：**
```bash
pip install -r requirements.txt
```

### Q2: API 连接测试失败？

**检查项：**
1. RAGFlow 服务是否正在运行
2. URL 地址是否正确
3. API Key 和 Chat ID 是否正确
4. 网络是否正常

**测试命令：**
```bash
curl http://localhost/api/v1/system/version
```

### Q3: 在哪里可以找到我的 API Key？

**路径：**
RAGFlow Web 界面 → 用户头像 → API Keys → Create New Key

### Q4: 配置错了怎么办？

**重新配置：**
```bash
# 删除旧的 .env 文件
rm .env  # Linux/Mac
del .env  # Windows

# 重新运行配置向导
python setup_config.py
```

或者直接编辑 `.env` 文件修改配置。

### Q5: 可以配置多个 RAGFlow 实例吗？

目前 skill 只支持一个 RAGFlow 实例。如需切换，修改 `.env` 文件中的配置即可。

---

## 📞 需要帮助？

如果遇到问题：

1. **查看完整文档**：[RAGFLOW_SETUP.md](RAGFLOW_SETUP.md)
2. **提交 Issue**：https://github.com/zhaoxin139/tax-knowledge-skill/issues
3. **运行验证脚本**：`python verify_installation.py` 查看详细错误信息

---

## ✅ 配置完成检查清单

确认以下项目都已完成：

- [ ] 已安装 Python 依赖
- [ ] 已获取 RAGFlow API URL
- [ ] 已获取 API Key
- [ ] 已获取 Chat ID
- [ ] 已运行 `setup_config.py` 或手动配置 `.env`
- [ ] 已运行 `verify_installation.py` 并全部通过
- [ ] 已成功测试查询：`python query_tax.py "测试问题"`

全部勾选后，你就可以开始使用了！🎉

---

## 🚀 下一步

配置完成后：

1. **测试基本功能**
   ```bash
   python query_tax.py "增值税税率是多少？"
   ```

2. **集成到 OpenClaw**
   - 按照 OpenClaw 的安装说明加载此 skill
   - 开始智能问答

3. **优化知识库**
   - 上传更多税务文档
   - 调整检索参数
   - 收集用户反馈

祝你使用愉快！
