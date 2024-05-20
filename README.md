# Planegame
组员：罗嘉文，魏启哲，席琳峰，陈延平，朱俊宇

游戏玩法

上下左右控制外卖员摧毁外星人，击毁外星人boss得十分，击毁普通敌人得一分，得到50分游戏胜利。击毁敌人有概率产生道具，道具有两种，一种是回血的，一种是加强火力。玩家生命值为3，被敌人击中或者碰撞到敌人将会减一，生命值为0时游戏失败。

程序功能实现
- Menu主界面选择开始游戏以及退出游戏
- 上下左右方向键控制外卖员上下左右移动
- 游戏开始后左上角分数与玩家血量的更新
- 所有精灵的动画效果实现（不包括画图）
- 游戏中音效的播放，包括背景音乐，玩家射出的食物销毁的时候的音效，玩家获得道具后的音效。
- 玩家每间隔一段时间发射食物，敌人每间隔一段时间发射子弹。
- 对游戏中所有需要进行碰撞的对象进行碰撞检测
- boss敌人特殊的移动方式，攻击逻辑，正上方显示的boss血条，以及boss被击毁时会有特殊的被击毁动画播放。
- 吃到道具后对于道具的响应，增长血量或者是增加一个加强火力组件（以component的形式被添加到Hero类中）
- 背景的无缝滚动
- 游戏失败或者成功后界面的显示
- 制作该游戏中运用的设计模式：工厂模式，抽象工厂模式，适配器模式，装饰器模式


