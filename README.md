# 外卖员大战外星人
组员：罗嘉文，魏启哲，席琳峰，陈延平，朱俊宇
![30e49e4c5d867bc86e76d6ff8c277ac](https://github.com/AuSoleil626/Planegame/assets/142735159/962bb229-f11c-4311-a6c8-58aae6771d49)

![43f1cc150067797ccb09a321f5c3190](https://github.com/AuSoleil626/Planegame/assets/142735159/30c3d7cd-e603-4655-9a52-8280ddd97b09)

![d96066ba2af2c5bfe6fe0f818b95ea8](https://github.com/AuSoleil626/Planegame/assets/142735159/b52a3475-eea7-4bc6-89d7-701b8785ac42)

![795f164801dec95d89b3a09462cff31](https://github.com/AuSoleil626/Planegame/assets/142735159/7f1684fd-fc14-40b1-a047-4c9ccaadfb76)

![dc5fea16d1313046337ed127f1a9f77](https://github.com/AuSoleil626/Planegame/assets/142735159/29654ce6-f303-403a-bd2d-059e2d7e3e08)



https://github.com/AuSoleil626/Planegame/assets/142735159/fbf12afb-6935-4a33-a30c-57c312b1f528


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

陈延平  策划 美术：主角设计/动画 敌人动画
席琳峰  美术：boss设计/动画 
朱俊宇  美术：敌人设计/动画 敌人子弹设计/动画


姓名：魏启哲
学号：2230012584
负责游戏美术与游戏音效。
美术方面使用Aseprite进行2D像素风格绘制，负责游戏内食物类道具的绘制，开始界面文字的绘制，游戏内角色血条的绘制。
音效方面负责游戏内包括声音：
背景音乐，飞行音效，攻击与击中等音效的制作与剪辑。
