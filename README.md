# Clash Config Converter

一个基于 Python 的工具，用于将 [输入格式] 转换为 Clash 兼容的 YAML 配置文件。

## 功能
- 支持加载基础 YAML 模板
- 自动填充 `proxies` 和更新 `proxy-groups`
- 保持 YAML 格式规范

## 快速开始

1. 安装依赖:
   ```bash
   pip install -r requirements.txt
2. 修改 templates/base.yaml 根据你的需求调整规则。

3. 运行转换器:

 ```bash
 Bash
 python main.py
