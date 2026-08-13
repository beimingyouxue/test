// 点击按钮功能
let clickCount = 0;
const clickBtn = document.getElementById('clickBtn');
const output = document.getElementById('output');

clickBtn.addEventListener('click', function() {
    clickCount++;
    const messages = [
        '第一次点击！🎉',
        '继续加油！💪',
        '太棒了！⭐',
        '你真厉害！🚀',
        '保持下去！🔥'
    ];
    
    const messageIndex = Math.min(clickCount - 1, messages.length - 1);
    output.textContent = `已点击 ${clickCount} 次 - ${messages[messageIndex]}`;
    
    // 添加动画效果
    this.style.transform = 'scale(0.95)';
    setTimeout(() => {
        this.style.transform = 'scale(1)';
    }, 100);
});

// 实时时间显示
function updateTime() {
    const now = new Date();
    const timeString = now.toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: false
    });
    document.getElementById('time').textContent = timeString;
}

// 每秒更新时间
updateTime();
setInterval(updateTime, 1000);

// 页面加载完成提示
console.log('测试项目已加载完成！');
console.log('功能包括：');
console.log('- 按钮点击计数器');
console.log('- 实时时间显示');
console.log('- 响应式卡片布局');
