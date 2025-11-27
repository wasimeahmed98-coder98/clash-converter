import yaml
import os

# 定义基础模板路径和输出路径
TEMPLATE_PATH = 'templates/base.yaml'
OUTPUT_PATH = 'clash_config.yaml'

def load_template(path):
    """加载基础 Clash 模板"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Template not found at {path}")
    
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def parse_source_data(source):
    """
    [核心逻辑] 在这里编写你的解析代码
    将传入的源数据（如 vmess 链接、订阅内容等）转换为 Clash 的 proxy 字典格式
    """
    # 示例：这是一个模拟的节点数据
    # 在实际项目中，你需要编写逻辑来解析 vmess:// 或 ss:// 链接
    proxies = [
        {
            "name": "示例节点-香港",
            "type": "ss",
            "server": "1.2.3.4",
            "port": 8888,
            "cipher": "aes-256-gcm",
            "password": "password",
            "udp": True
        },
        {
            "name": "示例节点-美国",
            "type": "vmess",
            "server": "5.6.7.8",
            "port": 443,
            "uuid": "your-uuid",
            "alterId": 0,
            "cipher": "auto",
            "tls": True,
            "network": "ws"
        }
    ]
    return proxies

def generate_config():
    # 1. 加载模板
    config = load_template(TEMPLATE_PATH)
    
    # 2. 获取转换后的节点数据
    # 这里假设你从文件或 URL 获取源数据
    source_data = "raw_data_placeholder" 
    proxies = parse_source_data(source_data)
    
    # 3. 填充 proxies 部分
    config['proxies'] = proxies
    
    # 4. 填充 proxy-groups (自动将所有节点加入第一个选择组)
    if 'proxy-groups' in config and len(config['proxy-groups']) > 0:
        proxy_names = [p['name'] for p in proxies]
        # 将新节点添加到第一个策略组（通常是 Proxy 或 Select）
        config['proxy-groups'][0]['proxies'].extend(proxy_names)

    # 5. 保存文件
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        # allow_unicode=True 确保中文字符正常显示
        yaml.dump(config, f, allow_unicode=True, sort_keys=False)
    
    print(f"✅ 转换成功！配置文件已保存为: {OUTPUT_PATH}")

if __name__ == "__main__":
    generate_config()