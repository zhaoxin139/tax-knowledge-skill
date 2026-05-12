"""
安装验证脚本
用于检查 skill 是否已正确配置
"""
import os
import sys

def check_python_version():
    """检查 Python 版本"""
    print("✓ 检查 Python 版本...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 6:
        print(f"  ✓ Python {version.major}.{version.minor}.{version.micro} - 符合要求")
        return True
    else:
        print(f"  ✗ Python {version.major}.{version.minor}.{version.micro} - 需要 Python 3.6+")
        return False

def check_dependencies():
    """检查依赖包是否安装"""
    print("\n✓ 检查依赖包...")
    missing = []
    
    try:
        import requests
        print(f"  ✓ requests {requests.__version__}")
    except ImportError:
        missing.append("requests")
        print(f"  ✗ requests - 未安装")
    
    try:
        from dotenv import load_dotenv
        print(f"  ✓ python-dotenv - 已安装")
    except ImportError:
        missing.append("python-dotenv")
        print(f"  ✗ python-dotenv - 未安装（可选）")
    
    if missing:
        print(f"\n  请运行: pip install -r requirements.txt")
        return False
    return True

def check_env_file():
    """检查 .env 文件是否存在"""
    print("\n✓ 检查配置文件...")
    if os.path.exists(".env"):
        print("  ✓ .env 文件存在")
        return True
    else:
        print("  ⚠ .env 文件不存在")
        print("  提示: 复制 .env.example 为 .env 并配置你的参数")
        return False

def check_env_variables():
    """检查环境变量是否配置"""
    print("\n✓ 检查环境变量...")
    
    # 尝试加载 .env 文件
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass
    
    required_vars = [
        "RAGFLOW_API_URL",
        "RAGFLOW_API_KEY", 
        "RAGFLOW_CHAT_ID"
    ]
    
    all_set = True
    for var in required_vars:
        value = os.getenv(var)
        if value:
            # 隐藏敏感信息
            if var == "RAGFLOW_API_KEY":
                display_value = value[:8] + "..." if len(value) > 8 else "***"
            else:
                display_value = value
            print(f"  ✓ {var} = {display_value}")
        else:
            print(f"  ✗ {var} - 未配置")
            all_set = False
    
    return all_set

def test_api_connection():
    """测试 API 连接"""
    print("\n✓ 测试 API 连接...")
    
    RAGFLOW_API_URL = os.getenv("RAGFLOW_API_URL")
    RAGFLOW_API_KEY = os.getenv("RAGFLOW_API_KEY")
    RAGFLOW_CHAT_ID = os.getenv("RAGFLOW_CHAT_ID")
    
    if not all([RAGFLOW_API_URL, RAGFLOW_API_KEY, RAGFLOW_CHAT_ID]):
        print("  ⚠ 跳过测试：环境变量未完全配置")
        return None
    
    try:
        import requests
        
        url = f"{RAGFLOW_API_URL}/api/v1/chats_openai/{RAGFLOW_CHAT_ID}/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {RAGFLOW_API_KEY}"
        }
        
        # 发送一个简单的测试请求
        payload = {
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": "你好"}],
            "stream": False
        }
        
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        
        if response.status_code == 200:
            print("  ✓ API 连接成功")
            return True
        elif response.status_code == 401:
            print("  ✗ API 认证失败：请检查 API Key")
            return False
        else:
            print(f"  ⚠ API 返回状态码: {response.status_code}")
            print(f"  响应: {response.text[:200]}")
            return False
            
    except requests.exceptions.Timeout:
        print("  ✗ 连接超时：请检查网络和 RAGFLOW_API_URL")
        return False
    except requests.exceptions.ConnectionError:
        print("  ✗ 无法连接到 RAGFlow 服务：请检查 URL 和网络")
        return False
    except Exception as e:
        print(f"  ✗ 测试失败: {e}")
        return False

def main():
    """主函数"""
    print("=" * 60)
    print("TAX Knowledge Skill - 安装验证")
    print("=" * 60)
    
    results = []
    
    # 执行各项检查
    results.append(("Python 版本", check_python_version()))
    results.append(("依赖包", check_dependencies()))
    results.append(("配置文件", check_env_file()))
    results.append(("环境变量", check_env_variables()))
    
    # 如果环境变量配置完整，测试 API 连接
    env_vars_set = all([
        os.getenv("RAGFLOW_API_URL"),
        os.getenv("RAGFLOW_API_KEY"),
        os.getenv("RAGFLOW_CHAT_ID")
    ])
    
    if env_vars_set:
        api_result = test_api_connection()
        results.append(("API 连接", api_result if api_result is not None else True))
    
    # 总结
    print("\n" + "=" * 60)
    print("验证总结")
    print("=" * 60)
    
    all_passed = all(result[1] for result in results if result[1] is not None)
    
    for name, passed in results:
        if passed is None:
            status = "⊘ 跳过"
        elif passed:
            status = "✓ 通过"
        else:
            status = "✗ 失败"
        print(f"{status} - {name}")
    
    print("=" * 60)
    
    if all_passed:
        print("\n🎉 所有检查通过！Skill 已准备就绪。")
        print("\n你可以开始使用了：")
        print('  python query_tax.py "你的问题"')
    else:
        print("\n⚠ 部分检查未通过，请参考上述提示进行修复。")
        print("\n快速修复指南：")
        print("  1. 安装依赖: pip install -r requirements.txt")
        print("  2. 创建配置: copy .env.example .env (Windows) 或 cp .env.example .env (Linux/Mac)")
        print("  3. 编辑 .env 文件，填入你的实际配置")
        print("\n详细说明请查看: QUICKSTART.md")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
