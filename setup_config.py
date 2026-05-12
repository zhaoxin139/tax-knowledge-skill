#!/usr/bin/env python3
"""
TAX Knowledge Skill - 交互式配置向导
帮助用户轻松配置 RAGFlow API 凭证
"""
import os
import sys
from pathlib import Path

def print_header():
    """打印欢迎信息"""
    print("=" * 70)
    print("  TAX Knowledge Skill - 配置向导")
    print("=" * 70)
    print()
    print("此向导将帮助你配置 RAGFlow API 连接信息。")
    print("如果你还没有 RAGFlow 环境，请先参考 RAGFLOW_SETUP.md")
    print()

def get_input(prompt, default=None, required=True, hide_input=False):
    """获取用户输入"""
    if default:
        prompt = f"{prompt} [{default}]"
    
    while True:
        if hide_input:
            try:
                import getpass
                value = getpass.getpass(prompt + ": ")
            except:
                # 如果不支持 getpass，使用普通输入
                value = input(prompt + ": ")
        else:
            value = input(prompt + ": ")
        
        if value:
            return value
        elif default:
            return default
        elif required:
            print("  ⚠️  此项为必填项，请输入值")
        else:
            return ""

def check_existing_config():
    """检查是否已有配置文件"""
    env_file = Path(".env")
    if env_file.exists():
        print("📝 检测到已存在的 .env 文件")
        print()
        
        # 读取现有配置
        config = {}
        with open(env_file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    config[key.strip()] = value.strip()
        
        print("当前配置：")
        print(f"  RAGFLOW_API_URL: {config.get('RAGFLOW_API_URL', '未设置')}")
        print(f"  RAGFLOW_API_KEY: {'***' + config.get('RAGFLOW_API_KEY', '')[-4:] if config.get('RAGFLOW_API_KEY') else '未设置'}")
        print(f"  RAGFLOW_CHAT_ID: {config.get('RAGFLOW_CHAT_ID', '未设置')}")
        print()
        
        choice = input("是否要修改现有配置？(y/n) [n]: ").strip().lower()
        if choice != 'y':
            return config
    
    return None

def guide_get_api_key():
    """提供获取 API Key 的指引"""
    print()
    print("=" * 70)
    print("  📖 如何获取 RAGFlow API Key 和 Chat ID")
    print("=" * 70)
    print()
    print("1️⃣  访问你的 RAGFlow Web 界面")
    print("   例如: http://localhost 或 https://your-ragflow.com")
    print()
    print("2️⃣  获取 API Key:")
    print("   - 点击右上角用户头像")
    print("   - 选择 'API Keys'")
    print("   - 点击 'Create New Key'")
    print("   - 复制生成的 API Key (格式: ragflow-xxxxxxxx)")
    print()
    print("3️⃣  获取 Chat ID:")
    print("   - 进入 'Chat' 页面")
    print("   - 找到你创建的对话助手")
    print("   - 复制 Chat ID (格式: e4f3a7de397911f1ab5cc5a32a377c21)")
    print()
    print("💡 提示: 如果还没有创建知识库和助手，请参考 RAGFLOW_SETUP.md")
    print()

def validate_url(url):
    """验证 URL 格式"""
    if not url:
        return False
    return url.startswith('http://') or url.startswith('https://')

def validate_api_key(key):
    """验证 API Key 格式"""
    if not key:
        return False
    return key.startswith('ragflow-')

def test_connection(api_url, api_key, chat_id):
    """测试 API 连接"""
    print()
    print("🔍 正在测试连接...")
    
    try:
        import requests
        
        url = f"{api_url}/api/v1/chats_openai/{chat_id}/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        
        payload = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": "你好"}],
            "stream": False
        }
        
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        
        if response.status_code == 200:
            print("  ✅ 连接成功！")
            return True
        elif response.status_code == 401:
            print("  ❌ 认证失败：API Key 可能不正确")
            return False
        else:
            print(f"  ⚠️  连接异常：HTTP {response.status_code}")
            print(f"     响应: {response.text[:200]}")
            return False
            
    except requests.exceptions.Timeout:
        print("  ❌ 连接超时：请检查 URL 和网络")
        return False
    except requests.exceptions.ConnectionError:
        print("  ❌ 无法连接到服务器：请检查 URL 是否正确")
        return False
    except Exception as e:
        print(f"  ❌ 测试失败: {e}")
        return False

