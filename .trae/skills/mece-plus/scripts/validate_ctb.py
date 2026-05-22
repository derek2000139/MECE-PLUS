# -*- coding: utf-8 -*-
import re
import sys
import yaml

def validate_ctb(file_path):
    print(f"[*] 开始对文件进行确定性验证: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'# CTB_STATE_START\s*(.*?)\s*# CTB_STATE_END', content, re.DOTALL)
    if not match:
        print("[❌ ERROR] 未在输出中找到标准的 # CTB_STATE_START 和 # CTB_STATE_END 标记！")
        return False
    
    try:
        ctb_data = yaml.safe_load(match.group(1))
    except Exception as e:
        print(f"[❌ ERROR] YAML 解析失败: {e}")
        return False
        
    mece_nodes = ctb_data.get('from_01_mece', {}).get('nodes', [])
    forbidden_words = ["其他", "其它", "等等", "其余", "etc", "others"]
    
    for node in mece_nodes:
        for fw in forbidden_words:
            if fw in node.lower():
                print(f"[❌ MECE 违规] 节点 '{node}' 中包含了禁用词 '{fw}'！违反严格 MECE 原则。")
                return False
                
    node_count = len(mece_nodes)
    if node_count < 2 or node_count > 5:
        print(f"[❌ 结构违规] 第一层大类数量为 {node_count}。企业级标准要求大类数量必须在 2 ~ 5 个之间！")
        return False
        
    current_step = ctb_data.get('session', {}).get('current_step')
    print(f"[+] 当前流转阶段: {current_step}")
    if current_step == "02_system":
        if not ctb_data.get('from_02_system', {}).get('leverage_nodes'):
            print("[⚠️ 警告] 系统图阶段未指定关键杠杆节点 (leverage_nodes)。")
            
    print("[✅ 恭喜] 确定性校验通过！该阶段输出符合 McKinsey & BCG 交付标准。")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_ctb.py <path_to_markdown_file>")
        sys.exit(1)
    
    success = validate_ctb(sys.argv[1])
    sys.exit(0 if success else 1)