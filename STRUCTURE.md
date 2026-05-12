# 项目结构说明

```
tax-knowledge-skill/
│
├── plugin.json              # OpenClaw 插件配置文件（必需）
├── SKILL.md                 # 技能说明文档（必需）
├── query_tax.py             # 核心执行脚本
├── verify_installation.py   # 安装验证脚本
│
├── requirements.txt         # Python 依赖列表
├── .env.example             # 环境变量配置示例
├── .gitignore               # Git 忽略文件配置
│
├── README.md                # 详细使用文档
├── QUICKSTART.md            # 快速开始指南
└── STRUCTURE.md             # 本文件 - 项目结构说明
```

## 文件说明

### 核心文件（必需）

#### `plugin.json`
- **作用**: OpenClaw 插件的元数据配置
- **内容**: 技能名称、版本、描述、权限等
- **修改**: 一般不需要修改

#### `SKILL.md`
- **作用**: 告诉 AI 如何使用这个技能
- **内容**: 触发条件、使用指令、示例
- **修改**: 根据实际需求调整触发条件和指令

#### `query_tax.py`
- **作用**: 与 RAGFlow API 交互的核心脚本
- **功能**: 
  - 读取环境变量配置
  - 发送问题到 RAGFlow
  - 接收并返回答案
- **修改**: 如需自定义 API 调用逻辑时修改

### 配置文件

#### `requirements.txt`
- **作用**: 声明 Python 依赖包
- **内容**: 
  - `requests`: HTTP 请求库
  - `python-dotenv`: 环境变量加载库
- **修改**: 添加新依赖时更新

#### `.env.example`
- **作用**: 环境变量配置模板
- **内容**: API URL、API Key、Chat ID 的示例
- **使用**: 复制为 `.env` 并填入实际值
- **注意**: `.env` 文件已被 `.gitignore` 忽略，不会提交到版本控制

#### `.gitignore`
- **作用**: Git 版本控制忽略规则
- **保护**: 防止敏感信息（如 `.env`）被提交

### 辅助脚本

#### `verify_installation.py`
- **作用**: 自动验证安装是否正确
- **检查项**:
  - Python 版本
  - 依赖包安装
  - 环境变量配置
  - API 连接测试
- **使用**: 安装后运行此脚本确认配置

### 文档文件

#### `README.md`
- **作用**: 完整的使用文档
- **内容**:
  - 功能特性介绍
  - 详细安装步骤
  - 使用方法说明
  - 故障排除指南
  - 技术架构说明
  - 安全建议

#### `QUICKSTART.md`
- **作用**: 5 分钟快速上手指南
- **内容**: 最简化的安装和使用步骤
- **适用**: 新手用户快速开始

#### `STRUCTURE.md`
- **作用**: 项目结构说明（本文件）
- **内容**: 各文件的用途和关系

## 工作流程

### 用户安装流程

1. **克隆/下载** 此 skill 目录
2. **安装依赖**: `pip install -r requirements.txt`
3. **配置环境**: 复制 `.env.example` 为 `.env` 并填写配置
4. **验证安装**: 运行 `python verify_installation.py`
5. **开始使用**: 在 OpenClaw 中加载此 skill

### AI 调用流程

1. 用户提出税务相关问题
2. OpenClaw 根据 `SKILL.md` 判断需要调用此技能
3. 执行 `query_tax.py` 脚本，传入用户问题
4. 脚本读取 `.env` 中的配置
5. 向 RAGFlow API 发送请求
6. 接收答案并返回给用户

## 自定义修改

### 修改 API 端点
编辑 `query_tax.py` 第 24 行的 URL 构建逻辑

### 修改超时时间
编辑 `query_tax.py` 第 45 行的 `timeout` 参数

### 修改模型名称
编辑 `query_tax.py` 第 33 行的 `model` 参数

### 添加新功能
在 `query_tax.py` 中添加新的函数或参数处理逻辑

## 安全注意事项

1. **永远不要** 将 `.env` 文件提交到版本控制系统
2. **定期轮换** API Key
3. **限制权限** API Key 只授予必要的权限
4. **使用 HTTPS** 确保数据传输安全
5. **验证输入** 对用户输入进行必要的验证和清理

## 版本历史

- v1.0.0: 初始版本，基础问答功能
