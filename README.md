# 测试项目

这是一个简单的前端测试项目，用于代码测试和演示。

## 项目结构

```
test-project/
├── index.html      # 主页面
├── style.css       # 样式文件
├── script.js       # JavaScript 交互脚本
└── README.md       # 说明文档
```

## 功能特性

- **响应式设计**：适配不同屏幕尺寸
- **交互按钮**：点击计数器，带有鼓励消息
- **实时时钟**：显示当前日期和时间
- **现代UI**：渐变背景、卡片布局、悬停效果

## 使用方法

1. 直接在浏览器中打开 `index.html` 文件
2. 或者使用本地服务器运行（推荐）：
   ```bash
   # 使用 Python
   python -m http.server 8000
   
   # 或使用 Node.js
   npx serve
   ```

3. 访问 `http://localhost:8000`

## 技术栈

- HTML5
- CSS3 (Flexbox, Grid, Animations)
- Vanilla JavaScript (ES6+)

## 测试要点

- 按钮点击事件处理
- DOM 操作和更新
- 定时器功能
- CSS 动画和过渡效果
- 响应式布局