def save_config(api_url, api_key, chat_id):
    """保存配置到 .env 文件"""
    env_content = f"""# RAGFlow API 配置
# 自动生成于 {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

RAGFLOW_API_URL={api_url}
RAGFLOW_API_KEY={api_key}
RAGFLOW_CHAT_ID={chat_id}
"""
    
    with open('.env', 'w', encoding='utf-8') as f:
        f.write(env_content)
    
    print()
    print("✅ 配置已保存到 .env 文件")

def main():
    """主函数"""
    print_header()
    
    # 检查现有配置
    existing_config = check_existing_config()
    
    if existing_config:
        # 使用现有配置或修改
        api_url = get_input(
            "RAGFlow API URL", 
            default=existing_config.get('RAGFLOW_API_URL', ''),
            required=True
        )
        api_key = get_input(
            "RAGFlow API Key", 
            default=existing_config.get('RAGFLOW_API_KEY', ''),
            required=True,
            hide_input=True
        )
        chat_id = get_input(
            "RAGFlow Chat ID", 
            default=existing_config.get('RAGFLOW_CHAT_ID', ''),
            required=True
        )
    else:
        # 全新配置
        print("让我们开始配置吧！")
        print()
        
        # 提供获取指引
        need_help = input("需要查看如何获取 API Key 和 Chat ID 吗？(y/n) [n]: ").strip().lower()
        if need_help == 'y':
            guide_get_api_key()
            input("按回车键继续...")
            print()
        
        # 获取 API URL
        print("步骤 1/3: 配置 RAGFlow API URL")
        print("-" * 70)
        api_url = get_input(
            "请输入 RAGFlow API URL",
            default="http://localhost",
            required=True
        )
        
        # 验证 URL
        while not validate_url(api_url):
            print("  ⚠️  URL 格式不正确，应以 http:// 或 https:// 开头")
            api_url = get_input(
                "请重新输入 RAGFlow API URL",
                default=api_url,
                required=True
            )
        
        print()
        
        # 获取 API Key
        print("步骤 2/3: 配置 API Key")
        print("-" * 70)
        api_key = get_input(
            "请输入 RAGFlow API Key",
            required=True,
            hide_input=True
        )
        
        # 验证 API Key 格式（可选）
        if not validate_api_key(api_key):
            print("  ⚠️  警告: API Key 通常以 'ragflow-' 开头")
            confirm = input("  确定要继续使用此 Key 吗？(y/n) [y]: ").strip().lower()
            if confirm == 'n':
                api_key = get_input(
                    "请重新输入 RAGFlow API Key",
                    required=True,
                    hide_input=True
                )
        
        print()
        
        # 获取 Chat ID
        print("步骤 3/3: 配置 Chat ID")
        print("-" * 70)
        chat_id = get_input(
            "请输入 RAGFlow Chat ID",
            required=True
        )
    
    print()
    print("=" * 70)
    print("  配置摘要")
    print("=" * 70)
    print(f"  API URL:   {api_url}")
    print(f"  API Key:   ***{api_key[-4:]}")
    print(f"  Chat ID:   {chat_id}")
    print()
    
    # 确认保存
    confirm = input("确认保存以上配置？(y/n) [y]: ").strip().lower()
    if confirm == 'n':
        print("❌ 配置已取消")
        return
    
    # 保存配置
    save_config(api_url, api_key, chat_id)
    
    # 测试连接
    test_choice = input("是否要测试 API 连接？(y/n) [y]: ").strip().lower()
    if test_choice != 'n':
        success = test_connection(api_url, api_key, chat_id)
        
        if success:
            print()
            print("=" * 70)
            print("  🎉 配置完成！")
            print("=" * 70)
            print()
            print("你现在可以开始使用 TAX Knowledge Skill 了！")
            print()
            print("测试命令:")
            print('  python query_tax.py "增值税税率是多少？"')
            print()
            print("或者运行完整验证:")
            print("  python verify_installation.py")
            print()
        else:
            print()
            print("=" * 70)
            print("  ⚠️  连接测试失败")
            print("=" * 70)
            print()
            print("配置已保存，但连接测试未通过。可能的原因：")
            print("  1. RAGFlow 服务未启动")
            print("  2. URL 地址不正确")
            print("  3. API Key 或 Chat ID 错误")
            print("  4. 网络问题")
            print()
            print("你可以稍后修复问题，然后运行:")
            print("  python verify_installation.py")
            print()
    else:
        print()
        print("=" * 70)
        print("  ✅ 配置已保存")
        print("=" * 70)
        print()
        print("建议运行验证脚本确认配置:")
        print("  python verify_installation.py")
        print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ 配置已取消")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
